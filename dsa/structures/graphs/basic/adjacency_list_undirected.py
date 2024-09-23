class MyALUGraph:
    def __init__(self):
        self.a_list = [[]]

    def get_size(self):
        return len(self.a_list)

    def add_edge(self, first_vertex: int, second_vertex: int) -> "MyALUGraph":
        max_required_size = max(first_vertex, second_vertex) + 1

        if self.get_size() < max_required_size:
            self._resize(max_required_size)

        self.a_list[first_vertex].append(second_vertex)
        self.a_list[second_vertex].append(first_vertex)

        return self

    def _resize(self, new_size: int) -> None:
        delta = new_size - self.get_size()
        self.a_list += [[] for _ in range(delta)]
        self.size = new_size

    def are_connected(self, first_vertex: int, second_vertex: int) -> bool:
        max_vertex = max(first_vertex, second_vertex)

        if max_vertex > self.get_size():
            return False
        else:
            return second_vertex in self.a_list[first_vertex]


def test_connections():
    g = MyALUGraph()

    g.add_edge(1, 2).add_edge(9, 10)

    assert g.are_connected(1, 2) is True
    assert g.are_connected(1, 9) is False
    assert g.are_connected(20, 30) is False
    assert g.get_size() == 11
