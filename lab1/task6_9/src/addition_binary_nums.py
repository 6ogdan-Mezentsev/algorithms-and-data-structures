import random
from lab1.utils import read_file
from lab1.utils import write_result
from lab1.utils import write_except

file_input_path = '../txtf/input.txt'
file_output_path = '../txtf/output.txt'


def binary_addition(S):
    summa = 0
    if any(len(i) > 10**3 for i in S):
        if any(len(i) < 1 for i in S):
            print("Количество бит не должно превышать значения 10**3")
    else:
        for i in S:
            m = int(i, 2)
            summa += m
    return summa


if __name__ == "__main__":
    n, S = read_file(file_input_path)
    result = bin(binary_addition(S))[2:]
    if any(len(i) > 10 ** 3 for i in S) and any(len(i) < 1 for i in S):
        write_except(file_output_path)
    else:
        write_result(file_output_path, result)
