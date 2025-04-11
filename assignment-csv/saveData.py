import pandas as pd
#data in a list
data = [[122, 58.5, 78],
        [165, 49.90, 22],
        [175, 72.90, 38]]
#create pandas Dataframe with column name
df = pd.DataFrame(data, columns= ["Age"])
#Save the Dataframe into a CSV file
#index=False argument ensures that the DataFrame's index is not included in the CSV file.
df.to_csv("sampleData-1.csv", index= True)
print("numerical Data saved in a csv file, called sampleData-1")