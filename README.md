edX-datascrub
==============
edX-datascrub is used for scrubbing edX data into a format that is easy to analyze. This repository is forked from HarvardX-Tools: github.com/jimwaldo/HarvardX-Tools.

1) Process courses's metadata

python src/buildClassList.py
python src/separateClassFiles.py

2) (Optional) Clean up log. Get rid of any files that have already been processed, passing in the first date of a log that we want to keep as the command to the scripts. The script takes two parameters-- the first is the day from which the log entries are to be processed (the first day of the week) in YYYY-[MM-DD format, while the second is the identifier of the week, in YYYY-MM-DD format, generally the timestamp of the log file dump produced by edX (and which tends to be the last day the log files were collected in this dump. Run the following command under the directory in which the log file is.

python src/cullLogFiles.py start_time end_time

3) Separate out the log entries in each directory by the class. Run the following command under the directory in which the log file is.

python src/separateClassLogs.py

4) For each class, generate course axis

TODO

5) Separate log file into different log files for different classes:

python src/logs/separateClassLogs.py name_of_institute

name_of_institute has to match with with the name in the URL path. For example, name_of_institute = BerkeleyX

6) On each class's log file, generate nicely formatted CSV file for data analysis by running:

python src/makePersonClick.py class_log course_axis output_file.csv

kkao@berkeley.edu
