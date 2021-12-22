from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        # TODO  инициализировать атрибуты экземпляра класса Node
        ...

    # TODO реализовать метод __repr__ для отображения экземпляра


if __name__ == '__main__':
    first_node = ...  # TODO инициализировать первый узел

    second_node = ...  # TODO инициализировать второй узел
    first_node.next = ...  # TODO через атрибут экземпляра устанавливаем первому узлу следующий узел

    print(first_node)
    print(second_node)
