import unittest

from typing import Any, Iterable, Optional

from node import Node, DoubleLinkedNode
from task import LinkedList, DoubleLinkedList

@unittest.skip("Будет проверен позже")
class TestCaseNode(unittest.TestCase):

    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(5)
        self.assertIsNone(node.next)

        self.assertEqual(5, node.value)

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        right_node = Node("right")
        left_node = Node("left", next_=right_node)

        self.assertIs(right_node, left_node.next)
        self.assertIsNone(right_node.next)
        self.assertEqual("left", left_node.value)
        self.assertEqual("right", right_node.value)

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node = Node(5)

        expected_repr = "Node(5, None)"
        self.assertEqual(repr(node), expected_repr,
                         msg="Неправильный __repr__")

    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        node = Node(5, Node(10))

        expected_repr = "Node(5, Node(10))"
        self.assertEqual(repr(node), expected_repr,
                         msg="Неправильный __repr__")

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        self.assertEqual(str(node), str(some_value))

    def test_is_valid(self):
        Node.is_valid(None)
        Node.is_valid(Node(5))

        with self.assertRaises(TypeError):
            Node.is_valid(5)


class TestCaseDoubleLinkedNode(unittest.TestCase):

    def test_init_double_linked_node_without_prev(self):
        dln = DoubleLinkedNode(5)

        self.assertIsNone(dln.next)
        self.assertIsNone(dln.prev)

    @unittest.skip
    def test_init_double_linked_node_with_prev(self):
        first_node = DoubleLinkedNode("1")
        third_node = DoubleLinkedNode("3")
        second_node = DoubleLinkedNode("2", next_=right_node, prev=left_node)


    def test_repr_double_linked_node_without_prev(self):
        """Проверить метод __repr__, для случая когда нет предыдущего узла."""
        dln = DoubleLinkedNode(5)

        expected_repr = "DoubleLinkedNode(5, None, None)"
        self.assertEqual(repr(dln), expected_repr,
                         msg="Неправильный __repr__")

    def test_is_valid_double_linked_node(self):
        DoubleLinkedNode.is_valid(None)
        DoubleLinkedNode.is_valid(DoubleLinkedNode(5))

        with self.assertRaises(TypeError):
            DoubleLinkedNode.is_valid(5)


class TestCaseLinkedList(unittest.TestCase):

    def test_class_attribute(self):
        self.assertEqual(LinkedList.CLASS_NODE, Node)

    def test_init_linked_list(self):
        ll = LinkedList([1, 2, 3, 4, 5])

        self.assertIsInstance(ll, Iterable, None)
        self.assertEqual(ll._len, 5)
        with self.assertRaises(AssertionError):
            self.assertEqual(ll._len, 0)

        self.assertEqual(ll._head, 1)




