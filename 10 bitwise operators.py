# bitwise operators (&, |, ^)

'''
& (and)
| (or)
^ (XOR)

'''
x = 10
y = 8

print(bin(x))
print(bin(y))
print(bin(x & y))

# & 

print(bin(x & y), x & y) # 1000

# |
print(bin(x | y), x | y) # 1010

# ^
print(bin(x ^ y), x ^ y) # 0010

#   1010
#   1000

# & 1000   8
# | 1010  10
# ^ 0010   2