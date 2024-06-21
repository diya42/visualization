import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from datetime import datetime
import numpy as np
from pandas import read_csv
from matplotlib import pyplot
from pandas import read_csv
#Demonostration of Run Sequence Plot
series = read_csv('daily-min-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=True)


'''
df = pd.read_csv('daily-min-temperatures.csv', parse_dates=[['Date']])
print(df)

'''
series.plot(style='k.')
pyplot.show()

print(series[0:5])
