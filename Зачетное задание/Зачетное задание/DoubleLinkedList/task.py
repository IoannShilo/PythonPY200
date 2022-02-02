from collections.abc import MutableSequence

from typing import Any, Iterable, Optional

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):

    CLASS_NODE = Node
    count = 0

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._data = data
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head
        cls = self.__class__
        cls.count += 1

        if data is not None:
            for value in data:
                self.append(value)

    @classmethod
    def counter(cls):
        print(cls.count)

    @staticmethod
    def type_error(index) -> None:
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
        Метод связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def append(self, value: Any):
        """ Метод добавляет элемента в конец связного списка. """
        append_node = self.CLASS_NODE(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Метод выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        self.type_error(index)
        self.index_error(index)

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __iter__(self):
        print('вызываю __iter__')
        current_node = self._head
        for _ in range(len(self)):
            yield current_node.value
            current_node = current_node.next

    def __contains__(self, item) -> bool:
        print('вызываю __contains__')
        for current_value in self:
            if current_value == item:
                return True
        return False

    def __reversed__(self):
        for i in range(len(self)-1, -1, -1):
            yield self[i]

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        print('вызываю __getitem__')
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        self.type_error(index)
        self.index_error(index)
        print('вызываю __delitem__')
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
        """
        Метод вставляет в связный список новый элемент по указанному индексу
        :param index:
        :param value:
        """
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

    def remove(self, value):
        if value not in self:  # if not self.__contains__(value):
            raise ValueError

        for i in self._data:

            if i == value:
                self.__delitem__(i)



class DoubleLinkedList(LinkedList):
    CLASS_NODE = DoubleLinkedNode
    count = 0

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node


if __name__ == "__main__":
    ll = LinkedList()
    print(ll.counter())

    list_ = [1, 2, 3, 4]
    dll_1 = DoubleLinkedList(list_)
    # dll.remove(1)
    # print(dll)
    dll_2 = DoubleLinkedList(list_)

    print(LinkedList.counter())
    print(DoubleLinkedList.counter())


    # print(1 in dll)
    # print(7 in dll)
    # for item in dll:
    #     print(item)










