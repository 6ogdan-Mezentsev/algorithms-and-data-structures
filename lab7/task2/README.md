# Задание №2 по выбору  : `Примитивный калькулятор`
Студент ИТМО, Мезенцев Богдан Геннадьевич | 466683

## Задание
Дан примитивный калькулятор, который может выполнять следующие три операции с текущим числом х: умножить х на 2, умножить на 3 или прибавить 1 к х.
Дано положительное целое число п, найдите минимальное количество операций, необходимых для получения числа п, начиная с числа 1.

## Input / Output 

| Input | Output  |
|-------|---------|
| 5     | 3       | 
|       | 1 3 4 5 |

## Ограничения по времени и памяти

- Ограничение по времени. 1сек.
- Ограничение по памяти. ---.

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
   PYTHONPATH=$(pwd) python3 lab7/task2/src/*.py
   ```

## Запуск тестов для задачи
   ```bash
  python3 -m pytest -v lab7/task2/tests/*.py
   ```