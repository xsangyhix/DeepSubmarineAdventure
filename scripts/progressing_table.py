import math


def get_digits(integer):
    number_of_digits = -1
    if integer > 0:
        number_of_digits = int(math.log10(integer)) + 1
    elif integer < 0:
        number_of_digits = int(math.log10(integer) * -1) + 1
    elif integer == 0:
        number_of_digits = 1
    return number_of_digits


# Generating the matrix with the numbers
number_matrix = [[i * j for j in range(1, 12)] for i in range(1, 12)]

# print(number_matrix)

# Determining the maximum length of a single digit
max_digit_length = 1
for number in number_matrix[-1]:
    digit_length = get_digits(number)
    if digit_length > max_digit_length:
        max_digit_length = digit_length

for row in number_matrix:
    for number in row:
        for i in range(max_digit_length - get_digits(number)):
            print(' ', end='')
        print(number, end='  ')
    print('')