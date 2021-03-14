from functions import read_file, write_file, add_sales_tax_to_lines

lines = read_file()

tax = .10
updated_lines = add_sales_tax_to_lines(tax, lines)

write_file(updated_lines)
