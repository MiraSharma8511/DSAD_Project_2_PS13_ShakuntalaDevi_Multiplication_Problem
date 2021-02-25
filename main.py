from math import ceil, floor

in_file = 'inputPS13.txt'
out_file = 'outputPS13.txt'


def print_number(number1, number2):
    print(f'First number is: {number1}')
    print(f'Second number is: {number2}')


def read_input_file():
    input_file = open(in_file, "r")  # Open input_file to read the file data.
    i = 0
    number_array = ["", ""]
    for line in input_file:
        number_data = line.split(":")
        print(number_data)
        number_array[i] = number_data[1].strip()
        i += 1

    input_file.close()  # Close the input file and free the file resource.
    number1 = number_array[0]
    number2 = number_array[1]
    shakuntala_mul_method(int(number1), int(number2))


def shakuntala_mul_method(number1, number2):
    # Base case
    if number1 < 10 and number2 < 10:
        return number1 * number2

    # determine the size of X and Y
    size = max(len(str(number1)), len(str(number2)))

    # Split X and Y
    n = ceil(size // 2)
    p = 10 ** n
    a = floor(number1 // p)
    b = number1 % p
    c = floor(number2 // p)
    d = number2 % p

    # Recur until base case
    ac = shakuntala_mul_method(a, c)
    bd = shakuntala_mul_method(b, d)
    e = shakuntala_mul_method(a + b, c + d) - ac - bd
    i = (10 ** (2 * n) * ac + (10 ** n) * e + bd)
    print(i)
    # return the equation
    return i


read_input_file()
shakuntala_mul_method(221234, 123456)
