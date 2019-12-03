import math
import itertools
import pandas
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from time import time
from collections import OrderedDict
gt0 = time()

avl_data = "processed_avl_data.csv"
cols = ["VEHICLE_CODE","LAST_STOP_CODE","LAST_STOP_TIME", "DIRECTION","BUS_AT_STOP_SECS"]
data = pd.read_csv(avl_data)
data = data[cols]
print (data.head())

print ("\nOk! So There are total " + str(len(data[cols[0]].value_counts())) + " buses!")

# Segregate data into diff directions
upDirData = data[data['DIRECTION'].isin([0])]
downDirData = data[data['DIRECTION'].isin([1])]

print ("\nAnd! " + str(len(upDirData[cols[0]].value_counts())) + " buses are running in one direction!\n")
print ("While! " + str(len(downDirData[cols[0]].value_counts())) + " buses are running in other direction!\n")

# Let's Start Learning in Upward Dir (i.e. dir 0)
stopsInUpGo = [160, 161, 162, 163, 164, 165, 166, 167, 168, 133, 134, 65, 66, 177, 178, 179, 270, 180, 181, 182, 183, 184, 185, 304, 186, 187]

# It looks some unknown bus stops in given data, so lets filter them
upDirData = upDirData[data['LAST_STOP_CODE'].isin(stopsInUpGo)]
print (upDirData.head())
#upDirData.to_csv('AFURADA-BOAVISTA.csv')

busesStartingFromAF = upDirData[data['LAST_STOP_CODE'].isin([160])]
busesReachingAtBO = upDirData[data['LAST_STOP_CODE'].isin([187])]

vehiclesStartingAtAF = list(set(busesStartingFromAF["VEHICLE_CODE"].tolist()))
vehiclesReachingAtBO = list(set(busesReachingAtBO["VEHICLE_CODE"].tolist()))

print ("\nAnalyzing the Data, " + str(vehiclesStartingAtAF) + " are starting from AFURADA and " + str(vehiclesReachingAtBO) + " are reaching to BOAVISTA")
print( "\n Concluding " + str(list(set(vehiclesStartingAtAF) & set(vehiclesReachingAtBO))) + " vehicles can make us travel between AFURADA-BOAVISTA")