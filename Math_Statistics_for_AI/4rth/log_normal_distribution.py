import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read the CSV file
df = pd.read_csv("income.csv")
print(df)

# Plot with logarithmic x-axis



# Set seaborn plot size
sns.set(rc={'figure.figsize':(11.7, 8.27)})

# Create a bar plot
g = sns.barplot(x='income($)', y='count', data=df)
g.set_xticklabels(g.get_xticklabels(), rotation=45, horizontalalignment='right')
g.set(xscale="log")
plt.show()
