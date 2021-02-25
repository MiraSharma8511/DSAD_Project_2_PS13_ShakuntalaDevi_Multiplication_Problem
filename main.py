from math import ceil, floor

in_file = 'inputPS13.txt'
out_file = 'outputPS13.txt'


def read_input_file():
    input_file = open(in_file, "r")  # Open input_file to read the file data.
    i = 0
    number_array = ["", ""]  # Take an array to store the two input numbers from file.
    for line in input_file:
        number_data = line.split(":")  # Identify input numbers from input text format.
        # print(number_data)
        number_array[i] = number_data[1].strip()
        i += 1

    input_file.close()  # Close the input file and free the file resource.

    number1 = number_array[0]
    number2 = number_array[1]
    output_file = open(out_file, "w")  # Open out_file to write the output data.
    shakuntala_mul_method(int(number1), int(number2), output_file)
    output_file.close()  # Close the out file and free the file resource.


def shakuntala_mul_method(number1, number2, output_file):
    # If number is just one digit then no need to split, simple multiply and return result.
    if number1 < 10 or number2 < 10:
        return number1 * number2
    # If numbers are more than 2 digit then here below splitting process starts.

    # Find a max of size of number1 and number2 for splitting purpose.
    size = max(len(str(number1)), len(str(number2)))

    # Split number1 and number2 and find a,b,c,d for calculations in recursion.
    n = ceil(size // 2)
    p = 10 ** n
    a = floor(number1 // p)
    b = number1 % p
    c = floor(number2 // p)
    d = number2 % p

    output_file.write("----------------------------\n")  # Adding iterations and output details in opened output file.  
    output_file.write("1st number, x : %s\n" % number1)
    output_file.write("2nd Number, y : %s\n" % number2)
    output_file.write("Intermediate Values of A, B after partition:\n")
    output_file.write("x: " + str(number1) + " a: " + str(a) + " b : " + str(b) + "\n")
    output_file.write("y: " + str(number2) + " c: " + str(c) + " d : " + str(d) + "\n")

    # Perform Recursion until we get one digit number to enter above if condition.
    ac = shakuntala_mul_method(a, c, output_file)
    bd = shakuntala_mul_method(b, d, output_file)
    e = shakuntala_mul_method(a + b, c + d, output_file) - ac - bd
    # e = a * d + b * c
    i = (10 ** (2 * n) * ac + (10 ** n) * e + bd)
    output_file.write("Intermediate Product: " + str(number1) + " x " + str(number2) + " = " + str(
        int(number1) * int(number2)) + "\n")
    output_file.write("---------------------------\n")

    # Now return multiplication result
    return i


read_input_file()
