from lab6.utils import write_result, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def hash_table(N, X, A, B, AC, BC, AD, BD):
    """Составляет хеш-таблицу и возвращает значения X, A, B"""
    htable = set()

    for i in range(N):
        # Если X содержится в таблице, то выполняем соответствующую операцию
        if X in htable:
            A = (A + AC) % 1000
            B = (B + BC) % (10 ** 15)
        else:
            # Если X не содержится в таблице, добавляем его
            htable.add(X)
            A = (A + AD) % 1000
            B = (B + BD) % (10 ** 15)

        X = (X * A + B) % (10 ** 15)

    return X, A, B


if __name__ == "__main__":
    with open(FILE_INPUT_PATH, 'r') as file:
        N, X, A, B = map(int, file.readline().split())
        AC, BC, AD, BD = map(int, file.readline().split())

    X, A, B = hash_table(N, X, A, B, AC, BC, AD, BD)
    write_result(FILE_OUTPUT_PATH, [f"{X} {A} {B}"])

    print("---Lab6 Task5---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)