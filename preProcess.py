import pandas as pd

avl_csv = "avl_data.csv"

# Dropping attributes ID, LATITUDE, LONGITUDE, LOG_TIMESTAMP
col_names = ["VEHICLE_CODE","LINE_CODE","LAST_STOP_CODE","STATUS_TIME","LAST_STOP_TIME","LOG_TIMESTAMP"]
bin_cols = ["VEHICLE_STATUS", "ERROR", "DIRECTION"]

data = pd.read_csv(avl_csv)
data = data[col_names + bin_cols]

# Exploratory Data Analysis
def removeColsWithoutImpact(cols):
    col = 0
    for index in range(len(cols)):
        if len(data[cols[col]].value_counts()) == 1:
            # Looks like this is not making any impact on given data.
            print (cols[col] + " is not having any impact on given dataset, hence DROPPING!")
            cols.pop(col)
        else:
            col += 1


# For Binary Cols
removeColsWithoutImpact(bin_cols)
# For Other Cols
removeColsWithoutImpact(col_names)
data = data[col_names + bin_cols]
print (data.head())

indices_to_remove = []
from datetime import datetime
def getTime (datetimeStr):
    return datetime.strptime(datetimeStr, '%d/%m/%y %H:%M')

new_list = []
def inLoop(index, ms1, stIn):
    maxDiff = 0
    for nxtIndex in range(len(data) - index - 1):
        if data["LAST_STOP_CODE"][index] == data["LAST_STOP_CODE"][stIn]:
            ms2 = getTime(data["LAST_STOP_TIME"][stIn])
            diff = (ms2 - ms1).total_seconds()
            if  diff > 300:
                return maxDiff
            else:
                if diff > maxDiff:
                    maxDiff = diff
                indices_to_remove.append(stIn)
        stIn += 1
 
# For Redundant Cols LAST_STOP_CODE
for index in range(len(data)):
    # print (index)
    if index not in indices_to_remove:
        ms1 = getTime(data["LAST_STOP_TIME"][index])
        stIn = index + 1
        diff = inLoop(index, ms1, stIn)
        if diff is None:
            diff = 0
        dlst = data.iloc[index, :].tolist()
        dlst.append(int(diff))
        new_list.append(dlst)

cols = []
cols.extend(col_names)
cols.extend(bin_cols)
cols.append("BUS_AT_STOP_SECS")
avl_data = pd.DataFrame(new_list, columns=cols)
print ("Processed Data")
print (avl_data.head())
avl_data.to_csv('processed_avl_data.csv')