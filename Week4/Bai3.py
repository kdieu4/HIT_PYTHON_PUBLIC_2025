def getInput():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return arr, a, b


def countHappiness(arr, a, b):
    happiness = 0
    for i in arr:
        if i in a:
            happiness += 1
        elif i in b:
            happiness -= 1
    return happiness


arr, a, b = getInput()
print(countHappiness(arr, a, b))
