import seaborn as sns
import matplotlib.pyplot as plt

# Create a box plot of example data
data = [
    [12, 15, 18, 21, 23, 24, 26, 28, 30, 32],
    [5, 8, 10, 13, 15, 18, 20, 25, 30, 35]
]

# Create a box plot with labels
sns.boxplot(data=data, notch=True, showmeans=True)
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Box Plot Example')
plt.show()