# 3 задача. Сортировка пугалом
## Описание

«Сортировка пугалом» — это давно забытая народная потешка. Участнику под верхнюю одежду продевают деревянную палку, так что у него оказываются растопырены руки, как у огородного пугала. Перед ним ставятся п матрёшек в ряд. Из-за палки единственное, что он может сделать — это взять в руки две
матрешки на расстоянии друг от друга (то есть і-ую и і + k-ую), развернуться и
поставить их обратно в ряд, таким образом поменяв их местами.
Задача участника - расположить матрёшки по неубыванию размера. Может ли он это сделать?

Формат входного файла (input.txt):\
В первой строчке содержатся числа пик (1 ≤ n, k < 10^5) - число матрёшек и размах рук.\
Во второй строчке содержится п целых чисел, которые по модулю не превосходят 10^9 - размеры матрёшек.

Формат выходного файла (output.txt):\
Выведите «ДА», если возможно отсортировать матрёшки по неубыванию размера, и «НЕТ» в противном случае.

• Ограничение по времени. 2 сек.

• Ограничение по памяти. 256 мб.

## Запуск тестов для задачи:

```bash
python3 -m pytest -v lab3/task3/tests/*.py