import numpy as np
import pandas as pd

# Load the dataset
abaloneDF = pd.read_csv("./abalone.csv")
data = abaloneDF.drop(abaloneDF.columns[0], axis=1).to_numpy()

# K-Means Implementation
def kmeans(data, k, max_iters=100):
    # Step 1: Initialize cluster centers randomly
    np.random.seed(42)  # For reproducibility
    n_samples, n_features = data.shape
    centroids = data[np.random.choice(n_samples, k, replace=False)]

    for _ in range(max_iters):
        # Step 2: Assign each point to the nearest cluster center
        distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)  # Compute distances
        labels = np.argmin(distances, axis=1)  # Find closest cluster center

        # Step 3: Calculate new centroids
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])

        # Step 4: Check for convergence
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids

    return labels, centroids

# Input number of clusters
k = int(input("Enter value of K: "))

# Run K-Means
labels, centroids = kmeans(data, k)

# Output results
print(f"Cluster Centers:\n{centroids}")
for i in range(k):
    print(f"Cluster {i+1}: {np.where(labels == i)[0]}")
