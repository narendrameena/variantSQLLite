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
