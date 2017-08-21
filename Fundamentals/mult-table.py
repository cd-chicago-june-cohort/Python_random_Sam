def multiplication_table(size):
    top_row = "x"
    multiple = []
    for num in range(1, size + 1):
        multiple.append(num)
        top_row = top_row + ' ' + str(num)
    print top_row
    for item in multiple:
        row = str(item)
        for num in range(1, size + 1):
            mult = item * num
            row = row + ' ' + str(mult)
        print row

multiplication_table(12)

