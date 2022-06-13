#pip install -U scikit-learn
#pip install scikit-learn-extra

import pandas as pd
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids

df = pd.read_csv('Country clusters.csv')
df

plt.scatter(df['Longitude'], df['Latitude'])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

km = KMedoids(3)
km

y_predicted = km.fit_predict(df[['Longitude','Latitude']])
y_predicted

df['KMedoids'] = y_predicted
df.head()

plt.scatter(df['Longitude'], df['Latitude'], c=df['KMedoids'], cmap='rainbow')
