
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = np.array([
    [1, 2], [1.5, 1.8], [2, 2.5],
    [8, 8], [8.5, 9], [9, 8.5],
    [4, 7], [4.5, 7.5], [5, 8]
])

kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
labels = kmeans.fit_predict(data)

for i in range(3):
    points = data[labels == i]
    plt.scatter(points[:, 0], points[:, 1], label="Cluster " + str(i + 1))

plt.title("SOM Data Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
