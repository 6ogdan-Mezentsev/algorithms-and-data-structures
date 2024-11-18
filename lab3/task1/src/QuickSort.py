from lab3.utils import read_file
from lab3.utils import write_result
from lab3.utils import write_except
import random

file_input_path = '../txtf/input.txt'
file_output_path = '../txtf/output.txt'


def Randomized_QuickSort(A, l, r):
    """Рандомизированная быстрая сортировка с трехсторонним разделением"""
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = Partition3(A, l, r)   # m1, m2 - опорные элементы
        Randomized_QuickSort(A, l, m1 - 1)   # сортировка правого подмассива
        Randomized_QuickSort(A, m2 + 1, r)   # сортировка левого подмассива
    return A


def Partition3(A, l, r):
    """Трехстороннее разделение массива"""
    x = A[l]  # индекс опорного элемента
    i = l + 1  # индекс для элементов меньших опорного
    j = r  # индекс для элементов больших опорного
    k = l + 1  # индекс текущего элемента

    while k <= j:
        if A[k] < x:
            A[i], A[k] = A[k], A[i]  # Перемещаем меньший элемент в левую часть
            i += 1
            k += 1
        elif A[k] > x:
            A[j], A[k] = A[k], A[j]  # Перемещаем больший элемент в правую часть
            j -= 1
        else:
            k += 1  # Если элемент равен опорному, просто переходим к следующему

    A[l], A[i - 1] = A[i - 1], A[l]  # Перемещаем опорный элемент на его правильную позицию
    return i - 1, j  # Возвращаем индексы границ частей


if __name__ == "__main__":
    n, A = read_file(file_input_path, 0, 0)
    result = ' '.join(map(str, Randomized_QuickSort(A, 0, len(A)-1)))
    if (1 <= n <= 10**4) and all(abs(x) <= 10**9 for x in A):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)


