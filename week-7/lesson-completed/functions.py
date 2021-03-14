def find_the_sum_from_inventory(tax, name):
  lines = []

  f = open(name, "r")
  lines = f.readlines()
  f.close()


  total = 0

  for x in lines[1:]:
      product = x.split(",")

      price = float(product[2])

      total = total+price + (price * tax)

  return total

def find_the_avg_from_inventory(tax, name):
  lines = []

  f = open(name, "r")
  lines = f.readlines()
  f.close()


  total = 0

  for x in lines[1:]:
      product = x.split(",")

      price = float(product[2])

      total = total+price + (price * tax)

  return total / len(lines) - 1
