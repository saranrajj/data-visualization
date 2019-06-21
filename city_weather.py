import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()
#Load the CSV file
summarySheet = pd.read_csv('./data/mumbai.csv')

#List used to retain the month order
months = ["December", "November", "October", "September",
          "August","July", "June", "May", "April", "March", "February", "January"]

#load only required columns
skipColDf = summarySheet[["Month","Year","temp"]]

#calculate average temperature by month & Year
day1Summary = skipColDf.groupby(["Month","Year"], as_index=False).mean()
day1Summary.temp = day1Summary.temp.astype('int64')

day1Summary['Month'] = pd.Categorical(day1Summary['Month'], categories=months, ordered=True)
summary = day1Summary.pivot("Month", "Year", "temp")

#Draw heatmap
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(summary, annot=True, linewidths=.5, ax=ax ,cmap="bwr")
plt.title("Mumbai Weather")
plt.show()