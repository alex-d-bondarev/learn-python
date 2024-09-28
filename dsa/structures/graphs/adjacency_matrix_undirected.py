from typing import Optional

from dsa.structures.graphs.adjacency_matrix_traverser import MyAdjMatrTraverser


class MyAdjMatrUndirGraph(MyAdjMatrTraverser):
    def __init__(self):
        super().__init__(graph=[[None]], size=1)

    def get_size(self):
        return self.size

    def add_edge(self, start: int, target: int) -> "MyAdjMatrUndirGraph":
        max_required_size = max(start, target) + 1

        if self.size < max_required_size:
            self._resize(max_required_size)

        self.graph[start][target] = 1
        self.graph[target][start] = 1

        return self

    def _resize(self, new_size: int) -> None:
        delta = new_size - self.size

        for line in self.graph:
            line += [0 for _ in range(delta)]

        for _ in range(delta):
            self.graph.append([0 for _ in range(new_size)])

        self.size = new_size

    def are_connected(self, start: int, target: int) -> bool:
        max_vertex = max(start, target)

        if max_vertex > self.size:
            return False
        else:
            return self.graph[start][target] == 1


def test_connections():
    g = MyAdjMatrUndirGraph()

    g.add_edge(1, 2).add_edge(9, 10)

    assert g.are_connected(1, 2) is True
    assert g.are_connected(1, 9) is False
    assert g.are_connected(20, 30) is False
    assert g.get_size() == 11


def test_traversal():
    g = MyAdjMatrUndirGraph()
    g.add_edge(1, 2).add_edge(9, 10)

    (
        g.add_edge(1, 4)
        .add_edge(1, 15)
        .add_edge(2, 4)
        .add_edge(3, 2)
        .add_edge(3, 5)
        .add_edge(3, 7)
        .add_edge(4, 4)
        .add_edge(4, 6)
        .add_edge(15, 6)
        .add_edge(15, 8)
        .add_edge(15, 20)
    )

    assert g.traverse_bfs(1) == [1, 2, 4, 15, 3, 6, 8, 20, 5, 7]
    assert g.traverse_dfs(1) == [1, 2, 3, 5, 7, 4, 6, 15, 8, 20]
