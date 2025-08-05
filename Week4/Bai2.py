set1 = {"SV028315", "SV103729", "SV215948", "SV329107", "SV402836", "SV514290",
        "SV628473", "SV730912", "SV842067", "SV957120"}
set2 = {"SV028289", "SV103489", "SV211948", "SV329607", "SV252836", "SV589290",
        "SV628473", "SV730912", "SV842067", "SV957120"}
print("Danh sách sinh viên đăng ký tại bàn 1: ")
print(", ".join(set1))
print("Danh sách sinh viên đăng ký tại bàn 2: ")
print(", ".join(set2))
common = set1.intersection(set2)
if common:
    print("Danh sách sinh viên đăng ký tại cả hai bàn: ")
    print(", ".join(common))
else:
    print("Không có sinh viên nào đăng ký cả hai bàn.")

print("Danh sách sinh viên đăng ký tại bàn 1 mà không đặng ký tại bàn 2: ")
print(", ".join(set1.difference(set2)))
