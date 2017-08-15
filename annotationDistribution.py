#!/usr/bin/python
#author narumeena 
#description distribution of annotation type 


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
write_file = "data/annotationDistribution.csv"
with open(write_file, "wb") as outputFile:
    #printing all results a single graph 
    outputFile.write("vcf"+ "," + "commonVariant" +"," + "novalVariantNotDamaging" + ","+ "novalVariantWithDamaging" + "," + "lowFreqVariantNotDamaging" + "," + "lowFreqVariantWithDamaging" +'\n')
    for db in results:
        #make a connection to sqlite db
        conn=sqlite3.connect(db)
        #make sure which db 
        print("opened : " + db)
        print("Opened database successfully")
        #common variants 
        #aaf_gnomad_all > 0.05
        commonVariantCount = conn.execute('''select count(*) from variants where aaf_gnomad_all > 0.05''').fetchall()
        commonVariantCount = list(map(itemgetter(0), commonVariantCount))[0]

        print("commonVariantCount = " , commonVariantCount)

        #noval variants not damaging 
        #is_lof = 0 and in_dbsnp = 0

        novalVariantNotDamaging = conn.execute('''select count(*) from variants where is_lof = 0 and in_dbsnp = 0''').fetchall()
        novalVariantNotDamaging = list(map(itemgetter(0), novalVariantNotDamaging))[0]

        print("novalVariantNotDamaging  = " , novalVariantNotDamaging)

        #noval variants with damaging 
        #is_lof = 1 and in_dbsnp = 0

        novalVariantWithDamaging = conn.execute('''select count(*) from variants where is_lof = 1 and in_dbsnp = 0''').fetchall()
        novalVariantWithDamaging = list(map(itemgetter(0), novalVariantWithDamaging))[0]

        print("novalVariantWithDamaging = " , novalVariantWithDamaging)

        #low frequecy variants not damaging 
        #is_lof = 0 and in_dbsnp = 0 and aaf_gnomad_all < 0.05 and aaf_gnomad_all > 0.01

        lowFreqVariantNotDamaging = conn.execute('''select count(*) from variants where is_lof = 0 and in_dbsnp = 0 and aaf_gnomad_all < 0.05 and aaf_gnomad_all > 0.01''').fetchall()
        lowFreqVariantNotDamaging = list(map(itemgetter(0), lowFreqVariantNotDamaging))[0]

        print("lowFreqVariantNotDamaging = " , lowFreqVariantNotDamaging)

        #low frequecy variants wit damaging 
        #is_lof = 1 and in_dbsnp = 0 and aaf_gnomad_all < 0.05 and aaf_gnomad_all > 0.01

        lowFreqVariantWithDamaging = conn.execute('''select count(*) from variants where is_lof = 1 and in_dbsnp = 0 and aaf_gnomad_all < 0.05 and aaf_gnomad_all > 0.01''').fetchall()
        lowFreqVariantWithDamaging = list(map(itemgetter(0), lowFreqVariantWithDamaging))[0]

        print("lowFreqVariantWithDamaging = " , lowFreqVariantWithDamaging)

        line = db + "," + str(commonVariantCount) +"," + str(novalVariantNotDamaging) + ","+ str(novalVariantWithDamaging) + "," + str(lowFreqVariantNotDamaging) + "," + str(lowFreqVariantWithDamaging)
        #writing output to csv file 
        outputFile.write(line + '\n')
        # close db connection 
        conn.close() 

#finding noval varaints 
#select * from variants where is_lof = 1 and in_dbsnp = 0
#aaf_exac_all 0.05 >rare  commom > 0.10 
#is_lof 1 damaging
#noval in_dbsnp
