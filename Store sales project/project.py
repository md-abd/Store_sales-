import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori
import pandas as pd

data = pd.read_csv('store_sales.csv', header = None)
buy = []
for i in range(0, 500):
    buy.append([str(data.values[i,j]) for j in range(0, 13)])

 items= apriori(buy, min_support = 0.002, min_confidence = 0.2, min_lift = 3, min_length = 2)

result = list(items)