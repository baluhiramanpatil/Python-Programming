# data types in python (numeric, sequence, dictionary, set)

''' mutable and immutable data types:
    
    - mutable object can change its state or contents and immutable objects cannot.

mutable data types:
    
    - list 
    - dictionary
    - byte array

immutable data types:
    
    - int
    - float
    - complex
    - string
    - tuple
    - set
    
# numeric (integers, floot, complex numbers)
# sequence (string, list, tuple)
# dictionary
# set

string:
    
    - a string is a collection of one or more characters put in a single quote, double quote or triple quote
    - multi-line strings can be denoted using triple quotes, such as ''' or '''
    
list:
    - list is ordered sequence of items
    - it is one of the most used datatypes in python and is very flexible

tuple:
    
    - tuple is an orderd sequence of items same as a list
    - it is defined within parentheses () where items are separated by commas
    - tuple objects does not support item assignments

dictionary:
    
    - dictionary is an unordered collection of key-value pairs
    - dictionary is defined within braces {} with each item being a pair in the form key: value

set:
    
    - a set is an unordered collection of items
    - every set element is unique (no duplicates) and must be immutable (cannot change)
    - {}
'''
# numeric

a = 5
print(a, type(a))

a = (5)
print(a, type(a))

a = 5.5
print(a, type(a))

a = 2+5j
print(a, type(a))

# string

s = 'hello world'
print(s, type(s))

s = '''
    hello
    world
'''
print(s, type(s))

s = '10'
print(s, type(s))

# list

l = [10, 10.5, 2+5j, 'abc']
print(l, type(l))

l[1] = 11
print(l, type(l))

# tuple

t = (10, 20, 'hello world')
print(t, type(t))

a = (5)  # integer because tuple ask items are separated by commas
print(a, type(a))

a = (5, 10)
print(a, type(a))

# dictionary

d = {'name': 'python', 'hello': 'world', a: 10}
print(d, type(d))

# set

s= {10, 20, 30, 40, 50, 10}
print(s, type(s)) 