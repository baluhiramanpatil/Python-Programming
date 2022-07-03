# string function

'''
lower()
upper()
title()
capitalize()
find()
index()
isalpha()
isdigit()
isalnum()
'''
s = 'Hello World!'

# lower
ls = s.lower()
print(ls)

# upper
us = s.upper()
print(us)

# title
ts = s.title()
print(ts)

# capitalize
cs = s.capitalize()
print(cs)

# find
print(s.find('W'))
print(s.find('World'))
print(s.find('r', 3))       # star find from index 3
print(s.find('z'))          # if not find the given value, it will return -1

# index
print(s.index('W'))
print(s.index('z'))          # if not find the given value, it will return error

# isalpha (if value in alphabets then return True, if not then return False)
a = 'abc123'
print(a.isalpha())

# isgidit  (if value in digit then return True)
a = 'abc123'
print(a.isdigit())

b = '123'
print(b.isdigit())

# isalnum   (if value in alphabet or numeric then return True)
c = '123'
d = 'abc@123'
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(a.isalnum())
print(d.isalnum())
