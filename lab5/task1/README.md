# Задание №1 по выбору  : `Куча ли?`
Студент ИТМО, Мезенцев Богдан Геннадьевич | 466683

## Задание
Структуру данных «куча», или, более конкретно, «неубывающая пирамида», можно реализовать на основе массива.
Дан массив целых чисел. Определите, является ли он неубывающей пирамидой.

## Input / Output 

| Input     | Output |
|-----------|--------|
| 5         | NO     |
| 1 0 1 2 0 |

## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/repository-name.git
   ```
2. Перейдите в корневую папку проекта:
   ```bash
   cd repository-name
   ```
3. Запустите программу:
   ```bash
   PYTHONPATH=$(pwd) python3 lab5/task1/src/*.py
   ```

## Запуск тестов для задачи
   ```bash
  python3 -m pytest -v lab5/task1/tests/*.py
   ```