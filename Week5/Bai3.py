n = int(input())
a = input().split()
c = []
b = []
for x in a:
    c.append(int(x))

print(c)
# while len(b) < n:
x = 1
i = 0
while x != c[i] and len(b) < n:
    b.append(x)
    x += 1
i += 1

print(b)
