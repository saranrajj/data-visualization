import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()
#Load the CSV file
df = pd.read_csv('./data/mumbai.csv')

#List used to retain the month order
months = ["December", "November", "October", "September",
          "August","July", "June", "May", "April", "March", "February", "January"]

#load only required columns
skipColDf = df[["Month","Year","temp"]]

#calculate average temperature by month & Year
groupDf = skipColDf.groupby(["Month","Year"], as_index=False).mean()
groupDf.temp = groupDf.temp.astype('int64')

groupDf['Month'] = pd.Categorical(groupDf['Month'], categories=months, ordered=True)
summary = groupDf.pivot("Month", "Year", "temp")

#Draw heatmap
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(summary, annot=True, linewidths=.5, ax=ax ,cmap="bwr")
plt.title("Mumbai Weather")
plt.show()