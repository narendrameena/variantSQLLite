#!/usr/bin/python
#author narumeena 
#description density plot for noval variants  that are not reported in 1000k genome project, exom sequencing project and dbsnp or exac dataset 


import subprocess
import sqlite3
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
from operator import itemgetter #
sns.set(color_codes=True)
import csv

import os
import re
import fnmatch

#getting list of all db from sub-directories 
DBFolders="/Users/naru/Documents/BISR/WESPipelinePaper/benchmarking/ERR091571/"
results = []
for root, dirs, files in os.walk(DBFolders):
    for _file in files:
        if fnmatch.fnmatch(_file, '*.db'):
            results.append(os.path.join(root, _file))

print(results)

##multiple curves on one plot 
fig, ax = plt.subplots()

#printing all results a single graph 
for db in results:
    #make a connection to selite db
    conn=sqlite3.connect(db)
    #make sure which db 
    print("opened : " + db)

    #known variants, present in esp and 1kg and dbsnp datasets 
    variantInDB = conn.execute('''select aaf from variants where in_esp=1 AND in_dbsnp=1 AND in_1kg=1''').fetchall()
    variantInDB = list(map(itemgetter(0), variantInDB)) #first column 
    print("known variants : " + str(len(variantInDB)) +  "\n")
    
    #plot for known variants 
    sns.distplot(variantInDB, hist=False, rug=False, ax=ax,color="k")


    #de novov variants, not in dbsnp, esp and 1kg 
    variantNotInDB = conn.execute('''select aaf from variants where is_lof AND in_esp=0 AND in_dbsnp=0 AND in_1kg=0''').fetchall()
    variantNotInDB = list(map(itemgetter(0), variantNotInDB)) # first column 
    print("denovo variants : " + str(len(variantNotInDB )) +  "\n")
    #plot denovo variants 
    sns.distplot(variantNotInDB, hist=False, rug=False, ax=ax,color="r")
    
    
    # close db connection 
    conn.close()


# labling plotes 
plt.xlabel('Variant Read Frequency')
plt.ylabel('Density')
plt.xlim(0, 1.2)

plt.show()

# message for complet job 
print("Operation done successfully")



#path to db 
#DB = '/Users/naru/Documents/BISR/WESPipelinePaper/benchmarking/ERR034544/gatk/ERR034544.GATK.unifiedgenotyper.raw.default.new.vep.ann.db'

#conn = sqlite3.connect(DB)
#print("Opened database successfully")

#variants presents in dbsnp 1kg and esp 
#print("known varints! \n")
#variantInDB = conn.execute('''select aaf from variants where in_esp=1 AND in_dbsnp=1 AND in_1kg=1''').fetchall()
#variantInDB = list(map(itemgetter(0), variantInDB))
#print(variantInDB)
#print(len(variantInDB))

#De novo variants 
#print("Unknowen variants from DBs! \n ")
#variantNotInDB = conn.execute('''select aaf from variants where in_esp=0 AND in_dbsnp=0 AND in_1kg=0''').fetchall()
#variantNotInDB = list(map(itemgetter(0), variantNotInDB))
#print(variantNotInDB)
#print(len(variantNotInDB))


##multiple curves on one plot 
#fig, ax = plt.subplots()

#plots for known variants 
#sns.distplot(variantInDB, hist=False, rug=False, ax=ax,color="k");

#denovo variants 
#sns.distplot(variantNotInDB, hist=False, rug=False, ax=ax,color="r");


# labling plotes 
#plt.xlabel('Variant Read Frequency')
#plt.ylabel('Density')
#plt.xlim(0, 1.2)
#plt.show()

# message for complet job 
##print("Operation done successfully")

# close db connection 
#conn.close()
