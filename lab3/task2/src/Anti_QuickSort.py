from lab3.utils import read_file, write_result, write_except, print_input, print_output

file_input_path = '/Users/6ogdanmezentsev/PycharmProjects/algorithms-and-data-structures/lab3/task2/txtf/input.txt'
file_output_path = '/Users/6ogdanmezentsev/PycharmProjects/algorithms-and-data-structures/lab3/task2/txtf/output.txt'

"""
Худший случай для QuickSort возникает, когда массив
уже отсортирован или отсортирован в обратном порядке,
или когда опорный элемент всегда выбирается так, что
в результате разделения один из подмассивов будет содержать
почти все элементы (а другой — только один или два).
Это происходит, если каждый раз выбирается первый или последний элемент в массиве как опорный.
"""


def genearte_array(n):
    array = list(range(n, 0, -1))  # Массив отсортированный в обратном порядке
    return array


if __name__ == "__main__":
    n = read_file(file_input_path, 0, 0)
    result = ' '.join(map(str, genearte_array(n)))
    if 1 <= n <= 10**6:
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)

    print("---Lab3 Task2---")
    print_input(file_input_path)
    print_output(file_output_path)
