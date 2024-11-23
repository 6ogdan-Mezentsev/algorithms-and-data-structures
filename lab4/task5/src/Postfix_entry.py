from lab4.utils import read_file, write_result, write_except, print_input, print_output
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


def Postfix_calculate(expression):
    """Вычисляет значение выражения в постфиксной записи."""
    stack = []
    actions = ['+', '-', '*', '/']

    for simbol in expression.split():
        if simbol not in actions:
            stack.append(int(simbol))  # Если символ является числом, то добавляем его в стек
        else:
            b = stack.pop()
            a = stack.pop()

            # Выполняем соответственную операцию
            if simbol == '+':
                stack.append(a + b)
            elif simbol == '-':
                stack.append(a - b)
            elif simbol == '*':
                stack.append(a * b)
            elif simbol == '/':
                stack.append(int(a / b))

    return stack[0]  # Возвращаем значение выражения


if __name__ == "__main__":
    N, expression = read_file(file_input_path)
    expression = expression[0]
    if 1 <= N <= 10 ** 6:
        result = [Postfix_calculate(expression)]
        write_result(file_output_path, result, 0)
    else:
        write_except(file_output_path)

    print("---Lab4 Task5---")
    print_input(file_input_path)
    print_output(file_output_path)