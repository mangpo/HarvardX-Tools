# save this file as ......| test1.py
# run this file this way..| python  test1.py
import easygui as eg
import sys, os
import subprocess
import requests



title = "Edx Data Formatter"
eg.msgbox("In each prod-edx-NNN directory, decrypt all log files and place them in the same directory.\n \n After pressing OK, select the folders 'edX-datascrub' on your computer ", title)



edxRootSpace = eg.diropenbox("Please select the edX-datascrub folder on your computer.", "Select Root Folder")

eg.msgbox("After pressing OK, select the folder containing 'generateCourseAxis' on your computer ", title)


courseAxisRoot = eg.diropenbox("Please select the datascrub folder on your computer.", "Select Root Folder")

edxRoot = edxRootSpace.replace(' ','\ ')
addPathSrc = edxRoot + "/src"
# ex = "export PATH=$PATH:" + edxRoot + "/src"
addPathLog = edxRoot + "/src/logs"
addPathShell = edxRoot + "/shellscripts"

# print addPathSrc
# os.system(addPathSrc)
#subprocess.call(['export', ex])
# p1 = subprocess.Popen([addPathSrc], stdout=subprocess.PIPE, shell=True)
# print p1.communicate()
# subprocess.call([addPathLog], shell=True)
os.environ["PATH"] += os.pathsep + edxRootSpace + "/src"
os.environ["PATH"] += os.pathsep + edxRootSpace + "/src/logs"
os.environ["PATH"] += os.pathsep + edxRootSpace + "/shellscripts"
os.environ["PATH"] += os.pathsep + courseAxisRoot
# subprocess.call([addPathShell], shell=True)
# permissionSrc = "chmod -R 777 " + edxRoot + "/*"
courseAxisRootNoSpace = courseAxisRoot.replace(' ','\ ')

permissionSrc = "chmod -R 777 " + addPathSrc
permissionLog = "chmod -R 777 " + addPathLog
permissionShell = "chmod -R 777 " + addPathShell
axisPermission = "chmod -R 777 " + courseAxisRootNoSpace
subprocess.call([permissionSrc], shell=True) 
subprocess.call([permissionLog], shell=True) 
subprocess.call([permissionShell], shell=True) 
subprocess.call([axisPermission], shell=True) 


eg.msgbox("Select the directory which contains the classXXX.xml.tar.gz file", "Generate course_axis")
axisFolder = eg.diropenbox("Please select the classXXX.xml.tar.gz file on your computer.", "Select Root Folder")
os.chdir(axisFolder)
subprocess.call(["generateCourseAxis ."],shell=True)

msg = "Institution: Please enter the name of your institution as listed on edx followed by a capital letter X. Ex. BerkeleyX. (This is case-sensitive). \n Select the dates for which you would like data. Format: YYYY-MM-DD \n After filling in the fields, select the folder with all of your prod-edx-NNN files."
title = "Seperate Log Files"
fieldNames = ["Institution", "Start Date", "End Date"]
fieldValues = []
fieldValues = eg.multenterbox(msg,title,fieldNames)
if not fieldValues:
    sys.exit(0)

logFilesCommand = 'processLogData.sh ' + fieldValues[0] + " " + fieldValues[1] + " " + fieldValues[2]
#subprocess.Popen('cd setPath', shell=True)
setPath = eg.diropenbox("Please select the folder containing prod-edx-NNN files.", "Select Folder")
# setPath = setPath.replace(' ','\ ')
os.chdir(setPath)
subprocess.call([logFilesCommand], shell=True)
#subprocess.Popen('python csv_parser.py')
while 1:
    msg = "Select the files that you would like to transform to formatted csv files one by one or transform them all."
    title = "Transform Files"
    choices = ('Choose file', 'Cancel')
    bbox = eg.buttonbox(msg, title, choices)
    if bbox == 'Choose file':
        curFile = eg.fileopenbox('Choose file to transform', 'Transform file', filetypes = ["*.log"])
        command = 'transformOneLog.sh ' + curFile + " " + axisFolder + "/course_axis.csv"
        print command
        subprocess.call([command],shell=True)
    # elif bbox == 'Transform all files':
    #     subprocess.call(['transformAllLogs.sh'],shell=True)
    #     eg.msgbox('All files have been transformed. Thank you!','Files Transformed')
    #     sys.exit(0)
    else:
        sys.exit(0)


