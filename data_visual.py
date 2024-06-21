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

#Demonostration of Heat Map
np.random.seed(0)
uniform_data = np.random.rand(3, 3)
ax = sns.heatmap(uniform_data)


#Demonostration of Histogram
sns.displot(lst, bins=4)
plt.show()

#Demonstration of Scatter Plot
Age = [5,7,8,7,2,17,2,9,4,11,12,9,6]
Speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(Age, Speed)
plt.show()

#Demonstration of Pareto Chart
def pareto_plot(df, x=None, y=None, title=None, show_pct_y=False, pct_format='{0:.0%}'):
    xlabel = x
    ylabel = y
    tmp = df.sort_values(y, ascending=False)
    x = tmp[x].values
    y = tmp[y].values
    weights = y / y.sum()
    cumsum = weights.cumsum()
    
    fig, ax1 = plt.subplots()
    ax1.bar(x, y)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)

    ax2 = ax1.twinx()
    ax2.plot(x, cumsum, '-ro', alpha=0.5)
    ax2.set_ylabel('', color='r')
    ax2.tick_params('y', colors='r')
    
    vals = ax2.get_yticks()
    ax2.set_yticklabels(['{:,.2%}'.format(x) for x in vals])

    # hide y-labels on right side
    if not show_pct_y:
        ax2.set_yticks([])
    
    formatted_weights = [pct_format.format(x) for x in cumsum]
    for i, txt in enumerate(formatted_weights):
        ax2.annotate(txt, (x[i], cumsum[i]), fontweight='heavy')    
    
    if title:
        plt.title(title)
    
    plt.tight_layout()
    plt.show()


df = pd.DataFrame({
    'Age': [10, 4,3 , 2, 1],
    'Speed': [80,  110,  120,  140,   150]
})
pareto_plot(df, x='Age', y='Speed', title='Car Age - Speed')

#Demonostration of Run Sequence Plot
series = read_csv('daily-min-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
series.plot(style='k.')
pyplot.show()