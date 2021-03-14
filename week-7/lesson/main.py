lines = []

f = open("inventory.csv", "r")
lines = f.readlines()
f.close()


total = 0

for x in lines[1:]:
    product = x.split(",")

    price = float(product[2])

    total = total+price

print(total)