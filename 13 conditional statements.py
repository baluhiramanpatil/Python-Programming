# conditional statements

'''
key points:
    
    - if statements (if only work when condition is true)
    - if else statements (else only work when if condition is false)
    - if elif else statements (else only work when if and elif condition is false)
'''

# if

a = int(input('Enter the value: '))  # 10

if a % 2 == 0:
    print(a, '- This is a even number')

# if else

a = int(input('Enter the value: '))  # 5

if a % 2 == 0:
    print(a, '- This is a even number')

else:
    print(a, '- This is a odd number')

# if elif else

marks = eval(input('Enter your marks: '))

if marks >= 60:
    print('First Division')
    
elif marks >= 45:
    print('Second Division')
    
elif marks >= 35:
    print('Pass')
    
else:
    print('Fail')