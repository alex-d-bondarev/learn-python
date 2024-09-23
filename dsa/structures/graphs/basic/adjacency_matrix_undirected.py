class MyAMUGraph:
    def __init__(self):
        self.graph = [[0]]
        self.size = 1

    def get_size(self):
        return self.size

    def add_edge(self, first_vertex: int, second_vertex: int) -> "MyAMUGraph":
        max_required_size = max(first_vertex, second_vertex) + 1

        if self.size < max_required_size:
            self._resize(max_required_size)

        self.graph[first_vertex][second_vertex] = 1
        self.graph[second_vertex][first_vertex] = 1

        return self

    def _resize(self, new_size: int) -> None:
        delta = new_size - self.size

        for line in self.graph:
            line += [0 for _ in range(delta)]

        for _ in range(delta):
            self.graph.append([0 for _ in range(new_size)])

        self.size = new_size

    def are_connected(self, first_vertex: int, second_vertex: int) -> bool:
        max_vertex = max(first_vertex, second_vertex)

        if max_vertex > self.size:
            return False
        else:
            return self.graph[first_vertex][second_vertex] == 1


def test_connections():
    g = MyAMUGraph()

    g.add_edge(1, 2).add_edge(9, 10)

    assert g.are_connected(1, 2) is True
    assert g.are_connected(1, 9) is False
    assert g.are_connected(20, 30) is False
    assert g.get_size() == 11
