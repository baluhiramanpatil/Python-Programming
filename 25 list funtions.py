# list funtions

'''
del
pop()
remove()
clear()
update element
insert()
append()
extend()
count()
max()
min()
sort()
reverse()
index()
'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
len(l)

# del

del l[10]
print(l)

# pop

l.pop(4)
print(l)

# remove - use for remove element

l.remove(8)
print(l)

# clear

l.clear()
print(l)

# update list element

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
len(l)

l[9] = 10
print(l)

# insert()

l.insert(10, 11)
print(l)

# append()

l.append(12)
print(l)

# extend()

l1 = [13, 14, 15]

l.extend(l1)
print(l)

# count()

l3 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]

e = l3.count(5)
print(e)

# max()

m = max(l3)
print(m)

print(max(l3))

w = ['hello', 'world']

print(max(w))

# min()

l4 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]

n = min(l4)
print(n)

print(min(l4))

w = ['hello', 'world']

print(min(w))

# sort()

l5 = [6, 3, 1, 2, 4, 5]

l5.sort()
print(l5)

# reverse()

l5.reverse()
print(l5)

# index()

l5.index(6) 