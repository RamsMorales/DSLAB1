import pandas as pd

#-----------------------------------------------------------------------------------------------------
#                                               Step 1
#-----------------------------------------------------------------------------------------------------
## Load the data
oct2524Measurements = pd.read_csv("data/oct25-2024.csv")

## Display the first few rows
#print(data.head()) data loaded

## Print basic dataset information (columns, data types, missing values)
print(oct2524Measurements.info()) # based on the output we don't have any missing values although dropping, averaging, and per category averaging are available options

#-----------------------------------------------------------------------------------------------------
#                                               Step 2
#-----------------------------------------------------------------------------------------------------

## Compute summary statistics 
print(oct2524Measurements.describe())
