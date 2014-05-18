edX-datascrub is used for scrubbing edX data into a format that is easy to analyze. This repository is forked from [HarvardX-Tools](http://github.com/jimwaldo/HarvardX-Tools).

**Output:** The final processed data of each class is stored in csv file with the following fields: 
* time
* seconds to next action
* actor: user
* verb: action
* object_name: in the format of chapter/sequential/vertical/item_name
* object_type
* result: correct or incorrect if verb is problem_check, empty otherwise
* meta
* ip
* event_type
* page
* agent

The output rows are partially sorted by times. More specifically, if you only consider rows associated to one user, those rows are sorted by times.

# Setting Up
1. Clone this repository and [edX-courseaxis](http://github.com/kk415kk/datascrub) repository.
2. Add the following directories to your environment path
  * edX-datascrub/src
  * edX-datascrub/src/logs
  * edX-datascrub/shellscripts
  * edX-courseaxis
3. Make sure all shellscripts and python scripts inside these 4 directories are executable.
4. Decrypt all files from edX and store them in the same directories.

Then, you're ready to go!

# Obtaining Course Axis

Every class comes with class information and content packaged in classXXX.xml.tar.gz. Run `generateCourseAxis` script in the directory that contains classXXX.xml.tar.gz:

```
generateCourseAxis dir_contains_class_xml_targz
```

The script will generate many files including:
* info.csv collecting course names (e.g. BerkeleyX-CS191x-Spring_2013), start dates, and end dates of all classes
* one <course_name>_axis.csv for each class
* axis.error logging all the errors occurred during generating course axes. Check the error messages in this file to investigate why the course axis of any particular class is not being generated.

info.csv and course axes will be used in the next step. Note that if there is an error generating course axis or there is no start or end date for a specific class in its xml.tar.gz, that class is excluded from info.csv.

# Processing Activity Logs

You can choose to process activity logs of all classes at once or just one log of a specific class at a time.

## Processing All Logs

In the directory that contains prod-edx* directories in which contain the raw activity logs, simply run:

```
processAll.py path_to_info.csv
```

The script will:
* generate a separate log file for each class inside each prod-edx* directory. The log file is named after the class name.
* combine the separated log files of the same class located in different prod-edx* directories into one log file and store the combined log in the directory in which the script is run.
* transform the combined log file into a nicely formatted csv file for each class.

Note that the script will only generate the nicely formatted csv files for the classes listed in info.csv generated from the previous step.

## Processing One Log

In the directory that contains prod-edx* directories in which contain the raw activity logs, run:

```
processLogData.sh course_name start_date end_date
transformOneLog.sh course_name.log path_to_course_axis.csv
```

You can get `course_name`, `start_date`, and `end_date` from info.csv. Make sure to pick the correct course axis from many course axes generated from the previous step. If you do not want to process raw log data for the entire period that the course is offered, you can simply change `start_date` and `end_date` to your period of interest. 

`processLogData.sh` will generate `course_name.log` in the directory in which the script is running. `transformOneLog.sh` takes the generated `course_name.log` and the corresponding course axis generated from the Obtaining Course Axis section as its inputs.
