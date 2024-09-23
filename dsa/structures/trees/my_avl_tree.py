# Credit to https://www.w3schools.com/dsa/dsa_data_avltrees.php

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class AvlTreeNode:
    def __init__(
        self,
        value: int | str,
        left: Optional["AvlTreeNode"] = None,
        right: Optional["AvlTreeNode"] = None,
        height: int = 1,
    ):
        self.value: int | str = value
        self.left = left
        self.right = right
        self.height = height


class MyBinarySearchTree:
    def __init__(self, value: int | str):
        self.root: AvlTreeNode = AvlTreeNode(value)

    @staticmethod
    def get_height(node: Optional[AvlTreeNode]) -> int:
        return node.height if node else 0

    def get_balance(self, node: Optional[AvlTreeNode]) -> int:
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, node: AvlTreeNode):
        print("Rotate right on node", node.value)
        left_child = node.left
        right_child_of_left = left_child.right
        left_child.right = node
        node.left = right_child_of_left
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right),
        )
        left_child.height = 1 + max(
            self.get_height(left_child.left),
            self.get_height(left_child.right),
        )
        return left_child

    def left_rotate(self, node: AvlTreeNode):
        print("Rotate left on node", node.value)
        right_child = node.right
        left_child_of_right = right_child.left
        right_child.left = node
        node.right = left_child_of_right
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right),
        )
        right_child.height = 1 + max(
            self.get_height(right_child.left),
            self.get_height(right_child.right),
        )
        return right_child

    def insert(self, value: int | str) -> "MyBinarySearchTree":
        self.root = self._insert(self.root, value)
        return self

    def _insert(self, node: AvlTreeNode, value: int | str):
        if not node:
            return AvlTreeNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        # Update the balance factor and balance the tree
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Balancing the tree
        # Left-Left
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Left-Right
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right-Right
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Right-Left
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def to_string(self) -> str:
        return self._to_string(self.root)

    def _to_string(self, node: AvlTreeNode) -> str:
        if node is None:
            return ""

        if node.left or node.right:
            return f"l=({self._to_string(node.left)}), v={node.value}, r=({self._to_string(node.right)})"

        return node.value


def test_left_left():
    avl_tree = MyBinarySearchTree("Q")

    assert avl_tree.to_string() == "Q"

    avl_tree.insert("P").insert("D")
    assert avl_tree.to_string() == "l=(D), v=P, r=(Q)"

    avl_tree.insert("L").insert("C").insert("B")
    assert avl_tree.to_string() == "l=(l=(B), v=C, r=()), v=D, r=(l=(L), v=P, r=(Q))"


def test_right_right():
    avl_tree = MyBinarySearchTree("A")

    assert avl_tree.to_string() == "A"

    avl_tree.insert("B").insert("D")
    assert avl_tree.to_string() == "l=(A), v=B, r=(D)"

    avl_tree.insert("E").insert("C").insert("F")
    assert avl_tree.to_string() == "l=(l=(A), v=B, r=(C)), v=D, r=(l=(), v=E, r=(F))"


def test_left_right():
    avl_tree = MyBinarySearchTree("Q")

    assert avl_tree.to_string() == "Q"

    avl_tree.insert("E").insert("K")
    assert avl_tree.to_string() == "l=(E), v=K, r=(Q)"

    avl_tree.insert("C").insert("F").insert("G")
    assert avl_tree.to_string() == "l=(l=(C), v=E, r=()), v=F, r=(l=(G), v=K, r=(Q))"


def test_right_left():
    avl_tree = MyBinarySearchTree("A")

    assert avl_tree.to_string() == "A"

    avl_tree.insert("F").insert("B")
    assert avl_tree.to_string() == "l=(A), v=B, r=(F)"

    avl_tree.insert("G").insert("E").insert("D")
    assert avl_tree.to_string() == "l=(l=(A), v=B, r=(D)), v=E, r=(l=(), v=F, r=(G))"


def test_first_7_letters():
    avl_tree = MyBinarySearchTree("A")

    assert avl_tree.to_string() == "A"

    avl_tree.insert("B").insert("C")
    assert avl_tree.to_string() == "l=(A), v=B, r=(C)"

    avl_tree.insert("D")
    assert avl_tree.to_string() == "l=(A), v=B, r=(l=(), v=C, r=(D))"

    avl_tree.insert("E")
    assert avl_tree.to_string() == "l=(A), v=B, r=(l=(C), v=D, r=(E))"

    avl_tree.insert("F")
    assert avl_tree.to_string() == "l=(l=(A), v=B, r=(C)), v=D, r=(l=(), v=E, r=(F))"

    avl_tree.insert("G")
    assert avl_tree.to_string() == "l=(l=(A), v=B, r=(C)), v=D, r=(l=(E), v=F, r=(G))"
