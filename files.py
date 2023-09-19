import civis
import os
from os import listdir
from os.path import isfile, join

sql = 'select 123'

fut = civis.io.civis_to_csv('temp.csv', sql, 32, compression=None)

fut.result()

cwd = os.getcwd()
onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd) if 
os.path.isfile(os.path.join(cwd, f))]
print(onlyfiles) 
