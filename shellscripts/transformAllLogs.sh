#Tranform all json logs into nicely formatted csv logs.

for line in `ls *.log`;
do
    echo $line
    transformOneLog.sh $line
done