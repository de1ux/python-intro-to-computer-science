from functions import find_the_sum_from_inventory, find_the_avg_from_inventory

tax = float(input("Sales tax? "))
filename = input("Filename? ")
choice = input("Avg or sume? ")

if choice == "sum":
  the_sum = find_the_sum_from_inventory(tax, filename)
  print("The sum is", the_sum)

if choice == "avg":
  the_avg = find_the_avg_from_inventory(tax, filename)
  print("The avg is", the_avg)

