fullname = input("Enter your fullname: ")
rough = fullname.strip().split()
capital_world = [word.capitalize() for word in rough]
fullname = " ".join(capital_world)
print(fullname)