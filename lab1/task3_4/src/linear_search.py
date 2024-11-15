import random
from lab1.utils import read_file
from lab1.utils import write_result
from lab1.utils import write_except

file_input_path = '../txtf/input.txt'
file_output_path = '../txtf/output.txt'


def linear_search(A, V):
    index = []  # список для подсчета индексов, если элемент встречается несколько раз
    for i in range(0, len(A)):
        if int(A[i]) == V:
            index.append(i + 1)
        else:
            continue
    if len(index) == 0:
        return '-1 --> Число не найдено!'
    else:
        return f'Число V встречается {len(index)} раз/раза; Индексы числа V в последовательности: {', '.join(map(str, index))}'


if __name__ == "__main__":
    V, A = read_file(file_input_path)
    result = linear_search(A, V)
    if (0 <= len(A) <= 10**3) and all(abs(int(m)) <= 10**3 for m in A) and (abs(V) <= 10**3):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)