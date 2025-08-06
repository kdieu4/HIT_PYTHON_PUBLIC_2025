a = tuple(input().split())
b = set(a)
for x in b:
    if a.count(x) % 5 == 0 and a.count(x) % 10 != 0:
        print(x, end=" ")
