#!/usr/bin/env python

#To run this demo, put POP.py, rawlog.log (your raw log file) and this example3.py in the same directory. Then run "python POP.py".
#rawlog.log "logID\tlogMessage\n"
#We assume you run this script in the master of Yarn and Spark. If you are running Spark on top of single machine, delete "--master=yarn". 

#In this demo, we assume the POP.py is under the same directory as this file.

import os
import subprocess
import commands
from pprint import pprint

hadoopOutputDir = '/pjhe/test/'
hadoopInputDir = '/pjhe/logs/'


#upload you raw log file from local file system to HDFS
os.system('hadoop fs -rm ' + hadoopInputDir + 'rawlog.log')
os.system('hadoop fs -put rawlog.log ' + hadoopInputDir)

#remove the files in the output directory (initialization), if any
os.system('hadoop fs -rmr ' + hadoopOutputDir)

#submit the POP application to Spark
os.system('spark-submit --master=yarn POP.py')















