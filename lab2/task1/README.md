# 1 задача. Сортировка слиянием
## Описание
Используя псевдокод процедур Merge и Merge-sort из презентации к Лекции 2 (страницы 6-7), напишите программу сортировки слиянием на Python и проверьте сортировку, создав несколько рандомных массивов, подходящих под параметры:

• Формат входного файла (input.txt).\
В первой строке входного файла содержится число п (1 ≤ n < 2 * 10^4) - число элементов в массиве.
Во второй строке находятся п различных целых чисел, по модулю не превосходящих 10^9.

• Формат выходного файла (output.txt).\
Одна строка выходного файла с отсортированным массивом. Между любыми двумя числами должен стоять ровно один пробел.

• Ограничение по времени. 2сек.\
• Ограничение по памяти. 256 мб.

## Запуск тестов для задачи:

```bash
python3 -m pytest -v lab2/task1/tests/*.py