import numpy as np
import pandas as pd

# Sample data in a DataFrame
data = [
    ['Rainy', 'Hot', 'High', 'f', 'no'],
    ['Rainy', 'Hot', 'High', 't', 'no'],
    ['Overcast', 'Hot', 'High', 'f', 'yes'],
    ['Sunny', 'Mild', 'High', 'f', 'yes'],
    ['Sunny', 'Cool', 'Normal', 'f', 'yes'],
    ['Sunny', 'Cool', 'Normal', 't', 'no'],
    ['Overcast', 'Cool', 'Normal', 't', 'yes'],
    ['Rainy', 'Mild', 'High', 'f', 'no'],
    ['Rainy', 'Cool', 'Normal', 'f', 'yes'],
    ['Sunny', 'Mild', 'Normal', 'f', 'yes'],
    ['Rainy', 'Mild', 'Normal', 't', 'yes'],
    ['Overcast', 'Mild', 'High', 't', 'yes'],
    ['Overcast', 'Hot', 'Normal', 'f', 'yes'],
    ['Sunny', 'Mild', 'High', 't', 'no']
]
columns = ['Outlook', 'Temperature', 'Humidity', 'Windy', 'Play']
df = pd.DataFrame(data, columns=columns)

# Entropy calculation
def entropy(y):
    counts = y.value_counts(normalize=True)
    return -sum(counts * np.log2(counts))

# Split data by feature and value
def split_data(X, feature, value):
    left = X[X[feature] == value]
    right = X[X[feature] != value]
    return left, right

# Information Gain calculation
def information_gain(X, feature, target='Play'):
    total_entropy = entropy(X[target])
    values = X[feature].unique()
    weighted_entropy = sum(
        (len(split) / len(X)) * entropy(split[target]) for val in values
        if (split := X[X[feature] == val]).shape[0] > 0
    )
    return total_entropy - weighted_entropy

# Build the tree
def build_tree(X, target='Play', depth=0, max_depth=3):
    if depth == max_depth or len(X[target].unique()) == 1:
        return X[target].mode()[0]

    gains = {feature: information_gain(X, feature, target) for feature in X.columns if feature != target}
    best_feature = max(gains, key=gains.get)
    
    if gains[best_feature] == 0:
        return X[target].mode()[0]

    tree = {best_feature: {}}
    for value in X[best_feature].unique():
        subset = X[X[best_feature] == value]
        tree[best_feature][value] = build_tree(subset, target, depth + 1, max_depth)

    return tree

# Prediction
def predict(tree, sample):
    for feature, branches in tree.items():
        value = sample[feature]
        subtree = branches.get(value, None)
        if isinstance(subtree, dict):
            return predict(subtree, sample)
        else:
            return subtree

# Build and test
tree = build_tree(df)
print("Decision Tree:", tree)

x_test = {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Windy': 'f'}
print("Prediction for test example:", predict(tree, x_test))
