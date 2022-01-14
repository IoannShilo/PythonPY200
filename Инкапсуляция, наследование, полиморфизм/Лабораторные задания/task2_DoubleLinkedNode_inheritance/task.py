from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next_ = None
        self.set_next(next_)   # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self.next = next_

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):

    def __init__(self, value, next_=None, prev=None):
        super().__init__(value, next_)
        self.prev = prev


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value}, {self.next}, {self.prev})"



    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self.is_valid(prev)
        self._prev = prev



if __name__ == '__main__':
    prev = DoubleLinkedNode(1)
    node = Node(1)
    node2 = Node(2)
print(repr(node), repr(node2))

