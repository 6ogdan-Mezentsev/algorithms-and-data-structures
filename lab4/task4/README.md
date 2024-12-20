# Задание №6 по выбору  : `Очередь с минимумом`
Студент ИТМО, Мезенцев Богдан Геннадьевич | 466683

## Задание
Реализуйте работу очереди. В дополнение к стандартным операциям очереди, необходимо также отвечать на запрос о минимальном элементе из тех, которые сейчас находится в очереди. Для каждой операции запроса минимального элемента выведите ее результат.
На вход программе подаются строки, содержащие команды. Каждая строка содержит одну команду. Команда - это либо «+ N», либо «-», либо «?». Команда «+ N» означает добавление в очередь числа N, по модулю не превышающего 10^9.
Команда «-» означает изъятие элемента из очереди. Команда «?» означает запрос на поиск минимального элемента в очереди.

## Input / Output 

| Input | Output |
|-------|--------|
| 7     | 1      |
| +1    | 1      |
| ?     | 10     |
| +10   |
| ?     |
| -     |
| ?     |
| -     |

## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/repository-name.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd repository-name/lab4
   ```
3. Запустите программу:
   ```bash
   python3 task4/src/*.py
   ```

## Запуск тестов для задачи
   ```bash
  python3 -m pytest -v lab4/task4/tests/*.py
   ```
