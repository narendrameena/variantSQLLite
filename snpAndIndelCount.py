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
from operator import itemgetter
sns.set(color_codes=True)

#path to db 
DB = '/Users/naru/Documents/BISR/WESPipelinePaper/benchmarking/ERR034544/gatk/ERR034544.GATK.haplotypecaller.raw.default.new.vep.ann.db'

conn = sqlite3.connect(DB)
print("Opened database successfully")



#snp count 
#snpCount = conn.execute('''select type,count(*) from variants''').fetchall()
snpCount = conn.execute('''select count(*) from variants where type="snp"''').fetchall()
snpCount = list(map(itemgetter(0), snpCount))[0]

print(snpCount)




