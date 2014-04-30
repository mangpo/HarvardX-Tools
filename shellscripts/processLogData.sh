# Process all of the log data from an edX dump. This script will result in a WeeklyLog for
# each course.

# The script takes two parameters:
# argument 1: the day from which the log entries are to be processed 
#             (the first day of the week) in YYYY-MM-DD format.
# argument: 2 the last day from which the log entries are to be processed 
#             (the last day the log files were collected) in YYYY-MM-DD format.

# Get rid of any files that have already been processed.
for line in `ls | grep prod`;
do
    cd $line
    cullLogFiles.py $2 $3
    cd ..
done

# If any of the directories is empty, simply remove it.
rmdir *

# Separate out the log entries in each directory by the class.
for line in `ls | grep prod`;
do
    cd $line
    separateClassLogs.py $1
    cd ..
done

# Build a log for the week for each of the classes, writing the log to the current directory
buildWeekLog.py





