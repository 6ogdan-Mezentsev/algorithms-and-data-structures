# Практика по Алгоритмам и Cтруктурам Данных ИТМО
### Студент ИТМО Мезенцев Богдан Геннадьевич

## Цели и задачи
- Изучить основные команды Git
- Изучить различные алгоритмы сортировки
- Изучить процесс написания модульных тестов для алгоритмов

### Технологии
- **Python** - это язык программирования, который является технологией, на основе которой строятся различные инструменты и решения.
- **Git** - это система контроля версий, которая тоже является технологией. Она обеспечивает концепцию управления версиями и потоками разработки.

### Инструменты
- **UnitTest** - встроенный в Python модуль для написания юнит-тестов
- **Time** - библиотека, которая предоставляет функции для работы с временем
- **Psutil** - библеотка, которая используется для мониторинга и управления ресурсами операционной системы.
- **Markdown** - язык разметки для оформления документаций
- **GitHub** – это платформа, использующая технологию Git для хостинга и управления репозиториями.

## Инструкция по запуску

### Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/repository-name.git
2. Запуск всех src из labN:\
Скопируйте и введите в терминал данную команду:\
**(перед этим проверьте, что вы находитесь в корневой папке репозитория)**\
**N - номер лабораторной работы**
    ```bash
    find labN/task*/src/ -name "*.py" -exec python3 {} \;

### Запуск всех тестов
Скопируйте и введите в терминал данную команду:\
**(перед этим проверьте, что вы находитесь в корневой папке репозитория)**
   ```bash
   python3 -m pytest -v lab*/task*/tests/*.py