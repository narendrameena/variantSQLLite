#!/usr/bin/python
#author narumeena 
#description density plot for noval varients that ae not reported in 1000k genome project, exome seqencing project and dbsnp or exac dataset 


import subprocess
import sqlite3
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
from operator import itemgetter
sns.set(color_codes=True)

#path to db 
DB = '/Users/naru/Documents/BISR/WESPipelinePaper/benchmarking/ERR034544/gatk/ERR034544.GATK.unifiedgenotyper.raw.default.new.vep.ann.db'

conn = sqlite3.connect(DB)
print("Opened database successfully")

#varients presents in dbsnp 1kg and esp 
variantInDB = conn.execute('''select aaf from variants where in_esp=1 AND in_dbsnp=1 AND in_1kg=1''').fetchall()
variantInDB = list(map(itemgetter(0), variantInDB))
#print(variantInDB)
print(len(variantInDB))

#De novo variants 
variantNotInDB = conn.execute('''select aaf from variants where in_esp=0 AND in_dbsnp=0 AND in_1kg=0''').fetchall()
variantNotInDB = list(map(itemgetter(0), variantNotInDB))
#print(variantNotInDB)
print(len(variantNotInDB))


##multiple curves on one plot 
fig, ax = plt.subplots()

#plotes for known variants 
sns.distplot(variantInDB, hist=False, rug=False, ax=ax,color="k");

#denovo variants 
sns.distplot(variantNotInDB, hist=False, rug=False, ax=ax,color="r");


# labling plotes 
plt.xlabel('Variant Read Frequency')
plt.ylabel('Density')
plt.xlim(0, 1.2)
plt.show()

# message for complet job 
print("Operation done successfully")

# close db connection 
conn.close()

