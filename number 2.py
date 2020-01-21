lines = "kousha.text"
count = 0
with open(lines, 'r') as f:
    for line in f:
        count += 1
print("number of your lines is:", count)