gross = int(input("Nhập lương nhân viên (VND): "))

if gross >= 15000000:
    tax = 0.3 * gross
elif gross >= 7000000:
    tax = 0.2 * gross
else:
    tax = 0.1 * gross

net = gross - tax

print(f"Thuế: {int(tax)} Thu nhập: {int(net)}")