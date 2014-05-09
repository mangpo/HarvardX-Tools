edX-datascrub is used for scrubbing edX data into a format that is easy to analyze. This repository is forked from [HarvardX-Tools](http://github.com/jimwaldo/HarvardX-Tools).

# Setting up
1. Clone the repository.
2. Add the following directories to your environment path
  * edX-datascrub/src
  * edX-datascrub/src/logs
  * edX-datascrub/shellscripts

Then, you're ready to go!

# Processing Raw Activity Logs

Please refer to our [wiki](http://github.com/mangpo/edX-datascrub/wiki) on how to use the scripts.

All
1) generateCourseAxis .
2) processAll.py info.csv

One Course
1) generateCourseAxis .
2) processLogData.sh cname start end
3) transformOneLog.sh cname course_axis.csv
