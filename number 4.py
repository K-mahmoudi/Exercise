from collections import Counter
a = "kousha.text"
with open(a, 'r') as infile:
    words = infile.read().split()
Counter = Counter(words)
most_occur = Counter.most_common()
print(most_occur)