import pandas as pd
#read data from csv file into DataFrame
df = pd.read_csv("sampleData-1.csv")
print("\n**** Data from CSV file  ****\n")
print(df)
print(df.describe())