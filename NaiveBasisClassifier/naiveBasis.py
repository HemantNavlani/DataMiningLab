import pandas as pd
import numpy as np

df = pd.read_csv("Data.csv")

df.head()

newDF = df.drop(df.columns[0], axis=1)
mat = newDF.to_numpy()
print(mat)

R = mat.shape[0]-1 
C = mat.shape[1]

countYes=0
for i in range(R):
    if mat[i][C-1] == "Yes":
        countYes+=1
countNo=R-countYes
P = countYes/R ## P for P(E=Yes)
NP = countNo/R ## NP for P(E=No)

Pyes=1
Pno=1
for c in range(C-1):
    instanceVal=mat[R][c]
    countInstanceYes=0
    countInstanceNo=0
    for r in range(R):
        if mat[r][c]==instanceVal:
            if mat[r][C-1]=="Yes":
                countInstanceYes+=1
            else:
                countInstanceNo+=1
    Pyes=Pyes*(countInstanceYes/countYes)
    Pno=Pno*(countInstanceNo/countNo)
Pyes=Pyes*P
Pno=Pno*NP
print(f"Yes = {Pyes}")
print(f"No = {Pno}")

if Pyes>Pno:
    df.iloc[R, C] = "Yes"
else:
    df.iloc[R, C] = "No"

df.tail()

df.to_csv("Results.csv", index=False)

predictionDF=pd.read_csv("Results.csv")
predictionDF.tail()