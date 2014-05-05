#Tranform all json logs into nicely formatted csv logs.

for log in `ls *.log`;
do
    echo $log
    axis=${log:0:`expr length $log - 4`}.csv
    echo transformOneLog.sh $log $axis
done