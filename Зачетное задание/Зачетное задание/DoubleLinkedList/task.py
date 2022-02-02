from collections.abc import MutableSequence

from typing import Any, Iterable, Optional

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):

    CLASS_NODE = Node

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    @staticmethod
    def type_error(index: int) -> None:
        """
        Метод, который проводит проверку TypeError
        :param index:
        """
        if not isinstance(index, int):
            raise TypeError()

    def index_error(self, index: int) -> None:
        """
        Метод проводит проверку IndexError
        :param index:
        """
        if not 0 <= index < self._len:
            raise IndexError()

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Метод, который связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        print('linked nodes')
        left_node.next = right_node

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = self.CLASS_NODE(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        self.type_error(index)
        self.index_error(index)

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node




    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        self.type_error(index)
        self.index_error(index)

        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self._len -= 1

    def insert(self, index: int, value: Any) -> None:
        self.type_error(index)

        insert_node = self.CLASS_NODE(value)

        if index == 0:
            insert_node.next = self._head
            self._head = insert_node
            self._len += 1
        elif index >= self._len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self._len += 1

    def __len__(self):
        return self._len

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"


class DoubleLinkedList(LinkedList):

    CLASS_NODE = DoubleLinkedNode

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node


if __name__ == "__main__":
    list_ = [1, 2, 3, 4]

    dll = DoubleLinkedList(list_)
    del(dll[2])
    print(dll)







