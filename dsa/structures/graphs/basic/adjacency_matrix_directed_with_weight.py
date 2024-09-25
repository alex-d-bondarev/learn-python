from typing import Optional

from dsa.structures.graphs.basic.adjacency_matrix_traverser import MyAdjMatrTraverser


class MyAdjMatrDirWeightedGraph:
    def __init__(self):
        self.graph: list[list[Optional[int]]] = [[None]]
        self.size = 1

    def get_size(self):
        return self.size

    def add_edge(
        self, first_vertex: int, second_vertex: int, weight: int
    ) -> "MyAdjMatrDirWeightedGraph":
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

    def traverse_bfs(self, start) -> list:
        """Breadth First Search Traversal"""
        traverser = MyAdjMatrTraverser(graph=self.graph, size=self.size)
        return traverser.traverse_bfs(start=start)

    def traverse_dfs(self, start) -> list:
        """Depth First Search Traversal"""
        traverser = MyAdjMatrTraverser(graph=self.graph, size=self.size)
        return traverser.traverse_dfs(start=start)

    def dijkstra(self, start) -> list:
        distances = [float("inf")] * self.size
        distances[start] = 0
        to_visit = [start]

        while len(to_visit) > 0:
            current = to_visit.pop()
            for target, weight in enumerate(self.graph[current]):
                if weight and weight > 0:
                    distance = distances[current] + weight
                    if distance < distances[target]:
                        distances[target] = distance
                        to_visit.append(target)

        return distances

    def dijkstra_path(self, start_vertex, target_vertex) -> tuple[int | float, list]:
        distances, predecessors = self._dijkstra_distances_and_predecessors(start_vertex)
        distance = distances[target_vertex]

        if distance == float("inf"):
            return float("inf"), []

        return distance, self._prepare_path(predecessors, target_vertex)

    def _dijkstra_distances_and_predecessors(self, start_vertex) -> tuple[list, list]:
        distances = [float("inf")] * self.size
        distances[start_vertex] = 0
        predecessors = [None for _ in range(self.size)]

        to_visit = [start_vertex]
        while len(to_visit) > 0:
            current = to_visit.pop()
            for target, weight in enumerate(self.graph[current]):
                if weight and weight > 0:
                    distance = distances[current] + weight
                    if distance < distances[target]:
                        distances[target] = distance
                        predecessors[target] = current
                        to_visit.append(target)

        return distances, predecessors

    def _prepare_path(self, predecessors, target_vertex):
        predecessor = target_vertex
        path = []
        while predecessor:
            path.append(predecessor)
            predecessor = predecessors[predecessor]
        return list(reversed(path))


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

    assert g.dijkstra(1) == [float("inf"), 0, 2, 9, 20, 5, 5, 14, 21]
    assert g.dijkstra_path(1, 7) == (14, [1, 2, 6, 3, 7])
