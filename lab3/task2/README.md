# 2 задача. Анти-quick sort
## Описание

Требуется написать программу, генерирующую тест, на котором быстрая сортировка сделает наибольшее число таких сравнений.

Формат входного файла (input.txt):\
В первой строке находится единственное число n (1 ≤ n ≤ 10^6).

Формат выходного файла (output.txt):\
Вывести перестановку чисел от 1 до n, на которой быстрая сортировка выполнит максимальное число сравнений.
Если таких перестановок несколько, вывести любую из них.

• Ограничение по времени. 2 сек.

• Ограничение по памяти. 256 мб.

## Запуск тестов для задачи:

```bash
python3 -m pytest -v lab3/task2/tests/*.py