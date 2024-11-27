# Лабораторная работа №3: Быстрая сортировка, сортировки за линейное время.

## Описание
В ходе данной лабораторной работе студенты познакомятся с алгоритмом быстрой сортировки "Quick Sort".

## Навигация
[Задача 1 - Улучшение Quick sort](task1/README.md)\
[Задача 2 - Анти-quick sort](task2/README.md)\
[Задача 3 - Сортировка пугалом](task3/README.md)\
[Задача 5 - Индекс Хирша](task4/README.md)\
[Задача 6 - Сортировка целых чисел](task5/README.md)\
[Задача 8 - K ближайших точек к началу координат](task6/README.md)

## Запуск проекта и тестирование
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/username/repository-name.git
2. Запуск всех src из lab3:
    ```bash
    PYTHONPATH=. find lab3/task*/src/ -name "*.py" -exec python3 {} \;
3. Запуск всех тестов для алгоритмов:
    ```bash
    python3 -m pytest -v lab3/task*/tests/*.py
