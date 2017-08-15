#!/usr/bin/python
#author narumeena 
#description box plot ofr indel and snp count from gemini db 

import subprocess
import sqlite3
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
from operator import itemgetter #
import csv
import os
import re
import fnmatch

#getting list of all db from sub-directories 
DBFolders="/Users/naru/Documents/BISR/WESPipelinePaper/benchmarking/"
results = []
for root, dirs, files in os.walk(DBFolders):
    for _file in files:
        if fnmatch.fnmatch(_file, '*.db'):
            results.append(os.path.join(root, _file))

print(results)
write_file = "data/snpAndIndelCount.csv"
with open(write_file, "wb") as outputFile:
    #printing all results a single graph 
    outputFile.write("vcf"+ "," + "snpCount" +"," + "indelCount" + '\n')
    for db in results:
        #make a connection to sqlite db
        conn=sqlite3.connect(db)
        #make sure which db 
        print("opened : " + db)
        print("Opened database successfully")
        #snp count in vcf file 
        snpCount = conn.execute('''select count(*) from variants where type="snp"''').fetchall()
        snpCount = list(map(itemgetter(0), snpCount))[0]
        print(snpCount)

        #indel count in vcf file 
        indelCount = conn.execute('''select count(*) from variants where type="indel"''').fetchall()
        indelCount = list(map(itemgetter(0), indelCount))[0]
        print(indelCount)

        line = db + "," + str(snpCount) +"," + str(indelCount)
        #writing output to csv file 
        outputFile.write(line + '\n')
        # close db connection 
        conn.close()



