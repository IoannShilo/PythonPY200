from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def is_valid(cls, node: Any) -> None:
        if not isinstance(node, (type(None), cls)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"] = None):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, prev: Optional["DoubleLinkedNode"] = None,
                 next_: Optional["DoubleLinkedNode"] = None):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self) -> str:
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"  # todo make all

        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self.is_valid(prev)
        self._prev = prev
