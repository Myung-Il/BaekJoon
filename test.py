l = [[0, 123, 32], [100, 3, 352]]

for row in l:
    output_line = ""
    for num in row:output_line += f"{num:>4}"
    print(output_line)