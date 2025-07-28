def count_x(lst):
    x = int(input("Enter a number X: "))
    ans = lst.count(x)
    if ans != 0:
        print(f"The number {x} appears {ans} times")
    else:
        print(f"There are no numbers {x} in the list!")


def replace(lst):
    if len(lst) >= 7:
        replacement = [8, 5, 4, 0, 1, 3]
        lst[1:7] = replacement
        print(f"The list after replacement is:{lst}")
    else:
        print("The list is too short!")
    return lst


def is_ordered(lst):
    if lst == sorted(lst):
        print("TĂNG")
    elif lst == sorted(lst, reverse=True):
        print("GIẢM")
    else:
        print("NO")


n = int(input("Enter a number: "))
list1 = []
for i in range(n):
    num = int(input(f"Enter the {i + 1} number: "))
    list1.append(num)

count_x(list1)

# Thay thế phần tử từ vị trí 2 -> 7 trong list thành [8, 5, 4, 0, 1, 3].
list2 = replace(list1)

print(f"The maximum value in list is {max(list2)}")
print(f"The minimum value in list is {min(list2)}")

y = int(input("Enter a number y to insert to head of the list: "))
list2.insert(0, y)
print(f"The list after inserting: {list2}")

is_ordered(list2)
