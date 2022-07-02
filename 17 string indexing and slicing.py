# string indexing and slicing

'''
- a string is a sequence of characters
- strings can be created by enclosing characters inside a single-quote or double-quotes
- triple quotes can be used to represent multipline strings

'''

s = 'welcome to python'

# lengh of string

print(len(s))

# indexing

print(s[0])
print(s[1])
print(s[7])
print(s[8])
print(s[-1])
print(s[16])

# slicing

print(s[0:17])
print(s[0: ])
print(s[8:17])
print(s[0:7])
print(s[ :17])

# with reverse

print(s[:7:-2])
print(s[-1:0:-2])
print(s[-1:11:-3])
print(s[-2:3:-2])

# with increment

print(s[0:17:2])
print(s[0:7:2])
print(s[8:17:3])
print(s[0:7:2])
print(s[ :17:4])