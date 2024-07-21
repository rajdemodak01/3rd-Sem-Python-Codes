import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate random normal data points
np.random.seed(0)
data_points = np.random.randn(100, 2)  # 100 data points with 2 features

# Perform K-means clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(data_points)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Plot the data points and centroids
plt.scatter(data_points[:, 0], data_points[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1],c='red')
plt.title('K-means Clustering')
plt.show()