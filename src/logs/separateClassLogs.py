#!/usr/bin/env python
'''
Take the log files for the various days, and separate them by class

This script will take all the log files for a particular server (one for each day)
that are in a particular directory (by server) and separate them into log files for
a given class. The entries are separated by the class identifier found in each log
entry, labeled by the course id in the context structure. 
Created on Feb 5, 2014

@author: waldo
'''
import os
import glob
import json
import csv
import sys
       
def addName(name, dirName):
    '''
    Adds the name of a course to the dictionary of courses, and opens a log file 
    for the entries for that course
    '''
    fname = name + '-' + dirName
    fout = open(fname, 'w')
    return fout
    
def getName(line, institute):
    '''
    Extracts the name of the course from the log entry. If no course name is 
    in the log entry, the log entry goes into the unknown class file
    '''
    try:
        dcl = json.loads(line)
        if 'page' in dcl:
          cl = dcl['page']
        if (cl == None or cl.find(institute) == -1) and ('event_type' in dcl):
          cl = dcl['event_type']
        if (cl == None or cl.find(institute) == -1) and ('event' in dcl):
          cl = dcl['event']
          if isinstance(cl,basestring):
            cl = json.loads(cl)

          if 'course_id' in cl:
            cl = cl['course_id']
          elif 'course' in cl:
            cl = cl['course']
          elif 'problem_id' in cl:
            cl = cl['problem_id']
          else:
            cl = None
        if (cl == None or cl.find(institute) == -1) and ('context' in dcl):
          cl = dcl['context']
          if isinstance(cl,basestring):
            cl = json.loads(cl)

          if 'course_id' in cl:
            cl = cl['course_id']
          elif 'course' in cl:
            cl = cl['course']
          elif 'problem_id' in cl:
            cl = cl['problem_id']
          else:
            cl = None
          
        if cl and cl.find(institute):
          loc1 = cl.find(institute)+len(institute)
          loc2 = cl.find("/",loc1)
          if loc2 == -1:
            cl = cl[loc1:]
          else:
            cl = cl[loc1:loc2]
        else:
          cl = ''       

        cl = cl.replace('/','-') 
        if cl == '':
          cl = 'unknown'
    except ValueError:
        cl = 'unknown'
    return cl.strip(u'\u200b')
    
def getClassList():
    '''
    Returns a dictionary of class names and number of log entries for that class.
    Finds out if there is a ClassList.csv file at the next level of the directory
    hierarchy, and if so reads that file and creates a dictionary of class name and
    log entry counts for the class. Otherwise, returns an empty dictionary. Note 
    that the ClassList.csv file will be written at the end of the extraction of
    class log entries.
    '''
    cldict = {}
    if 'ClassList.csv' in os.listdir('..'):
        clfile = open('../ClassList.csv', 'rU')
        clreader = csv.reader(clfile)
        for cname, count in clreader:
            cldict[cname] = int(count)
        clfile.close()
    return cldict

def get_log_files(startDate, endDate):
    '''
    Returns a sorted list of all of the daily files in the directory. Since the 
    files are sorted by date, the log entries encountered when reading through those
    files will be in time-stamp order.
    '''
    all_logs = glob.glob('20*.log')
    fileList = []
    for f in all_logs:
      fdate = f[:f.index('_')]
      if (fdate >= startDate) and (fdate <= endDate):
        fileList.append(f)
    fileList.sort()
    return fileList

if __name__ == '__main__':
    name = sys.argv[1]
    startDate = sys.argv[2]
    endDate = sys.argv[3]

    full_name = name.split('-')
    institute = full_name[0] + '/'
    course = full_name[1]
    term = full_name[2]
    print "Course Name:", course

    courseDict = {}
    output = None
    dirName = os.getcwd()
    dirName = dirName[dirName.rindex('/')+1:]
    loglist = get_log_files(startDate, endDate)
    print "Processing:"
    print loglist
    for logName in loglist:
        infile = open(logName, 'r')
        for line in infile:
            cName = getName(line, institute)
            if cName:
              if cName == course:
                if not output:
                  output = addName(name, dirName)
                output.write(line)

              if cName not in courseDict:
                courseDict[cName] = 1
              else:
                courseDict[cName] += 1
        infile.close()
    
    if output:
      output.close()

    clFile = csv.writer(open('../ClassList.csv', 'w'))
    for c in iter(courseDict):
      try:
        clFile.writerow([c, courseDict[c]])
      except UnicodeEncodeError:
        print "UnicodeEncodeError at class", c
