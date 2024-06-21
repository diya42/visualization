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
x = [] 
y = [] 

with open('daily-min-temperatures.csv','r') as csvfile: 
    lines = read_csv(csvfile, delimiter=',') 
    for row in lines: 
        x.append(row[0]) 
        y.append(int(row[1])) 
  
plt.plot(x, y, color = 'g', linestyle = 'dashed', 
         marker = 'o',label = " Data") 
  
plt.xticks(rotation = 25) 
plt.xlabel('Dates') 
plt.ylabel('Temperature(°C)') 
plt.title('daily-min-temperatures.csv', fontsize = 20) 
plt.grid() 
plt.legend() 
plt.show()