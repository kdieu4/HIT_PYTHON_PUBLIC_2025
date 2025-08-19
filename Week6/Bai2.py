n, m = map(int, input("Nhập số hàng và số cột: ").split())

print("Nhập ma trận: ")
matrix = [list(map(int, input().split())) for _ in range(n)]

transpose = list(map(lambda *rows: list(rows), *matrix))

print("Ma trận chuyển vị: ")
for row in transpose:
    print(*row)

print("Ma trận ban đầu: ")
for row in matrix:
    print(*row)
