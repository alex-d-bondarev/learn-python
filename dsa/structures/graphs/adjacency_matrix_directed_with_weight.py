from collections.abc import Iterable
from typing import Optional

from dijkstra_shortest_path import DijkstraShortestPath
from dsa.structures.graphs.my_naive_path import MyNaivePath
from with_iterable_subgraph import GraphWithIterableSubGraph

from dsa.structures.graphs.adjacency_matrix_traverser import MyAdjMatrTraverser


class MyAdjMatrDirWeightedGraph(MyAdjMatrTraverser, GraphWithIterableSubGraph):
    def __init__(self):
        super().__init__(graph=[[None]], size=1)

    def get_iterable_subgraph(self, index) -> Iterable[tuple[int, int]]:
        return enumerate(self.graph[index])

    def get_size(self) -> int:
        return self.size

    def add_edge(
        self, start: int, target: int, weight: int
    ) -> "MyAdjMatrDirWeightedGraph":
        max_required_size = max(start, target) + 1

        if self.size < max_required_size:
            self._resize(max_required_size)

        self.graph[start][target] = weight

        return self

    def _resize(self, new_size: int) -> None:
        delta = new_size - self.size

        for line in self.graph:
            line += [None for _ in range(delta)]

        for _ in range(delta):
            self.graph.append([None for _ in range(new_size)])

        self.size = new_size

    def are_connected(self, start: int, target: int) -> bool:
        max_vertex = max(start, target)

        if max_vertex > self.get_size():
            return False
        else:
            return self.graph[start][target] is not None

    def connection_weight(self, start: int, target: int) -> Optional[int]:
        if self.are_connected(start, target):
            return self.graph[start][target]

        return None

    def dijkstra_distances(self, start) -> list:
        return MyNaivePath.get_naive_distances(self, start)

    def dijkstra_min_heap(self, start) -> list:
        return DijkstraShortestPath.get_all_distances_optimized(self, start)

    def dijkstra_path(self, start_vertex, target_vertex) -> tuple[int | float, list]:
        return DijkstraShortestPath.get_path(self, start_vertex, target_vertex)

    def dijkstra_narrowed_path(self, start_vertex, target_vertex) -> tuple[int | float, list]:
        return DijkstraShortestPath.get_narrowed_path(self, start_vertex, target_vertex)


def test_connections():
    g = MyAdjMatrDirWeightedGraph()

    g.add_edge(1, 2, 10).add_edge(9, 10, 99)

    assert g.are_connected(1, 2) is True
    assert g.are_connected(2, 1) is False
    assert g.connection_weight(1, 2) == 10
    assert g.connection_weight(2, 1) is None

    assert g.are_connected(1, 9) is False
    assert g.are_connected(20, 30) is False
    assert g.get_size() == 11


def test_traversal():
    g = MyAdjMatrDirWeightedGraph()
    g.add_edge(1, 2, 1).add_edge(9, 10, 1)

    (
        g.add_edge(1, 4, 1)
        .add_edge(1, 15, 2)
        .add_edge(2, 4, 3)
        .add_edge(3, 2, 4)
        .add_edge(3, 5, 5)
        .add_edge(3, 7, 1)
        .add_edge(4, 4, 1)
        .add_edge(4, 6, 1)
        .add_edge(15, 8, 6)
        .add_edge(15, 8, 1)
        .add_edge(15, 20, 1)
    )

    assert g.traverse_bfs(1) == [1, 2, 4, 15, 6, 8, 20]
    assert g.traverse_dfs(1) == [1, 2, 4, 6, 15, 8, 20]


def test_dijkstra():
    g = MyAdjMatrDirWeightedGraph()
    (
        g.add_edge(1, 2, 2)
        .add_edge(1, 3, 15)
        .add_edge(1, 4, 20)
        .add_edge(2, 5, 3)
        .add_edge(2, 6, 3)
        .add_edge(3, 7, 5)
        .add_edge(4, 8, 1)
        .add_edge(6, 3, 4)
        .add_edge(7, 8, 10)
    )

    assert g.dijkstra_distances(1) == [float("inf"), 0, 2, 9, 20, 5, 5, 14, 21]
    assert g.dijkstra_min_heap(1) == [float("inf"), 0, 2, 9, 20, 5, 5, 14, 21]

    assert g.dijkstra_path(1, 7) == (14, [1, 2, 6, 3, 7])
    assert g.dijkstra_narrowed_path(1, 7) == (14, [1, 2, 6, 3, 7])
