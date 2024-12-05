from itertools import combinations
from collections import defaultdict

transactions = [
    ['milk', 'bread', 'butter'],
    ['milk', 'bread'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['milk', 'bread', 'eggs'],
    ['butter', 'eggs']
]

def generate_new_candidates(frequent_itemsets, k):
    """Generate candidate itemsets of size k from frequent itemsets of size k-1."""
    candidates = set()
    frequent_itemsets_list = list(frequent_itemsets)
    for i in range(len(frequent_itemsets_list)):
        for j in range(i+1, len(frequent_itemsets_list)):
            # Union of two itemsets of size k-1 can create a candidate of size k
            candidate = frequent_itemsets_list[i] | frequent_itemsets_list[j]
            if len(candidate) == k: 
                candidates.add(candidate)
    return candidates

def count_support(transactions, candidates):
    """Count the support of each candidate itemset."""
    support_count = defaultdict(int)
    for transaction in transactions:
        transaction_set = set(transaction)
        for candidate in candidates:
            if candidate.issubset(transaction_set):
                support_count[candidate] += 1
    return support_count

def filter_frequent_itemsets(support_count, min_support, total_transactions):
    """Filter itemsets that meet the minimum support threshold."""
    frequent_itemsets = {}
    for itemset, count in support_count.items():
        support = count / total_transactions
        if support >= min_support:
            frequent_itemsets[itemset] = support
    return frequent_itemsets





def generate_initial_candidates(transactions):
    """Generate the 1-itemsets from transactions."""
    candidates = set()
    for transaction in transactions:
        for item in transaction:
            candidates.add(frozenset([item]))  # 1-itemset
    return candidates


def apriori(transactions, min_support):
    """Apriori algorithm to find frequent itemsets."""
    transactions = [set(transaction) for transaction in transactions]
    total_transactions = len(transactions)

    # 1-itemsets
    current_itemsets = generate_initial_candidates(transactions)
    frequent_itemsets = {}
    
    k = 1
    while current_itemsets:
        #  support counting for current candidates
        support_count = count_support(transactions, current_itemsets)
        
        #filtering itemsets by minimum support
        frequent_k_itemsets = filter_frequent_itemsets(support_count, min_support, total_transactions)
        
        if not frequent_k_itemsets:
            break
        
        # saving frequent itemsets
        frequent_itemsets.update(frequent_k_itemsets)
        
        # generating new candidates for the next level (k+1)
        current_itemsets = generate_new_candidates(frequent_k_itemsets.keys(), k + 1)
        k += 1
    
    return frequent_itemsets






min_support = 0.5

frequent_itemsets = apriori(transactions, min_support)

for itemset, support in frequent_itemsets.items():
    print(f"Frequent Itemset: {set(itemset)}, Support: {support:.2f}")



