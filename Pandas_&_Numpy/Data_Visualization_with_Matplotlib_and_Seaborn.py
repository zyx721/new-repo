import matplotlib.pyplot as plt
import pandas as np
import pandas as pd

# a = np.read_excel("chapter_3_assets/8_matplotlib_seaborn/linechart.xlsx")
# print(a)
# from matplotlib import pyplot as plt
# plt.figure(figsize=(10,4))
# plt.plot(a["Quarter"],a["Fridge"],color="blue",label="Fridge")
# plt.plot(a["Quarter"],a["Dishwasher"],color="red",label="Dishwasher")
# plt.plot(a["Quarter"],a["Washing Machine"],color="black",label="Washing Machine")
# plt.title("Product Sales")
# plt.xlabel("quarter")
# plt.ylabel("revenue")
# plt.legend()
# ts = a[["Fridge","Dishwasher","Washing Machine"]].sum()
# plt.pie(ts,labels=ts.index,autopct="%1.1f%%",explode=(0.1,0,0),shadow=True,startangle=140)
#
# a.set_index("Quarter",inplace=True)
# a.plot(kind="bar")
# plt.show()

df_scorc = pd.read_excel("chapter_3_assets/8_matplotlib_seaborn/histograms.xlsx")
# print(df_scorc)
plt.hist(df_scorc["Exam_Score"])
plt.show()

import seaborn as sns
# sns.histplot(df_scorc["Exam_Score"],kde=True)
df = pd.read_excel("chapter_3_assets/8_matplotlib_seaborn/scatter_plot.xlsx")
print(df)
sns.scatterplot(data=df,x="area_square_ft",y="price")
plt.show()