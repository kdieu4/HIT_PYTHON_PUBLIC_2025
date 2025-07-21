cost = 28
n = 3
coins = int(input("Nhập số tiền: "))

beerBottle = coins // cost
emptyBottle = beerBottle
total = beerBottle

while emptyBottle >= 3:
    newBottle = emptyBottle // 3
    total = total + newBottle
    emptyBottle = newBottle + emptyBottle % 3

print(f"Số chai bia có thể mua được là: {total}")