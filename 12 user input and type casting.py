# user input & type casting

'''
key points:
    
    input()     # ask input from user
    int()       # can handle int value
    float()     # can handle float value
    eval()      # can handle int, float and binary value
    
'''
# user input

a = input('Enter the value: ')
print(a, type(a))

a = input('Enter the value: ')
b = input('Enter the value: ')
print(a+b)

# type casting

a = int(input('Enter the value: '))     # 10
b = int(input('Enter the value: '))     # 20
print(a+b)

a = float(input('Enter the value: '))   # 10.1
b = float(input('Enter the value: '))   # 10.2
print(a+b)

a = eval(input('Enter the value: '))    # 10
b = eval(input('Enter the value: '))    # 10.5
print(a+b)

a = eval(input('Enter the value: '))    # 0b1010
b = eval(input('Enter the value: '))    # 10
print(a+b)