# pip install pyfpgrowth

import pyfpgrowth
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

store_data = pd.read_csv('store_data.csv')

store_data.head()

store_data = pd.read_csv('store_data.csv', header=None)
store_data.head()

records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])

patterns = pyfpgrowth.find_frequent_patterns(transactions, 10)

rules = pyfpgrowth.generate_association_rules(patterns, 0.8)

association_results = list(rules)

print(len(association_results))
      

print(association_results)
