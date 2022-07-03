# list iteration

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

len(l)
lenl = len(l)

# iteration

for i in l:
    print(i)

# using range

for a in range(lenl):
    # print(a)
    print(l[a])

for a in range(lenl):
    print(a, l[a])
    
# reverse iteration

for r in range(lenl-1, -1, -1):
    # print(r)
    print(l[r])