a = input().split()
b = set()
c = []

for i in range(len(a)):
    for j in range(len(a[i])):
        c.append(a[i][j])

ans = []

for x in c:
    if x not in b:
        ans.append(x)
        b.add(x)

print(ans)
