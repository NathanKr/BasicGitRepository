This is based on http://hortonworks.com/hadoop-tutorial/hands-on-tour-of-apache-spark-in-5-minutes/

on hortonworks linux sandbox HDP 2.3_1 :

// --- get some html file and save to HDFS via hadoop fs
[root@sandbox ~] #  wget http://en.wikipedia.org/wiki/Hortonworks
[root@sandbox ~] #  hadoop fs -put ~/Hortonworks /user/guest/Hortonworks

// --- open python API to spark
[root@sandbox ~] #  pyspark

// --- open the file on HDFS
>>> myLines = sc.textFile('hdfs://sandbox.hortonworks.com/user/guest/Hortonworks')

// --- only non empty lines counts
>>> myLines_filtered = myLines.filter( lambda x: len(x) > 0 )

// --- count number of lines
>>> myLines_filtered.count()