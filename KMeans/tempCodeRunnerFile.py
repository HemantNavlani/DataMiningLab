import pandas as pd
import numpy as np
import random
import math

abaloneDF = pd.read_csv("./abalone.csv")
abaloneDF.head()

mat = abaloneDF.drop(abaloneDF.columns[0], axis=1).to_numpy()
R = mat.shape[0]
C = mat.shape[1]
print(mat, R, C)

print("Enter value of K : ")
k = int(input())
print(f"Value of k={k}")


def eucDist(a, b):
    dist=0
    for i in range(C):
        dist = dist + (a[i]-b[i])**2
    dist = math.sqrt(dist)
    return dist
    
def squareEucDist(a, b):
    dist=0
    for i in range(C):
        dist = dist + (a[i]-b[i])**2
    return dist

def createClusters(clusterMeans):
    for i in range(k):
        clusters.append({*{}})
    for r in range(R):
        temp = [] ## This is a Dist List for storing dist of a single data point with all the clusterMeans
        for x in range(k):
            temp.append(eucDist(clusterMeans[x], mat[r]))
        minimum = min(temp)
        ind = temp.index(minimum)
        clusters[ind].add(r)
    return clusters
    
def updateClusterMeans(clusters):
    newClusterMeans=[]  ## This is also a list od sets
    for i in range(len(clusters)):
        tempMean=[]
        for x in range(C):
            tempMean.append(1) ## Making len of tempMean equal to number of columns
        for c in range(C):
            for r in clusters[i]:
                tempMean[c]=tempMean[c]+mat[r][c]
            tempMean[c]=tempMean[c]/len(clusters[i])
        newClusterMeans.append(tempMean)
    return newClusterMeans

def calcVariance(clusters, clusterMeans):
    varianceSum=0
    for c in range(k):
        localClusterVariance=0
        localClusterLen=len(clusters[c])
        for dp in clusters[c]: ## dp for Data Point
            localClusterVariance=localClusterVariance+squareEucDist(mat[dp], clusterMeans[c])
        varianceSum=varianceSum+localClusterVariance/localClusterLen
    return varianceSum

def randomClusterMeans():
    st = {*()}
    clusterMeans = []
    clusterMeansRows = []
    x = k
    while x:
        r = random.randrange(0, R-1)
        if not r in st:
            st.add(r)
            clusterMeans.append(mat[r])
            clusterMeansRows.append(r)
            x=x-1
    return [clusterMeans, clusterMeansRows]

iterations = 100 ## This many times we are choosing k random data points
varianceToClusterMeans={} #

for iter in range(iterations): ## choosing random clusterMeans 'iterations' times
    retVal = randomClusterMeans()
    clusterMeans=retVal[0]
    clusterMeansRows=retVal[1]
    clusters=[]
    prevClusters=[]
    while True:
        clusters = createClusters(clusterMeans)
        
        if len(prevClusters)>0 and prevClusters==clusters:
            variance=calcVariance(clusters, clusterMeans)
            varianceToClusterMeans[variance]=clusterMeansRows
            break
        clusterMeans=updateClusterMeans(clusters)
        prevClusters=clusters
        
print(varianceToClusterMeans)

minVariance = min(varianceToClusterMeans.keys())
clusterMeanRows = varianceToClusterMeans[minVariance]
clusterMeans = []
for r in clusterMeanRows:
    clusterMeans.append(mat[r])
    
## Calculate the clusters finally
prevClusters = []
clusters = []
while True:
    clusters=createClusters(clusterMeans)

    if len(prevClusters)>0 and prevClusters==clusters:
        break
        
    prevClusters=clusters
    clusterMeans=updateClusterMeans(clusters)

print(f"Variance for given value of k({k}) = {minVariance}\n")
print(f"Clusters for given value of k({k}) = {clusters}\n")