import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

np.random.seed(0)
data=np.random.randn(100,2)

kmeans=KMeans(n_clusters=3)
kmeans.fit(data)
centroids=kmeans.cluster_centers_
labels=kmeans.labels_

plt.scatter(data[:,0],data[:,1],c=labels)
plt.scatter(centroids[:,0],centroids[:,1],c='red')
plt.show()