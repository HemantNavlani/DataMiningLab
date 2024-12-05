import pandas as pd
import numpy as np
import math
from math import inf

df = pd.read_csv('species.csv')
df.head(5)

inputDF = pd.read_csv('input.csv')
inputDF.head()
matInput = inputDF.to_numpy()

mat = df.to_numpy()
print(mat)

R = mat.shape[0]
C = mat.shape[1]-1 ## Subtracted 1 because the last column is a label
print(f"Number of Rows = {R}")
print(f"Number of Columns = {C}")

labels = {*{}}
for r in range(R):
    labels.add(mat[r][C])
print(labels)

dists = []
for r in range(R):
    dist=0
    for c in range(C):
        dist=dist+(mat[r][c]-matInput[0][c])**2
    dist = math.sqrt(dist)
    dists.append(dist)
print(dists)

k = int(input())

topK = {*{}} ## To store the indices of top k least distance from the matrix
for i in range(k):
    minInd=-1
    minVal=float('inf')
    for j in range(R):
        if j not in topK and dists[j]<minVal:
            minInd=j
            minVal=dists[j]
    if minInd!=-1:
        topK.add(minInd)  ## we added if condition, because if the value of k is greater than R then also no problem happens
print(topK)

### Displaying the Labels of the top k rows

labelCount = {} ## To store the count of top k labels
for r in topK:
    if mat[r][C] not in labelCount:
        labelCount.update({mat[r][C]: 1})
    else:
        labelCount[mat[r][C]]+=1
print(labelCount)



maxLabelCount=max(zip(labelCount.values(),labelCount.keys()))
print(maxLabelCount)
prediction = maxLabelCount[1]
print(f"***Prediction for the Label using k-NN[k={k}] = {prediction}")