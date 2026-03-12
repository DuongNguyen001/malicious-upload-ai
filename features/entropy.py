import math
from collections import Counter

def calculate_entropy(data):

    if len(data) == 0:
        return 0

    counter = Counter(data)
    entropy = 0

    for count in counter.values():
        p = count / len(data)
        entropy -= p * math.log2(p)

    return entropy
