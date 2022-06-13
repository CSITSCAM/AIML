import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('Country clusters.csv')
df.head()

plt.scatter(df['Longitude'], df['Latitude'])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

km = KMeans(n_clusters=3) #" here KMeans(3) is the number of cluster we want to have in our datasets"
km

#fit & predict
y_predicted = km.fit_predict(df[['Longitude','Latitude']])
y_predicted

df['Cluster'] = y_predicted
df.head()

plt.scatter(df['Longitude'], df['Latitude'], c=df['Cluster'], cmap='rainbow')
