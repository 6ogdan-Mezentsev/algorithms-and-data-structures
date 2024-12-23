from lab7.utils import read_file, write_result, write_except, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def min_coins(money, coins):
    """Находит минимальное количество монет для размена суммы"""
    min_coins = [float('inf')] * (money + 1)  # массив для хранения минимального числа монет для каждой суммы
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, money + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[money] == float('inf'):
        return -1
    else:
        return str(min_coins[money])


if __name__ == "__main__":
    money, coins = read_file(FILE_INPUT_PATH, start_line=0, task='task1')
    if 1 <= money <= 10 ** 3:
        write_result(FILE_OUTPUT_PATH, min_coins(money, coins))
    else:
        write_except(FILE_OUTPUT_PATH)

    print("---Lab7 Task1---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)
