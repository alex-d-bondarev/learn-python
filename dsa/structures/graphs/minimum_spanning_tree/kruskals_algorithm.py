from collections import namedtuple
from typing import Optional

from dsa.structures.graphs.minimum_spanning_tree.mst import MST

Edge = namedtuple("Edge", ["left", "right", "weight"])


class ListGraph:
    def __init__(self, size):
        self.size = size
        self.edges: list[Edge] = []
        self.parents: list[Optional[int]] = [None] * size
        self.ranks: list[int] = [0] * size
        self.weights: list[int] = [0] * size

    def add_edge(self, left, right, weight) -> "ListGraph":
        if self._out_of_bounds(left) or self._out_of_bounds(left):
            error_msg = f"Unexpected edge values {left} and {right}"
            raise ValueError(error_msg)

        self.edges.append(Edge(left=left, right=right, weight=weight))
        return self

    def find_parent(self, child) -> Optional[int]:
        if self.parents[child] is None:
            self.parents[child] = child
            return child
        if self.parents[child] == child:
            return child
        return self.find_parent(self.parents[child])

    def union(self, edge: Edge) -> None:
        left_root = self.find_parent(edge.left)
        right_root = self.find_parent(edge.right)

        if self.ranks[left_root] < self.ranks[right_root]:
            self.parents[edge.left] = edge.right
            self.weights[edge.left] = edge.weight
        elif self.ranks[left_root] > self.ranks[right_root]:
            self.parents[edge.right] = edge.left
            self.weights[edge.right] = edge.weight
        else:
            self.parents[edge.right] = edge.left
            self.weights[edge.right] = edge.weight
            self.ranks[edge.left] += 1

    def _out_of_bounds(self, child):
        return not 0 <= child < self.size


def find_kruskal_mst(graph: ListGraph) -> MST:
    graph.edges = sorted(graph.edges, key=lambda edge: edge.weight)

    for edge in graph.edges:
        left_root = graph.find_parent(edge.left)
        right_root = graph.find_parent(edge.right)

        if left_root != right_root:
            graph.union(edge)

    return MST(parents=graph.parents, weights=graph.weights)


def test_kruskal_mst():
    graph = ListGraph(6)

    (
        graph.add_edge(0, 1, 1)
        .add_edge(0, 2, 8)
        .add_edge(0, 4, 6)
        .add_edge(1, 3, 2)
        .add_edge(2, 3, 4)
        .add_edge(2, 4, 5)
        .add_edge(3, 5, 3)
        .add_edge(4, 5, 9)
    )

    mst = find_kruskal_mst(graph)
    assert mst.parents == [0, 0, 3, 1, 2, 3]
    assert mst.weights == [0, 1, 4, 2, 5, 3]


def test_w3s_example():
    graph = ListGraph(7)

    (
        graph.add_edge(0, 1, 4)
        .add_edge(0, 6, 10)
        .add_edge(0, 2, 9)
        .add_edge(1, 2, 8)
        .add_edge(2, 3, 5)
        .add_edge(2, 4, 2)
        .add_edge(2, 6, 7)
        .add_edge(3, 4, 3)
        .add_edge(3, 5, 7)
        .add_edge(4, 6, 6)
        .add_edge(5, 6, 11)
    )

    mst = find_kruskal_mst(graph)
    assert mst.parents == [0, 0, 1, 4, 2, 3, 4]
    assert mst.weights == [0, 4, 8, 3, 2, 7, 6]
