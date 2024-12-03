from lab5.utils import read_file, write_result, write_except, print_input, print_output
from collections import deque
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def hight_of_tree(n, parents):
    """Вычесляет высоту дерева"""

    children = [[] for _ in range(n)]  # Создаем список детей для каждого узла
    root = None

    for child, parent in enumerate(parents):
        if parent == -1:
            root = child  # Узел без родителя является корневым
        else:
            children[parent].append(child)

    queue = deque([(root, 1)])
    height = 0

    while queue:
        node, level = queue.popleft()
        height = max(height, level)
        for child in children[node]:
            queue.append((child, level + 1))

    return str(height)


if __name__ == "__main__":
    n, parents = read_file(FILE_INPUT_PATH)
    result = hight_of_tree(n, parents)
    write_result(FILE_OUTPUT_PATH, result)

    print("---Lab5 Task2---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)
