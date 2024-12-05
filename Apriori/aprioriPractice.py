# from collections import defaultdict

# def apriori(transactions,minSupport):
#     transactions = [set(transaction) for transaction in transactions]
#     total = len(transactions)

#     k = 1
#     current = generateInitial(transactions)
#     freqItems = {}
#     while current : 
#         supportCnt = cntSupport(transactions,current)

#         freqK = filterFreq(supportCnt,minSupport,total)

#         if not freqK : break

#         freqItems.update(freqK)
#         current = generateNew(freqK.keys(),k+1)
#         k+=1
#     return freqItems


# def generateInitial(transactions):
#     candidates = set()
#     for transaction in transactions:
#         for item in transaction:
#             candidates.add(frozenset([item]))
#     return candidates


# def cntSupport(transactions,current): 
#     supportCnt = defaultdict(int)

#     for transaction in transactions:
#         transactionSet = set(transaction)
#         for candidate in current:
#             if (candidate.issubset(transactionSet)):


from collections import defaultdict

def apriori(transactions,minSupport):
    transanctions = [set(transaction) for transaction in transactions]
    total = len(transanctions)
    print(total)
    k = 1 
    freq = {}
    current = generateInitial(transactions)
    while current: 
        supportCnt = countSupport(transactions,current)
        freqK = filterFreq(supportCnt,minSupport,total)
        if not freqK : 
            break
        freq.update(freqK)
        current = generateNew(freqK.keys(),k+1)
        k+=1
    return freq    

transactions =     [
    ['milk', 'bread', 'butter'],
    ['milk', 'bread'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['milk', 'bread', 'eggs'],
    ['butter', 'eggs']
]
minSupport = 0.5
def generateInitial(transactions): 
    candidates = set()
    for transaction in transactions : 
        for item in transaction :
            candidates.add(frozenset([item]))
    return candidates

def countSupport(transactions,items):
    supportCnt = defaultdict(int)
    for transaction in transactions : 
        transactionSet = set(transaction)
        for candidate in items : 
            if (candidate.issubset(transaction)) : 
                supportCnt[candidate]+=1
    return supportCnt

def filterFreq(supportCnt,minSupport,total):
    freq = {}
    for item, cnt in supportCnt.items():
        support = cnt/total
        if support>=minSupport: 
            freq[item] = support
    return freq

def generateNew(freq,k):
    candidates = set()
    freqList = list(freq)
    for i in range(len(freqList)):
        for j in range(i+1,len(freqList)):
            candidate = freqList[i] | freqList[j] 
            if (len(candidate)==k) : candidates.add(candidate)
    return candidates

freq = apriori(transactions,minSupport)

for item,supp in freq.items() : 
    print(f"Freq Item : {set(item)}, supp : {supp:.2f}")

print(len(freq))