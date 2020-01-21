k = 'kousha.text'
with open(k, 'r') as infile:
    words = infile.read().split()
max_word = max(words, key=len)
max_len = len(max(words, key=len))
print(max_word,max_len)