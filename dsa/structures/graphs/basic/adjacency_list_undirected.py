class MyAdjListUndirectedGraph:
    def __init__(self):
        self.a_list = [[]]

    def get_size(self):
        return len(self.a_list)

    def add_edge(self, start: int, target: int) -> "MyAdjListUndirectedGraph":
        max_required_size = max(start, target) + 1

        if self.get_size() < max_required_size:
            self._resize(max_required_size)

        self.a_list[start].append(target)
        self.a_list[start] = sorted(self.a_list[start])

        if start != target:
            self.a_list[target].append(start)
            self.a_list[target] = sorted(self.a_list[target])

        return self

    def _resize(self, new_size: int) -> None:
        delta = new_size - self.get_size()
        self.a_list += [[] for _ in range(delta)]
        self.size = new_size

    def are_connected(self, start: int, target: int) -> bool:
        max_vertex = max(start, target)

        if max_vertex > self.get_size():
            return False
        else:
            return target in self.a_list[start]

    def traverse_bfs(self, start) -> list:
        """Breadth First Search Traversal"""
        result = []
        visited = [False for _ in range(self.get_size())]
        to_visit = [start]

        while len(to_visit) > 0:
            current = to_visit.pop(0)
            if not visited[current]:
                visited[current] = True
                result.append(current)
                to_visit += self.a_list[current]

        return result

    def traverse_dfs(self, start) -> list:
        """Depth First Search Traversal"""
        visited = [False for _ in range(self.get_size())]
        result = []

        self._traverse_dfs(start, visited, result)

        return result

    def _traverse_dfs(self, vertex, visited, result):
        visited[vertex] = True
        result.append(vertex)

        for next_v in self.a_list[vertex]:
            if not visited[next_v]:
                self._traverse_dfs(next_v, visited, result)


def test_connections():
    g = MyAdjListUndirectedGraph()

    g.add_edge(1, 2).add_edge(9, 10)

    assert g.are_connected(1, 2) is True
    assert g.are_connected(1, 9) is False
    assert g.are_connected(20, 30) is False
    assert g.get_size() == 11


def test_traversal():
    g = MyAdjListUndirectedGraph()
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
