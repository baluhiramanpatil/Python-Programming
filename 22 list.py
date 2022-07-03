# list

'''
- mutable
- []
- multiple values with csv
- [[]]
- [[], [], {}]
'''
# check data type

l = [10, 20, 30, 40, 50, 'Hello']
print(l, type(l))

# check length of elements

print(len(l))

# list slicing

l[4]

l[4: ]

l[ :4]

l[ : ]

l[0:6]

print(l[3], l[-1])

# reverse slicing

l[-1: :-1] # steps 1
l[-1: :-2] # steps 2

# list slicing using steps / increment

l[0:6:2]