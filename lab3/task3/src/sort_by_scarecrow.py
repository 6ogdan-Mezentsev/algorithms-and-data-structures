from lab3.utils import read_file, write_result, write_except, print_input, print_output
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


def can_sort_by_scarecrow(n, k, sizes_of_matryoshkas):
    # Разбиваем индексы на блоки по модулю k
    blocks = [[] for _ in range(k)]
    for i in range(n):
        blocks[i % k].append(sizes_of_matryoshkas[i])

    # Сортируем каждый блок
    for block in blocks:
        block.sort()

    # Объединяем блоки в один отсортированный массив
    sorted_sizes = []
    for i in range(n):
        sorted_sizes.append(blocks[i % k][i // k])

    # Проверяем, является ли объединённый массив отсортированным
    if sorted_sizes == sorted(sizes_of_matryoshkas):
        return "ДА"
    else:
        return "НЕТ"


if __name__ == "__main__":
    n, k, sizes_of_matryoshkas = read_file(file_input_path, 0, 'task3')
    result = can_sort_by_scarecrow(n, k, sizes_of_matryoshkas)
    if (1 <= n) and (k <= 10**5) and all(abs(x) <= 10**9 for x in sizes_of_matryoshkas):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)

    print("---Lab3 Task3---")
    print_input(file_input_path)
    print_output(file_output_path)
