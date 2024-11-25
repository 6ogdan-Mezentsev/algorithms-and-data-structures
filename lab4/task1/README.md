# Задание №1 по выбору  : `Стек`
Студент ИТМО, Мезенцев Богдан Геннадьевич | 466683

## Задание 
Реализуйте работу стека. Для каждой операции изъятия элемента выведите ее результат.
На вход программе подаются строки, содержащие команды. Каждая строка содержит одну команду. Команда — это либо "+ N", либо "-". Команда "+ N"означает добавление в стек числа N, по модулю не превышающего 10^9. Команда "-"означает изъятие элемента из стека. Гарантируется, что не происходит извлечения из пустого стека. Гарантируется, что размер стека в процессе выполнения команд не превысит 10^6 элементов.

## Input / Output 

| Input | Output |
|-------|--------|
| 6     | 10     |
| +1    | 1234   |
| +10   |
| -     |
| +2    |
| +1234 |
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
   python3 task1/src/*.py
   ```

## Запуск тестов для задачи
   ```bash
  python3 -m pytest -v lab4/task1/tests/*.py
   ```