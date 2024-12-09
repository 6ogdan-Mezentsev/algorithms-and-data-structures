# Лабораторная работа №7: Динамическое программирование

## Описание
В ходе данной лабораторной работе можно познакомится с динамическим программированием. 

## Навигация
[Задача 1 - Обмен монет](task1/README.md)\
[Задача 2 - Примитивный калькулятор](task2/README.md)\
[Задача 5 - Редакционное расстояние](task3/README.md)\
[Задача 6 - Шаблоны](task4/README.md)\

## Запуск проекта и тестирование
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/username/repository-name.git
2. Запуск всех src из lab7:
    ```bash
    PYTHONPATH=. find lab7/task*/src/ -name "*.py" -exec python3 {} \;
3. Запуск всех тестов для алгоритмов:
    ```bash
    python3 -m pytest -v lab7/task*/tests/*.py
