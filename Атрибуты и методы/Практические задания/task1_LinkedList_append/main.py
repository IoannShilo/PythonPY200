from typing import Any, Iterable, Optional

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        print('init')
        self.len = 0
        self.head: Optional[Node] = None

        for value in data:
            self.append(value)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        print('step by step')
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        print(current_node, 'head v step bu step')
        for _ in range(index):
            print(current_node.next, 'current node next')
            current_node = current_node.next
            print(current_node, 'current node', self.head, 'self.head')
        print(current_node, 'return current_node')
        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        print('linked nodes')
        left_node.set_next(right_node)

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        print('начало getitem')
        node = self.step_by_step_on_nodes(index)
        print(node.value, 'возврат getitem')
        return node.value

    def __str__(self) -> str:
        return f"{[node for node in self]}"

    def __len__(self):
        print('--len')
        return self.len

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        print('append')
        append_node = Node(value)  # right node
        print(append_node, 'append node v append')
        print(self.head, 'self.head v append')
        if self.head is None:
            print(' if selfhead is none')
            self.head = append_node
        else:
            print('else')
            print(self.len - 1)
            last_node = self.step_by_step_on_nodes(self.len - 1 )  #left node
            print(last_node, 'last node')
            print(append_node, 'append node')
            self.linked_nodes(last_node, append_node)
        print('len + 1')
        self.len += 1
        print(self.len, 'len')


if __name__ == "__main__":
    list_ = [1, 8, 2, 3, 4]

    ll = LinkedList(list_)
    print(ll)

    ll.append(100)
    print(ll)
