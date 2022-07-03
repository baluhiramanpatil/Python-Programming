# string iteration

s = 'Hello world!'

print(len(s))

for i in range(len(s)):
    print(s[i])


for a in range(len(s)):
    print(a, s[a])
    
# reverse

# method 1

r = s[-1: :-1]
l = len(s)
print(l)

for a in range(l):
    print(r[a])

# method 2

print(len(r))

for b in range(len(r)):
    print(r[b])

for c in range(len(r)):
    print(c, r[c])

# method 3

for d in s:
    print(d)
    