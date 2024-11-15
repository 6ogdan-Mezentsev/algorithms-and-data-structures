import random
from lab1.utils import read_file
from lab1.utils import write_result
from lab1.utils import write_except

file_input_path = '../txtf/input.txt'
file_output_path = '../txtf/output.txt'


def sortland(M2, n):
    M = [] # исходный неотсортированный массив
    S = [] # список с индексами жителей

    M = M2
    M2 = sorted(M2)
    minimum = min(M)
    medium = M[n // 2]
    maximum = max(M)
    S = [M2.index(minimum) + 1, M2.index(medium) + 1, M2.index(maximum) + 1]
    return S


if __name__ == "__main__":
    # generate test array and writing it to input.txt
    random_numbers = [random.uniform(0, 1000000) for _ in range(3, 10000)]
    lines = [f'{len(random_numbers)}\n', ' '.join(map(str, random_numbers))]
    file = open('../txtf/input.txt', 'w')
    file.writelines(lines)

    n, M2 = read_file(file_input_path)
    result = ' '.join(map(str, sortland(M2, n)))
    if (3 <= n <= 9999) and (n % 2 != 0) and all(float(m) <= 10**6 for m in M2):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)
