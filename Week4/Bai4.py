def getInput():
    a = []
    n = int(input("Nhập số phần tử trong mảng: "))
    for i in range(n):
        a.append(input(f"Nhập phần tử thứ {i + 1}: "))
    return a


def countDigit(tup):
    count = 0
    for x in tup:
        if x.isdigit():
            count += 1
    return count


a = getInput()
print("Mảng xâu a vừa nhập là: ", a)
b = tuple(a)
print("Tuple được chuyển từ list: ", b)

print("Số phần tử trong b có dạng số là: " + str(countDigit(b)))
