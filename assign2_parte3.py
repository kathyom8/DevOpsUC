import subprocess
import csv

from crontab import CronTab  
  
pytonProcess = subprocess.check_output('ps -e | wc -l', shell=True).decode()
pytonProcess = pytonProcess.split('\n')
  

# open the file in the write mode
f = open('/home/katherine/Documents/DevOps_UC/listprocess.csv', 'a+')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(pytonProcess)

# close the file
f.close()
