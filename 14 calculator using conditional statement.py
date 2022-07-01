# calculator using conditional statement

print('''
      
      + add
      - subtract
      * multiply
      / division
      
      ''')

num1 = eval(input("Enter the value 1: "))
num2 = eval(input("Enter the value 2: "))

opr = input('Enter the operator (+, -, *, /): ')

if opr == '+':
    print(num1 + num2)

elif opr == '-':
    print(num1 - num2)

elif opr == '*':
    print(num1 * num2)

elif opr == '/':
    print(num1 / num2)

else:
    print("invalid")