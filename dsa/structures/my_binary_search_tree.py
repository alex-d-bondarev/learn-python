import logging
from typing import Optional

logger = logging.getLogger(__name__)


class BinaryTreeNode:
    def __init__(
        self,
        value: int,
        left: Optional["BinaryTreeNode"] = None,
        right: Optional["BinaryTreeNode"] = None,
    ):
        self.value: int = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(value={self.value}, left={self.left}, right={self.right})"

    def add(self, value: int) -> None:
        if self.value > value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryTreeNode(value)
        elif self.value < value:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryTreeNode(value)
        else:
            return  # This value already exists and duplicate should not be created

    def find(self, value: int) -> Optional["BinaryTreeNode"]:
        if self.value == value:
            return self

        if self.value > value:
            if self.left:
                return self.left.find(value)
        elif self.right:
            return self.right.find(value)
        return None


class MyBinarySearchTree:
    def __init__(self, value: int):
        self.root: BinaryTreeNode = BinaryTreeNode(value)

    def __repr__(self):
        return f"Tree({self.root})"

    def insert(self, value: int) -> None:
        self.root.add(value)

    def find(self, value) -> Optional["BinaryTreeNode"]:
        return self.root.find(value)

    def height(self) -> int:
        all_nodes = [(0, self.root)]
        height = 0

        while len(all_nodes) > 0:
            level, node = all_nodes.pop()

            if level > height:
                height = level

            if node.left:
                all_nodes.append((level+1, node.left))

            if node.right:
                all_nodes.append((level+1, node.right))

        return height

    def size(self):
        all_nodes = [self.root]
        size = 0

        while len(all_nodes) > 0:
            node = all_nodes.pop()
            size += 1

            if node.left:
                all_nodes.append(node.left)

            if node.right:
                all_nodes.append(node.right)

        return size


def test_tree_flow():
    tree = MyBinarySearchTree(42)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)
    tree.insert(21)
    tree.insert(22)

    twenty = tree.find(21)
    assert twenty.right.value == 22
    assert tree.height() == 4
    assert tree.size() == 7

    logger.info(repr(tree))
