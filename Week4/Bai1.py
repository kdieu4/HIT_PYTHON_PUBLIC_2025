def tupleInput():
    a = []
    n = int(input("Nhập số phần tử trong mảng: "))
    for i in range(n):
        a.append(input(f"Nhập phần tử thứ {i + 1}: "))
    return tuple(a)


tup_str = tupleInput()
print("Tuple ban đầu: ", tup_str)
tup_int = tuple(map(int, tup_str))
print("Tuple sau khi chuyển đổi thành số: ", tup_int)
print("Trung bình cộng các phẩn tử: ", sum(tup_int) / len(tup_int))
