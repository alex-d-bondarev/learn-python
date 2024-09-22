import logging
from typing import Optional

logger = logging.getLogger(__name__)


class TreeNode:
    ROOT_VALUE = "root"

    def __init__(
        self,
        value: Optional[str],
        children: Optional[list["TreeNode"]] = None,
    ):
        self.children: list[TreeNode] = children if children else list()
        self.value: Optional[str] = value

    def __repr__(self):
        return f"TreeNode(value={self.value}, children={self.children})"

    def is_root(self) -> bool:
        return self.value == self.ROOT_VALUE

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def is_child(self) -> bool:
        return not self.is_root()

    def is_parent(self) -> bool:
        return not self.is_leaf()


class MyTree:
    def __init__(self):
        self.root = TreeNode(TreeNode.ROOT_VALUE, None)

    def __repr__(self):
        return f"Tree({self.root})"

    def add_child(self, value) -> None:
        new_child = TreeNode(value, None)
        self.root.children.append(new_child)

    def find(self, value) -> Optional[TreeNode]:
        unparsed = [self.root]

        while len(unparsed) > 0:
            pointer = unparsed.pop(0)

            if pointer.value == value:
                return pointer

            unparsed += pointer.children

        return None

    def add_sub_child(self, child_value, value):
        child = self.find(child_value)

        if child:
            new_node = TreeNode(value, None)
            child.children.append(new_node)

    def height(self) -> int:
        all_nodes = [(0, self.root)]
        height = 0

        while len(all_nodes) > 0:
            level, node = all_nodes.pop()

            if level > height:
                height = level

            if node.is_parent():
                for child in node.children:
                    all_nodes.append((level + 1, child))

        return height

    def size(self):
        all_nodes = [self.root]
        size = 0

        while len(all_nodes) > 0:
            node = all_nodes.pop()
            size += 1

            if node.is_parent():
                all_nodes += node.children

        return size


def test_tree_flow():
    tree = MyTree()
    tree.add_child("first")
    tree.add_child("second")

    second = tree.find("second")
    assert second.value == "second"

    tree.add_sub_child("second", "first_sub_second")
    assert second.children[0].value == "first_sub_second"

    assert tree.find("does not exist") is None

    assert tree.root.is_root() is True
    assert second.is_root() is False

    assert tree.root.is_child() is False
    assert second.is_child() is True

    assert second.is_leaf() is False
    assert second.children[0].is_leaf() is True

    assert second.is_parent() is True
    assert second.children[0].is_parent() is False

    assert tree.height() == 2
    assert tree.size() == 4

    logger.info(repr(tree))
