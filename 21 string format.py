# string format

'''
- the format() method formats the specific value(s) and insert them inside the placeholder
- the placeholder is define using {} 

- examples:
    
    - named indexes
    text1 = "Welcome to {first} {last}".format(first = 'python', last = 'program')
    
    - numbered indexes
    text2 = "Welcome to {0} {1}".format('python', 'program')
    
    - empty placeholderes
    text3 = "Welcome to {} {}".format('python', 'program')
    
    - value placeholder
    text4 = "Welcome to {a} {b}".format(a = 'python', b = 'program')
    
    - value placeholder using space
    text5 = "Welcome to {a:10} {b:10}".format(a = 'python', b = 'program')
    
    value placeholder using space alignment
    - left <, right >, center ^, 
    
    text6 = "Welcome to {a:<10} {b:>10} {c:^10}".format(a = 'python', b = 'program', c = 3.9) 
   
    
'''
text1 = "Welcome to {first} {middle}{last}".format(first = 'python', last = 'program')
print(text1)

text2 = "Welcome to {0} {1}".format('python', 'program')
print(text2)

text3 = "Welcome to {} {}".format('python', 'program')
print(text3)

text4 = "Welcome to {a} {b}".format(a = 'python', b = 3.9)
print(text4)

text5 = "Welcome to {a:10} {b:10}".format(a = 123, b = 456)
print(text5)

text6 = "Welcome to {a:<10} {b:>10} {c:^10}".format(a = 'python', b = 'program', c = 3.9)
print(text6)