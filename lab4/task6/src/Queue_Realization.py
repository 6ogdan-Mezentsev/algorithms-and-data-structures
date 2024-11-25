class Node:
    """Класс, описывающий новый узел в связанном списке"""
    def __init__(self, value):
        self.value = value  # Данные, которые содержит узел
        self.next = None  # Указатель на следующий узел. Если узел последний, next = None


class Queue:
    """Класс реализует очередь на основе связанного списка и описывает методы для работы с ней"""
    def __init__(self, max_size):
        self.first = None  # Указатель на начало очереди
        self.last = None  # Указатель на конец очереди
        self.size = 0  # Текущий размер очереди
        self.max_size = max_size  # Максимальная вместимость очереди

    def isEmpty(self):
        """Проверяет, очередь пуста или нет"""
        return self.size == 0

    def isFull(self):
        """Проверка на переполнение"""
        return self.size == self.max_size

    def enQueue(self, value):
        """Добавляет элемент в очередь"""
        if self.isFull():
            return print("Очередь переполнена!")

        new_node = Node(value)  # Создаём новый узел
        if self.last is None: # Если очередь пуста
            self.first = self.last = new_node
        else:
            self.last.next = new_node  # Добавляем новый узел в конец очереди
            self.last = new_node  # Меняем указатель для последнего элемента
        self.size += 1

    def deQueue(self):
        """Удаляет первый элемент очереди"""
        self.first = self.first.next  # Меняем указатель для первого элемента

        if self.first is None:  # Если очередь стала пустой
            self.last = None

        self.size -= 1

    def display_queue(self):
        """Выводит элементы всей очереди"""
        elements = []  # Список для хранения элементов
        current_first = self.first  # Первый элемент очереди

        while current_first:  # Пока есть узлы
            elements.append(current_first.value)
            current_first = current_first.next

        return ", ".join(map(str, elements))


if __name__ == "__main__":
    print("---Lab4 Task6_2---")
    queue = Queue(3)

    queue.enQueue(1)
    print(queue.display_queue())
    queue.enQueue(2)
    print(queue.display_queue())
    queue.enQueue(3)
    print(queue.display_queue())
    queue.deQueue()
    print(queue.display_queue())
    queue.deQueue()
    print(queue.display_queue())




