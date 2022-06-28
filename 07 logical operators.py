# logical operators (and, or, not)

'''
and (return true if both statements are true)
or (return true if one of the statements is true)
not (reverse the result, returns the false if the result is true)

'''
x = 10
y = 20

# and

print(x == 10 and x < y)
print(x == 10 and x < y and x == y)

# or

print(x == 10 or x < y and x == y)
print(x == 10 or x < y or x == y)
print(x != 10 or x < y or x == y)

# not

print(not x == 10)
print(not x != 10)
