def arrayInput():
    n = int(input())
    a = input().split()
    c = []
    for x in a:
        c.append(int(x))
    return c


arr = arrayInput()
res = []
x = 1
i = 0
while len(res) < len(arr):
    while i < len(arr):
        if x != arr[i]:
            res.append(x)
            i += 1
        x += 1

print(res[len(arr) - 1])
