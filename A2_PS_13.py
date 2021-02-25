in_file = 'inputPS13.txt'
out_file = 'outputPS13.txt'
prompt_file = 'promptsPS18.txt'


def printName():
    return "hello"

    # def read_input_file(self):
    #     input_file = open(in_file, "r")  # Open input_file to read the file data.
    #     count = 0
    #     for line in input_file:
    #         student_data_list = line.split(
    #             "/")  # Read line to split record with '/' to get student_id & CGPA separate.
    #         count += 1
    #         self.studentMap.insert_student_rec(
    #             student_data_list[0].strip(),
    #             student_data_list[1].strip())  # Insert record in the hash table.
    #         input_file.close()  # Close the input file and free the file resource.
    #
    #         output_file = open(out_file, "w")  # Open out_file to write the output data.
    #         output_file.write("Record added successfully %d.\n" % count)
    #         output_file.close()  # Close out_file after intimating the successful insertion of records


class ShakuntaladeviReport:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def student_info(self):
        return (self.a + " / " + self.b) + "\n"


shakuntaladeviReport = ShakuntaladeviReport()  # Initiate the University Report Class.
# shakuntaladevi.read_input_file()  # Read input file
# shakuntaladevi.read_prompts_file()  # Read prompt file
# shakuntaladevi.destroy_hash()  # Destroy the hash map and release the resource.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     # print_number(223245, 123456)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# f_length = int(len(number1))
# s_length = len(number2)
# if f_length % 2 == 0:
#     a = int(f_length / 2)
# else:
#     a = int(f_length / 2) + 1
# if f_length % 2 == 0:
#     b = int(f_length / 2)
# else:
#     b = int(f_length / 2) + 1
# # b = int(f_length // 2)
# if s_length % 2 == 0:
#     c = int(s_length / 2)
# else:
#     c = int(s_length / 2) + 1
# if s_length % 2 == 0:
#     d = int(s_length / 2)
# else:
#     d = int(s_length / 2) + 1
# # c = int(s_length // 2)
# # d = int(s_length // 2)
# intermediate_a1 = number1[0:a]
# intermediate_a2 = number1[b:f_length]
# intermediate_b1 = number2[0:c]
# intermediate_b2 = number2[d:s_length]
#
# output_file = open(out_file, "a")  # Open output file to append the eligible students.
# output_file.write("1st number, x : %s\n" % number1)
# output_file.write("2nd Number, y : %s\n" % number2)
# output_file.write("Intermediate Values of A, B after partition:\n")
# output_file.write("x: " + number1 + " a: " + intermediate_a1 + " b : " + intermediate_a2 + "\n")
# output_file.write("y: " + number2 + " c: " + intermediate_b1 + " d : " + intermediate_b2 + "\n")
# output_file.write("---------------------------\n")
# output_file.close()
# if f_length > 2:
#     first_iteration(intermediate_a1, intermediate_b1)
# else:
#     output_file = open(out_file, "a")  # Open output file to append the eligible students.
#     output_file.write(
#         "Intermediate Product: " + number1 + " x " + number2 + " = " + str(int(number1) * int(number2)) + "\n")
#     output_file.write("---------------------------\n")
#     output_file.close()
# # Close output file.


# def first_iteration(number1, number2):
#     if number1 < 10 and number2 < 10:
#         return number1 * number2
#
#     size = max(len(str(number1)), len(str(number2)))
#
#     # Splitting process of number1 and number 2.
#     n = ceil(size // 2)
#     p = 10 ** n
#     a = floor(number1 // p)
#     b = number1 % p
#     c = floor(number2 // p)
#     d = number2 % p
#
#     # Apply Recursion unless the base case is achieved.
#     ac = karatsuba(a, c)
#     bd = karatsuba(b, d)
#     e = karatsuba(a + b, c + d) - ac - bd
#     # Getting product values as per algorithm.
#     i = (10 ** (2 * n) * ac + (10 ** n) * e + bd)
#     print(i)
#


# output_file = open(out_file, "w")  # Open out_file to write the output data.
# output_file.write("---------------------------\n")
# output_file.write("1st number, x : %s\n" % number1)
# output_file.write("2nd Number, y : %s\n" % number2)
#
# # print(f'First number is: {number1}')
# # print(f'Second number is: {number2}')
# output_file.close()
