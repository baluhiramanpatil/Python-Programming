# zip function

l1 = [1, 3, 5]
l2 = [2, 4, 6]

# zip

for a, b in zip(l1, l2):
    print(a, b)

# alternate method 
l = len(l1)

for i in range(l):
    print(l1[i], l2[i]) 