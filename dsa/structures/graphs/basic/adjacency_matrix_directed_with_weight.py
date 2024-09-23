from typing import Optional


class MyAMDWWGraph:
    def __init__(self):
        self.graph: list[list[Optional[int]]] = [[None]]
        self.size = 1

    def get_size(self):
        return self.size

    def add_edge(
        self, first_vertex: int, second_vertex: int, weight: int
    ) -> "MyAMDWWGraph":
        max_required_size = max(first_vertex, second_vertex) + 1

        if self.size < max_required_size:
            self._resize(max_required_size)

        self.graph[first_vertex][second_vertex] = weight

        return self

    def _resize(self, new_size: int) -> None:
        delta = new_size - self.size

        for line in self.graph:
            line += [None for _ in range(delta)]

        for _ in range(delta):
            self.graph.append([None for _ in range(new_size)])

        self.size = new_size

    def are_connected(self, first_vertex: int, second_vertex: int) -> bool:
        max_vertex = max(first_vertex, second_vertex)

        if max_vertex > self.get_size():
            return False
        else:
            return self.graph[first_vertex][second_vertex] is not None

    def connection_weight(self, first_vertex: int, second_vertex: int) -> Optional[int]:
        if self.are_connected(first_vertex, second_vertex):
            return self.graph[first_vertex][second_vertex]

        return None


def test_connections():
    g = MyAMDWWGraph()

    g.add_edge(1, 2, 10).add_edge(9, 10, 99)

    assert g.are_connected(1, 2) is True
    assert g.are_connected(2, 1) is False
    assert g.connection_weight(1, 2) == 10
    assert g.connection_weight(2, 1) is None

    assert g.are_connected(1, 9) is False
    assert g.are_connected(20, 30) is False
    assert g.get_size() == 11
