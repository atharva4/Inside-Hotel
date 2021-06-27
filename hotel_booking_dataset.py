# -*- coding: utf-8 -*-

#!pip install geopy
#!pip install Nominatim

# import pip
# pip.main(['install','geopy'])

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import geopy
from geopy.geocoders import Nominatim

X= []

dataset=pd.read_csv('cityList.csv',encoding='cp1252')
cities=dataset.iloc[:,-1].values;
#print(cities)

geolocator = Nominatim(user_agent="Your_Name")
for i in cities:
  temp = []
  location = geolocator.geocode(i)
  #print(i,":",location.longitude)
  temp.append(location.latitude)
  temp.append(location.longitude)
  X.append(temp)

k_means_score = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i)
  kmeans.fit(X)
  k_means_score.append(kmeans.inertia_)
plt.plot(range(1,11), k_means_score)
plt.show()

no_of_clusters = 4

kmeans = KMeans(n_clusters=no_of_clusters)
kmeans.fit(X)
print(kmeans.inertia_)
print("")

df = pd.DataFrame(X)

plt.scatter(df[0],df[1])
plt.show()

y_pred = kmeans.predict(X)
print(y_pred)

inertia_list = []
density_list = []

for i in range(no_of_clusters):
  grp = df[y_pred==i]
  km = KMeans(n_clusters=1)
  km.fit(grp)
  inertia_list.append(km.inertia_)
  density_list.append(grp.shape[0] / km.inertia_)
  
print("")
print(inertia_list)
print(density_list)

df_plot = np.array(df)

for i in range(no_of_clusters):
  plt.scatter(df_plot[y_pred==i, 0], df_plot[y_pred==i, 1])

plt.show()

final_list = []

for i in range(no_of_clusters):
  temp = []
  #print(city_state_country(kmeans.cluster_centers_[i]))
  location = geolocator.reverse(kmeans.cluster_centers_[i], exactly_one=True)
  address = location.raw['address']
  print(i,end=" ")
  state = address.get('state', '')
  print(state)
  temp.append(density_list[i])
  temp.append(state)
  final_list.append(temp)

print("")
final_df = pd.DataFrame(final_list)
print(final_df.sort_values(by=[0], ascending=False))