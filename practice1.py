# -*- coding: utf-8 -*-
"""Practice1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I5KPDRILYf9N9xqkjhFa8OeURYFWMtZB
"""

import pandas as pd
from google.colab import drive 
import matplotlib.pyplot as plt

drive.mount('/content.gdrive/', force_remount = True)

df = pd.read_csv("/content.gdrive/MyDrive/ECON441B_Xialei_Gao/Stock Price.csv")
df.describe()

df.head()

plt.figure(figsize = (30,8))
plt.plot(df['Date'],df['Open'], )
plt.title('Daily Open') 
plt.ylabel('Open')
plt.plot()

# Conclusion 
# The Daily opening price is reaching a new high on 1/12/2023 (the datetime is on inverted order for the graph)