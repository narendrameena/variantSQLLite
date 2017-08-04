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
from operator import itemgetter
sns.set(color_codes=True)


#path to db 
DB = '/Users/naru/Documents/BISR/WESPipelinePaper/benchmarking/ERR034544/gatk/ERR034544.GATK.haplotypecaller.raw.default.new.vep.ann.db'

conn = sqlite3.connect(DB)
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



#finding noval varaints 
#select * from variants where is_lof = 1 and in_dbsnp = 0
#aaf_exac_all 0.05 >rare  commom > 0.10 
#is_lof 1 damaging
#noval in_dbsnp
