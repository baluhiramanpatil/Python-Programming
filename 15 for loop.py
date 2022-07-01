# for loop

'''
range(n)

start with 0
end with n-1
increment 1

range(N, n)

start with N
end with n-1
increment 1

range(N, n, 2)

start with N
end with n-1
increment 2

'''

for n in range(10):
    print(n)

for n in range(5, 11):
    print(n)

for n in range(5, 11, 2): # step 2
    print(n)

for n in range(6):
    print('Thanks!')

# 2 table with for loop

for n in range(1, 11):
    print('2 * ', n, '=', 2 * n)

# reverse loop

for n in range(10, 0, -1):
    print(n)

for n in range(10, 0, -2):
    print(n)

for n in range(10, -1, -2):
    print(n) 