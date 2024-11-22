from lab2.utils import read_file, write_result, write_except, print_input, print_output
import os

file_input_path = os.path.abspath("../txtf/input.txt")
file_output_path = os.path.abspath("../txtf/output.txt")


def element_of_majority(A):
    A.sort()
    element = A[len(A) // 2]  # в отсортированном массиве элемент большинства будет стоять по середине!
    count = A.count(element)
    if count > len(A) // 2:
        return 1
    else:
        return 0


if __name__ == "__main__":
    n, A = read_file(file_input_path)
    result = str(element_of_majority(A))
    if 1 <= n <= 10**5 and all(abs(x) <= 10**9 for x in A):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)

    print("---Lab2 Task3---")
    print_input(file_input_path)
    print_output(file_output_path)


