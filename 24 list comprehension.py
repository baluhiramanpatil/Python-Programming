# list comprehension

'''
list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
'''
l = []

# for loop

for i in range(1, 101):
    # print(i)
    l.append(i)
    print(l)

# list comprehension

l1 = [c for c in range(1, 101)]
print(l1)

# list comprehension with filter

l2 = [c for c in range(1, 101) if c % 2 == 0] 
print(l2)

# list comprehension using string

s = 'Welcome'

s1 = [w for w in s]
print(s1)
