import pandas as pd
import numpy as np
import math
from math import inf


df = pd.read_csv('species.csv')
df.head()

inputDf = pd.read_csv('input.csv')
inputDf.head()

matInput = inputDf.to_numpy()
print(matInput)
mat = df.to_numpy()
print(mat)

R = mat.shape[0]
C = mat.shape[1]-1

print(R)
print(C)

labels = {*{}}
for r in range(R):
    labels.add(mat[r][C])
print(labels)

dists = []
for r in range(R):
    dist = 0
    for c in range(C):
        dist=dist+(mat[r][c]-matInput[0][c])**2
    dist = math.sqrt(dist)
    dists.append(dist)
print(dists)

k = int(input())

topK = {*{}}
for i in range(k):
    minInd = -1
    minVal = float('inf')

    for j in range(R):
        if j not in topK and dists[j]<minVal:
            minInd = j
            minVal = dists[j]
    if minInd!=-1:
        topK.add(minInd)
print(topK)

labelCnt = {}
for r in topK:
    if mat[r][C] not in labelCnt:
        labelCnt.update({mat[r][C]:1})
    else : labelCnt[mat[r][C]]+=1
print(labelCnt)

# maxLabelCount=max(zip(labelCnt.values(),labelCnt.keys()))
# print(maxLabelCount)
# prediction = maxLabelCount[1]
# print(f"***Prediction for the Label using k-NN[k={k}] = {prediction}")