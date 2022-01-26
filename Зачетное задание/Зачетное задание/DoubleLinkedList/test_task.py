import unittest

from node import Node, DoubleLinkedNode
from task import LinkedList, DoubleLinkedList


class TestCase(unittest.TestCase):

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
    @unittest.skip("Будет реализован позже")
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

    def test_init_double_linked_node_without_prev(self):
        dln = DoubleLinkedNode(5)

        self.assertIsNone(dln.next)
        self.assertIsNone(dln.prev)

    def test_init_double_linked_node_with_prev(self):
        right_node = DoubleLinkedNode("right")
        left_node = DoubleLinkedNode("left", next_= right_node)
        prev_node = DoubleLinkedNode("right", prev=left_node, next_=right_node)

        self.assertIs(right_node, left_node.next)
        self.assertIs(left_node, prev_node.prev)
        self.assertIsNone(right_node.next)
        self.assertIsNone(left_node.prev)
        self.assertEqual("left", left_node.value)
        self.assertEqual("right", right_node.value)
        self.assertEqual(prev_node.value, left_node.next.value)
        self.assertEqual(right_node.value, left_node.next.value)

