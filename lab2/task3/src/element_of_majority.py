# Задача 5
from lab2.utils import read_file
from lab2.utils import write_result
from lab2.utils import write_except

file_input_path = '../txtf/input.txt'
file_output_path = '../txtf/output.txt'


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


