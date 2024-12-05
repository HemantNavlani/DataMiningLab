import pandas as pd
import numpy as np

df = pd.read_csv('abalone.csv')
data = df.drop(df.columns[0],axis=1).to_numpy()

def kmeans(data,k,maxIt=100):
    np.random.seed(42)
    nSamples,nFeatures = data.shape
    centroids = data[np.random.choice(nSamples,k,replace=False)]

    for _ in range(maxIt):
        distances = np.linalg.norm(data[:,np.newaxis]-centroids,axis=2)

        labels = np.argmin(distances,axis=1)

        newCentroids = np.array([data[labels==i].mean(axis=0) for i in range(k)])
        if np.all(centroids==newCentroids):break
        centroids = newCentroids
    return labels,centroids

k = int(input())
labels,centroids = kmeans(data,k)

print(f"Cluster centers: {centroids}")
for i in range(k):
    print(f"Cluster{i+1}:{np.where(labels==i)[0]}")