# string to list

user = input('say something : ')

l = user.split()
print(l)

# method 2
l = []

for a in range(1, 4):
    n = input("enter the value: ")
    l.append(int(n))
    
print(l)