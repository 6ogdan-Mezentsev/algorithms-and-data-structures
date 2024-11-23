class Node:
    """Класс, описывающий новый узел в связанном списке"""
    def __init__(self, value):
        """Инициализация данных узла"""
        self.value = value  # Значение, которое содержит узел
        self.next = None  # Указатель на следующий узел. Если узел последний, next = None


class Stack:
    """Класс реализует стек на основе связанного списка и описывает методы для работы с ним"""
    def __init__(self):
        """Инициализация верхнего элемента стека"""
        self.top = None  # Указатель на верхний элемент стека. Если стек пуст, top = None

    def isEmpty(self):
        """Проверяет, стек пустой или нет"""
        return self.top is None

    def push(self, value):
        """Добавляет новый элемент в стек"""
        new_node = Node(value)  # Создание нового узела(элемента стека)
        new_node.next = self.top  # Для нового узла передаём текущий верхний элемент стека
        self.top = new_node  # Новый узел становится верхним элементом стека

    def pop(self):
        """Удаляет верхний элемент стека и возвращает его данные"""
        deleted_value = self.top.value  # Сохраняем значение верхнего узла(удаляемого элемента)
        self.top = self.top.next  # Меняем указатель верхеного элемента на следующий узел
        return deleted_value  # Возвращаем значение удалённого узла

    def display_stack(self):
        """Выводит элементы всего стека"""
        current_top = self.top  # Первый элемент стека
        elements = []  # Список для хранения элементов
        while current_top:  # Пока не закончатся все узлы, будем добавлять их в список
            elements.append(current_top.value)
            current_top = current_top.next  # Меняем указатель верхеного элемента на следующий узел
        print(", ".join(map(str, elements)))


if __name__ == "__main__":
    print("---Lab4 Task6_1---")
    stack = Stack()

    print(stack.isEmpty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display_stack()
    stack.pop()
    stack.display_stack()
    stack.pop()
    stack.display_stack()
    print(stack.isEmpty())