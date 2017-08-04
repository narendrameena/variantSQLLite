#!/usr/bin/python
#author narumeena 
#description intial script to play with a varait sqlite db genrated by gemini : cheers

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
#path to gemini 
GEMINI = '/Users/naru/Documents/BISR/software/gemini/bin/gemini'

#running gemini commmand and caching the output in a variable 
output = subprocess.check_output(GEMINI + ' query -q "select * from variants where is_lof = 1 and in_dbsnp = 0" --header '+ DB, shell=True)
#print "program output:", output


#query direct to db 

conn = sqlite3.connect(DB)
print "Opened database successfully";
#cursor = conn.execute('''select depth from variants''')
#data = cursor.fetchall()
#readFreq = map(itemgetter(0), data)
#print readFreq
#sns.distplot(readFreq, hist=False, rug=True);

print "Operation done successfully";
conn.close()




#direct from gemini 
#running gemini commmand and caching the output in a variable 
#output = subprocess.check_output(GEMINI + ' query -q "select count(*) from variants where is_lof =  and in_dbsnp = 1"  --header ' + DB, shell=True)


output = subprocess.check_output(GEMINI + ' de_novo --columns "chrom,start,end" ' + DB, shell=True)

 #gemini de_novo --columns "chrom,start,end" test.de_novo.db
#print "program output:", output
print(output)