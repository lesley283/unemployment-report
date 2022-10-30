
import os
from dotenv import load_dotenv
from pandas import read_csv
from plotly.express import line
from statistics import mean

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}&datatype=csv"

df = read_csv(request_url)

print(df.head())
print(df.columns)
print(len(df))

# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date?
# Display the unemployment rate using a percent sign.

print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
first_row = df.iloc[0]
#print(first_row)
print(f"{first_row['value']}%", "as of", first_row["timestamp"])

# Challenge B
#
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?

# https://stackoverflow.com/questions/11350770/filter-pandas-dataframe-by-substring-criteria
this_year_df = df[df["timestamp"].str.contains("2022-")]
print(this_year_df)

print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{this_year_df['value'].mean()}%")
print("NO MONTHS:", len(this_year_df))

# Challenge C
#
# Plot a line chart of unemployment rates over time.
fig = line(x=df["timestamp"], y=df["value"], title="United States Unemployment Rate over time", labels={
           "x": "Month", "y": "Unemployment Rate"})
fig.show()
