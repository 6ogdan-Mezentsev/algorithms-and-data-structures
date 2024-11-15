# Задание 1
from lab2.utils import read_file
from lab2.utils import write_result
from lab2.utils import write_except

file_input_path = '../txtf/input.txt'
file_output_path = '../txtf/output.txt'


def merge_sort(A, n):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        merge_sort(left, n)
        merge_sort(right, n)
        # i - индекс в списке left
        # j - индекс в списке right
        # k - индекс в исходном списке A
        i = j = k = 0
        while i < len(left) and j < len(right): # рекурсивно сравниваем элементы отсортированных массивов и добаляем их в исходныый массив А
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while j < len(right): # если в правом массиве остались элементы, а в левом нет
            A[k] = right[j]
            j += 1
            k += 1

        while i < len(left): # если в левом массиве остались элементы, а в правом нет
            A[k] = left[i]
            i += 1
            k += 1

        return A
    else:
        return A


if __name__ == "__main__":
    n, A = read_file(file_input_path)
    result = ' '.join(map(str, merge_sort(A, n)))
    if (1 <= n <= 20000) and all(abs(x) <= 10 ** 9 for x in A):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)











