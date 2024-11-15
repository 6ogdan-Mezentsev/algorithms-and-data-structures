from lab3.utils import read_file
from lab3.utils import write_result
from lab3.utils import write_except
from lab3.task1.src.QuickSort import Randomized_QuickSort, Partition3

file_input_path = '../txtf/input.txt'
file_output_path = '../txtf/output.txt'


def sorting_integers(A, B):
    C = []  # массив для перемноженных чисел
    for b in B:
        for a in A:
            C.append(a*b)
    Randomized_QuickSort(C, 0, len(C) - 1)  # используем быструю сортировку для массива C
    return sum(C[i] for i in range(0, len(C), 10))


if __name__ == "__main__":
    n, A = read_file(file_input_path, 0, 0)
    m, B = read_file(file_input_path, 2, 0)
    result = str(sorting_integers(A, B))
    if (1 <= n <= 6000) and (1 <= m <= 6000) and all(0 <= abs(a) <= 40000 for a in A) and all(0 <= abs(b) <= 40000 for b in B):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)
