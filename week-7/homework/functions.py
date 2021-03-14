def read_file():
    lines = []

    f = open("inventory.csv", "r")
    lines = f.readlines()
    f.close()

    return lines

def write_file(lines):
    f = open("results.csv", "w")

    for line in lines:
        f.write(line)

    f.close()

def add_sales_tax_to_lines(tax, lines):
    new_lines = []

    for line in lines:
        print("do something with the line")

    return new_lines