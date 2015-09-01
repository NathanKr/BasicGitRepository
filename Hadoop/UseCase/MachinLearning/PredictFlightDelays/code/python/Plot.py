# Python library imports: numpy, random, sklearn, pandas, etc

import warnings
warnings.filterwarnings('ignore')

import sys
import random
import numpy as np

from sklearn import linear_model, cross_validation, metrics, svm
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

import pandas as pd
import matplotlib.pyplot as plt


root = "..\\Data\\"

# --- this is 0.7 GB file and i get memory error on my 4MB RAM PC
# --- so this code is not checked !!!
flt_2007 =  pd.read_csv(root+'2007.csv') 
flt_2007.shape # write size

# --- we want to handle only flights originating from 'ORD'
# --- define coulmn DepDelay : delay > 15 min 
df = flt_2007[flt_2007['Origin']=='ORD'].dropna(subset=['DepDelay'])
df['DepDelayed'] = df['DepDelay'].apply(lambda x: x>=15)
print "total flights: " + str(df.shape[0])
print "total delays: " + str(df['DepDelayed'].sum())


# --- Compute average number of delayed flights per month
grouped = df[['DepDelayed', 'month']].groupby('month').mean()
# --- plot average delays by month
grouped.plot(kind='bar')


# --- Compute average number of delayed flights by hour.
# --- zfill(4)[:2] --> fill left side with 0 so total chars are 4 e.g. 830 is translated
# --- to 0830 and [:2] takes first two chars i.e. 08 then it is translated to int 8 to
# --- represent the hour
df['hour'] = df['CRSDepTime'].map(lambda x: int(str(int(x)).zfill(4)[:2]))
grouped = df[['DepDelayed', 'hour']].groupby('hour').mean()
# --- plot average delays by hour of day
grouped.plot(kind='bar')



# Compute average number of delayed flights per carrier
grouped1 = df[['DepDelayed', 'Carrier']].groupby('Carrier').filter(lambda x: len(x)>10)
grouped2 = grouped1.groupby('Carrier').mean()
carrier = grouped2.sort(['DepDelayed'], ascending=False)
# display top 15 destination carriers by delay (from ORD)
carrier[:15].plot(kind='bar')
