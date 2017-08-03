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
sns.set(color_codes=True)



#path to db 
DB = '/Users/naru/Documents/BISR/WESPipelinePaper/benchmarking/ERR034544/gatk/ERR034544.GATK.haplotypecaller.raw.default.snpeff.ann.new.db'
#path to gemini 
GEMINI = '/Users/naru/Documents/BISR/software/gemini/bin/gemini'

conn = sqlite3.connect(DB)
print "Opened database successfully";
cursor = conn.execute('''select depth from variants''')
data = cursor.fetchall()
readFreq = map(itemgetter(0), data)
print readFreq
print len(readFreq)
sns.distplot(readFreq, hist=False, rug=True);

print "Operation done successfully";
conn.close()

