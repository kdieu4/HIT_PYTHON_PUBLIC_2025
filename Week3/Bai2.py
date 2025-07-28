def build_matrix(lst, rows, cols):
    if rows * cols > len(lst):
        print("NO")
        return
    matrix = []
    print("Matrix: ")
    for i in range(rows):
        row = lst[i * cols:(i + 1) * cols]
        matrix.append(row)
    for row in matrix:
        print(row)


k = int(input("Enter the numbers of list: "))
print("Enter the elements of the list: ")
a = [int(input(f"a[{i}] = ")) for i in range(k)]

n = int(input("Enter the numbers of row: "))
m = int(input("Enter the numbers of column: "))

# list1 = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6]

build_matrix(a, n, m)
