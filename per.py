import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from datetime import datetime
import numpy as np
from pandas import read_csv
from matplotlib import pyplot
from pandas import read_csv
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

'''
df = pd.DataFrame({
    'Age': [10, 4,3 , 2, 1],
    'Speed': [80,  110,  120,  140,   150]
})
pareto_plot(df, x='Age', y='Speed', title='Car Age - Speed')'''

import pandas as pd
import matplotlib.pyplot as plt

# Provided dataset
df = pd.DataFrame({
    'Age': [10, 4, 3, 2, 1],
    'Speed': [80, 110, 120, 140, 150]
})

def pareto_plot(df, x, y, title=None, show_pct_y=False, pct_format='{0:.0%}'):
    # Sort the dataframe by the 'y' column in descending order
    df = df.sort_values(by=y, ascending=False)

    # Calculate cumulative percentage
    df['cumperc'] = df[y].cumsum() / df[y].sum() * 100

    # Create figure and twin axes
    fig, ax = plt.subplots()
    ax2 = ax.twinx()

    # Plot bar chart on primary y-axis
    df.plot(kind='bar', x=x, y=y, ax=ax, color='blue', legend=False)

    # Plot cumulative percentage line on secondary y-axis
    df.plot(kind='line', x=x, y='cumperc', ax=ax2, color='red', marker='o', legend=False)

    # Set labels
    ax.set_ylabel(y)
    ax2.set_ylabel('Cumulative Percentage')
    ax.set_xlabel(x)

    # Format secondary y-axis ticks as percentages
    ax2.yaxis.set_major_formatter(PercentFormatter())

    # Set title
    if title:
        plt.title(title)

    # Show grid
    ax.grid(True)
    ax2.grid(False)

    # Show the plot
    plt.show()

# Plot the Pareto chart
pareto_plot(df, x='Age', y='Speed', title='Pareto Chart of Car Speed by Age')
