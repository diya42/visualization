import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from datetime import datetime
import numpy as np
from pandas import read_csv
from matplotlib import pyplot
from pandas import read_csv

#Demonostration of Box Plot
lst = [25, 145, 145, 148, 178, 178, 198, 201, 222, 210, 565, 589, 485, 333, 358, 158, 25]

df = pd.DataFrame(lst)
df.boxplot(column = 0)
plt.show()
data = {
    'Category A': [25, 35, 45, 55, 65, 75, 85, 95, 105, 115],
    'Category B': [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
    'Category C': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
}
df1 = pd.DataFrame(data)
print(data['Category A'])
df1.boxplot()
plt.title('Box Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
# Show the plot
plt.show()