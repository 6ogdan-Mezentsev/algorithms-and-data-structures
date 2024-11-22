from lab3.utils import read_file, write_result, write_except, print_input, print_output
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


def distance_search(n, k, points):
    # Вычисляем расстояние и сохраняем в виде кортежей (расстояние, (x, y))
    distances = [((x ** 2 + y ** 2), (x, y)) for x, y in points]
    # Сортируем по расстоянию
    distances.sort(key=lambda item: item[0])
    # Извлекаем первые K точек
    result_points = [point for _, point in distances[:k]]

    return result_points


if __name__ == "__main__":
    with open(file_input_path, 'r') as f:
        lines = f.readlines()
        n, k = map(int, lines[0].split())
        points = [tuple(map(int, line.split())) for line in lines[1:]]

    result = ' '.join(map(str, distance_search(n, k, points)))

    write_result(file_output_path, result)

    print("---Lab3 Task6---")
    print_input(file_input_path)
    print_output(file_output_path)


