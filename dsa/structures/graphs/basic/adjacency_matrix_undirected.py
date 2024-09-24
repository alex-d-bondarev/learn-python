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

    def traverse_bfs(self, start) -> list:
        """Breadth First Search Traversal"""
        visited = [False for _ in range(self.size)]
        to_visit = [start]
        result = []

        while len(to_visit) > 0:
            current = to_visit.pop(0)
            if not visited[current]:
                visited[current] = True
                result.append(current)
                for index, value in enumerate(self.graph[current]):
                    if value == 1:
                        to_visit.append(index)

        return result

    def traverse_dfs(self, start) -> list:
        """Depth First Search Traversal"""
        visited = [False for _ in range(self.size)]
        result = []

        self._traverse_dfs(start, visited, result)

        return result

    def _traverse_dfs(self, vertex, visited, result):
        visited[vertex] = True
        result.append(vertex)

        for i in range(0, self.size):
            if self.graph[vertex][i] == 1 and not visited[i]:
                self._traverse_dfs(i, visited, result)


def test_connections():
    g = MyAMUGraph()

    g.add_edge(1, 2).add_edge(9, 10)

    assert g.are_connected(1, 2) is True
    assert g.are_connected(1, 9) is False
    assert g.are_connected(20, 30) is False
    assert g.get_size() == 11


def test_traversal():
    g = MyAMUGraph()
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
