import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("revenue.csv")
df.plot(x='company',y='revenue',kind='bar',logy=True)
plt.show()