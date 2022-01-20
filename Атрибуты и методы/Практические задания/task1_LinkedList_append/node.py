from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        print('init node')
        self.value = value
        print(self.value, 'self.value v init node')

        self.next = None
        self.set_next(next_)


    def __repr__(self) -> str:
        print('repr')
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:

        return str(self.value)

    def is_valid(self, node: Any) -> None:
        print('is valid')
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        print('set_next')
        print(self.next, 'set next v set next do cikla')
        self.is_valid(next_)
        self.next = next_
        print(self.next, 'set next v set next posle cikla')

