### INPUT VALUES ####

#region
file_loc = 'C:/FILES/Algae/DRINKING_WATER_HISTORIC-From-Hansen-DB.csv'

# Name of datafile for checking
Output_Extension = '.csv'
Delimiter = ','
ChunckSize = 500

# LOAD DATA
import pandas as pd
DataFile = pd.read_csv(file_loc, sep=Delimiter, dtype=object)
#endregion


# Import Libs
#region
import numpy as np
import os
import re
import csv
#endregion


# Script
print('FILE READ')
NumToRemove = -1 * (len(Output_Extension))
Output_filename = file_loc[:NumToRemove]
Full_Filepath = Output_filename + Output_Extension
Row_Max = int((DataFile.shape[0])-1)
NoChuncks = Row_Max/ChunckSize
NoChuncksInt = int(NoChuncks)
PartialChunck = NoChuncks - NoChuncksInt

if PartialChunck > 0:
    Bool_PartialChunck = True
else:
    Bool_PartialChunck = False

counter = int(0)
FromRow = 0
ToRow = ChunckSize

while counter <= NoChuncksInt:
    df_temp=DataFile.iloc[FromRow:ToRow, :]
    FromRow = ToRow
    ToRow = ToRow + ChunckSize
    counter += 1
    FName = Output_filename + str(counter) + Output_Extension
    df_temp.to_csv(path_or_buf=FName, sep=Delimiter, index=False)

if PartialChunck == True:
    counter += 1
    FName = Output_filename + str(counter) + Output_Extension
    df_temp=DataFile.iloc[FromRow::, :]
    df_temp.to_csv(path_or_buf=FName, sep=Delimiter, index=False)

print('ALL DONE!!!!!!!!!!!!!!!!!!')