from typing import Iterable, Optional, Any

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        print("инит")
        self.head: Optional[Node] = None

        self.list_nodes = []
        if data is not None:
            self.init_linked_list(data)

    def init_linked_list(self, data: Iterable):
        """ Метод, который создает вспомогательный список и связывает в нём узлы. """
        print('инит линкед лист')
        self.list_nodes = [Node(value) for value in data]
        self.head = self.list_nodes[0]

        for i in range(len(self.list_nodes) - 1):
            current_node = self.list_nodes[i]
            next_node = self.list_nodes[i + 1]
            self.linked_nodes(current_node, next_node)

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        print("связали")
        left_node.set_next(right_node)

    def __repr__(self) -> str:
        return str(self.list_nodes)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        print('начало степ бай степ')
        if not isinstance(index, int):
            raise TypeError

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
            print('проход по узлу')
        print("ретерн степ бай степ")
        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        print('гет итем')
        node = self.step_by_step_on_nodes(index)
        print("ретерн гет итем")
        return node.value


if __name__ == "__main__":
    list_ = [1, 2, 3, 4]
    linked_list = LinkedList(list_)

    print(linked_list)
