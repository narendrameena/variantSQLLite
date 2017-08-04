#!/usr/bin/python
#author narumeena 
#description pie chart of caller variant overlap 

import subprocess
import sqlite3
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
from operator import itemgetter
sns.set(color_codes=True)


DB = '/Users/naru/Documents/BISR/WESPipelinePaper/benchmarking/ERR034544/gatk/ERR034544.GATK.unifiedgenotyper.raw.default.new.vep.ann.db'