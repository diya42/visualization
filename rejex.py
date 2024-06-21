import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from datetime import datetime
import numpy as np
from pandas import read_csv
from matplotlib import pyplot
from pandas import read_csv

df = pd.read_csv('daily-min-temperatures.csv', on_bad_lines='warn', sep=',')
#series = read_csv('daily-min-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=False)
x=df['Date']
# Sample date string

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Temp'], marker='o', linestyle='-', color='b')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Daily Minimum Temperatures')
plt.grid(True)
plt.tight_layout()
plt.show()

date_objs = [datetime.strptime(date, '%m/%d/%Y') for date in df]

# Find minimum and maximum dates
min_date = min(date_objs)
max_date = max(date_objs)

# Calculate the difference in days between max and min dates
date_diff_days = (max_date - min_date).days

# Convert minimum and maximum dates to months
min_month = min_date.month
max_month = max_date.month

# Calculate the difference in months between max and min dates
month_diff = abs(max_month - min_month)

print(f"Dates: {dates}")
print(f"Minimum Date: {min_date.strftime('%m/%d/%Y')}")
print(f"Maximum Date: {max_date.strftime('%m/%d/%Y')}")
print(f"Difference in Days: {date_diff_days} days")
print(f"Month of Minimum Date: {min_month}")
print(f"Month of Maximum Date: {max_month}")
print(f"Difference in Months: {month_diff} months")
'''
date_string = x

# Regular expression pattern to match dd/mm/yyyy format
pattern = r"(\d{2})/(\d{2})/(\d{4})"

# Use re.match to find the date parts
match = re.match(pattern, date_string)

if match:
    month = match.group(1)
    day = match.group(2)
    year=match.group(3)
    print(f"Day: {day}, Month: {month}, Year: {year}")
else:
    print("The date string does not match the expected format.")
'''