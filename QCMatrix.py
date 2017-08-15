#!/usr/bin/python
#author narumeena 
#description quality matrix for diffrent variant caller pipelines 

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
write_file = "data/QcMatrix.csv"
with open(write_file, "wb") as outputFile:
    #printing all results a single file 
    outputFile.write("vcf"+ "," + "novalSNP" +"," + "allSNP"  +'\n')
    for db in results:
        #make a connection to sqlite db
        conn=sqlite3.connect(db)
        #make sure which db 
        print("opened : " + db)
        print("Opened database successfully")
        #noval variants 
        #snp count in vcf file 
        novalsnpCount = conn.execute('''select count(*) from variants where type="snp" AND in_esp=0 AND in_dbsnp=0 AND in_1kg=0''').fetchall()
        novalsnpCount = list(map(itemgetter(0), novalsnpCount))[0]
        print(novalsnpCount)

        #all snp count in vcf file 
        allSnpCount = conn.execute('''select count(*) from variants where type="snp"''').fetchall()
        allSnpCount = list(map(itemgetter(0), allSnpCount))[0]
        print(allSnpCount)
        line = db + "," + str(novalsnpCount) +"," + str(allSnpCount)
        #writing output to csv file 
        outputFile.write(line + '\n')
        # close db connection 
        conn.close()

