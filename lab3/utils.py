import psutil
import time


def read_file(file_input_path, start_line=0, *args):
    with open(file_input_path, 'r') as file:
        lines = file.readlines()
        if args[0] == 'task3':
            m = [int(num) for num in lines[start_line].strip().split()]
            A = [int(num) for num in lines[start_line + 1].strip().split()]
            return m[0], m[1], A
        elif args[0] == 'task4':
            A = [int(num) for num in lines[start_line].strip().split(',')]
            return A
        elif len(lines) == 1:
            n = int(lines[start_line].strip())
            return n
        else:
            n = int(lines[start_line].strip())
            A = [int(num) for num in lines[start_line + 1].strip().split()]
            return n, A



def write_result(file_output_path, result):
    outfile = open(file_output_path, 'w').write(result)


def write_except(file_output_path):
    outfile = open(file_output_path, 'w').write("Проверьте корректность введённых данных")


def count_time_and_memory(algorithm, *args, **kwargs):
    # Засекаем время начала выполнения
    start_time = time.time()

    # Засекаем память до выполнения
    process = psutil.Process()
    memory_before = process.memory_info().rss / 1024  # В килобайтах

    # Выполняем функцию
    result = algorithm(*args, **kwargs)

    # Засекаем время конца выполнения
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Засекаем память после выполнения
    memory_after = process.memory_info().rss / 1024  # В килобайтах
    memory_used = memory_after - memory_before

    return result, elapsed_time, memory_used

