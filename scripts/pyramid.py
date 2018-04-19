def get_pyramid_matrix(size):
    result_matrix = []
    for row in range(1, size + 1):
        result_matrix.append([])
        for item in range(1, row):
            result_matrix[row - 1].append(item)
        result_matrix[row - 1].append(row)
        for item in reversed(range(1, row)):
            result_matrix[row - 1].append(item)

    return result_matrix


# Getting the values for the pyramid
pyramid_data = get_pyramid_matrix(8)

# Getting the length of the base
pyramid_base = (len(pyramid_data[-1]) * 2) - 1


# Printing the pyramid in target format
for row in pyramid_data:
    row_base = len(row) * 2 - 1
    row_padding = (pyramid_base - row_base) // 2
    print(' ' * row_padding, end='')
    for number in row:
        print(number, end=' ')
    print(' ' * (row_padding - 1))

for row in reversed(pyramid_data):
    row_base = len(row) * 2 - 1
    row_padding = (pyramid_base - row_base) // 2
    print(' ' * row_padding, end='')
    for number in row[:len(row) // 2 + 1]:
        print(number, end=' ')
    print(' ' * (row_padding - 1))
