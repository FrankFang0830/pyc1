from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.metrics import silhouette_score
warnings.filterwarnings("ignore")
sns.set(style="white", color_codes=True)

dataset = pd.read_csv('College.csv')
x = dataset.loc[:,['Apps','Enroll']]   #searching by index or char
y = dataset.iloc[:-1]          #searching by index(number)
sns.FacetGrid(dataset, hue="Private", height=4).map(plt.scatter, "Apps", "Enroll")
plt.show()

from sklearn import preprocessing
##we need to normalize data into a uniform criteria
scaler = preprocessing.StandardScaler()  #we need to normalize data into a uniform criteria
scaler.fit(x) #first step use fit() to get variance and mean, second step use mean/value to transform
X_scaled_array = scaler.transform(x) #transform into normal distribution
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns) #create a table(matrix) to store it

from sklearn.cluster import KMeans
nclusters =4# this is the k in kmeans
seed = 0
km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_scaled)
y_cluster_kmeans = km.predict(X_scaled)
print("Here is the centroid of k-means")
print(km.cluster_centers_)

print(y_cluster_kmeans)
#set plot  pattern
mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
color = 0
j = 0
for i in y_cluster_kmeans:
    plt.plot([X_scaled_array[j:j + 1, 0]], [X_scaled_array[j:j + 1, 1]], mark[i], markersize=5)
    j +=1
plt.show()


data = dataset.drop(columns=['name','Private'],axis=1)
wcss = []
#elbow method to know the number of clusters
for i in range(2,18):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(data)
    k=kmeans.fit_predict(data)
    sil = silhouette_score(data, k) #Silhouette Coefficient is calculated using the mean intra-cluster distance ( a ) and the mean nearest-cluster distance ( b ) for each sample
    print(" Silhouette analysis for KMeans clustering", i, " on sample data is", sil)
    wcss.append(kmeans.inertia_)          #inertia is calculated as the sum of squared distance for each point to it's closest centroid
plt.plot(range(2, 18), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()





