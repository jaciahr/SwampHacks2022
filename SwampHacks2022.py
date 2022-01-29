# Load packages we need
import sys
import os
import time

import pickle
import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats as stats
import sklearn
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 16})

# Let's check our software versions
print('### Python version: ' + __import__('sys').version)
print('### NumPy version: ' + np.__version__)
print('### SciPy version: ' + sp.__version__)
print('### Scikit-learn version: ' + sklearn.__version__)
print('### Pickle version: ' + pickle.format_version)
print('------------')




df = pd.read_csv('data.csv', sep='\t')


for col in df.columns:
    if 'E' in col:
        df.drop(columns=col, inplace=True)
    elif 'TIPI' in col: 
        if '4' not in col:
            df.drop(columns=col, inplace=True)
    elif 'I' in col:
        df.drop(columns=col, inplace=True)
    elif 'Q' not in col: 
        df.drop(columns=col, inplace=True)

print(df.head())
