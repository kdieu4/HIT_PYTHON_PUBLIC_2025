a = tuple(input().split())

b = set(a)
# 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 3 3 3 4 4 4 4 4
# print(b)
for x in b:
    if a.count(x) % 5 == 0 and a.count(x) % 10 != 0:
        print(x, end=" ")
