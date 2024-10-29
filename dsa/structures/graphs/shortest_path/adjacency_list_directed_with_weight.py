from collections.abc import Iterable
from typing import Optional

from dsa.structures.graphs.shortest_path.dijkstra_shortest_path import DijkstraShortestPath
from dsa.structures.graphs.shortest_path.my_naive_path import MyNaivePath
from dsa.structures.graphs.shortest_path.with_iterable_subgraph import GraphWithIterableSubGraph


class MyAdjListDirectedWeightedGraph(GraphWithIterableSubGraph):
    def __init__(self):
        self.a_list = [[]]

    def get_targets(self, start) -> list:
        return [target for target, _ in self.a_list[start]]

    def get_iterable_subgraph(self, index) -> Iterable[tuple[int, int]]:
        return self.a_list[index]

    def get_size(self):
        return len(self.a_list)

    def add_edge(
        self, start: int, target: int, weight: int
    ) -> "MyAdjListDirectedWeightedGraph":
        max_required_size = max(start, target) + 1

        if self.get_size() < max_required_size:
            self._resize(max_required_size)

        self.a_list[start].append((target, weight))

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
            for vertex, _ in self.a_list[start]:
                if vertex == target:
                    return True
        return False

    def connection_weight(self, start: int, target: int) -> Optional[int]:
        max_vertex = max(start, target)

        if max_vertex > self.get_size():
            return False
        else:
            for vertex, weight in self.a_list[start]:
                if vertex == target:
                    return weight
        return None

    def _traverse_dfs_recursively(self, vertex, visited, result):
        visited[vertex] = True
        result.append(vertex)

        for next_v, _ in self.a_list[vertex]:
            if not visited[next_v]:
                self._traverse_dfs_recursively(next_v, visited, result)

    def naive_distances(self, start) -> list:
        return MyNaivePath.get_naive_distances(self, start)

    def dijkstra_min_heap(self, start) -> list:
        return DijkstraShortestPath.get_all_distances_optimized(self, start)

    def dijkstra_path(self, start_vertex, target_vertex) -> tuple[int | float, list]:
        return DijkstraShortestPath.get_path(self, start_vertex, target_vertex)

    def dijkstra_narrowed_path(
        self, start_vertex, target_vertex
    ) -> tuple[int | float, list]:
        return DijkstraShortestPath.get_narrowed_path(self, start_vertex, target_vertex)

    def bellman_ford_path(self, start_vertex, target_vertex) -> tuple[int | float, list]:
        graph_size = self.get_size()
        sweeps = 0
        did_update = True

        results = [(None, float("inf"))] * graph_size  # predecessor, distance
        results[start_vertex] = (None, 0)

        while did_update and sweeps < graph_size:
            did_update = False

            for vertex_inx in range(graph_size):
                current, distance = results[vertex_inx]
                for target, weight in self.a_list[vertex_inx]:
                    target_predecessor, target_distance = results[target]
                    new_distance = distance + weight

                    if new_distance < target_distance:
                        did_update = True
                        results[target] = (vertex_inx, new_distance)

            sweeps += 1

        if sweeps == graph_size:
            return float("inf"), []

        predecessor, distance = results[target_vertex]
        path = [target_vertex]

        while predecessor:
            path.append(predecessor)
            predecessor, _ = results[predecessor]
        return distance, list(reversed(path))


def test_connections():
    g = MyAdjListDirectedWeightedGraph()

    g.add_edge(1, 2, 10).add_edge(9, 10, 99)

    assert g.are_connected(1, 2) is True
    assert g.are_connected(2, 1) is False
    assert g.connection_weight(1, 2) == 10
    assert g.connection_weight(2, 1) is None

    assert g.are_connected(1, 9) is False
    assert g.are_connected(20, 30) is False
    assert g.get_size() == 11


def test_traversal():
    g = MyAdjListDirectedWeightedGraph()
    g.add_edge(1, 2, 1).add_edge(9, 10, 1)

    (
        g.add_edge(1, 4, 1)
        .add_edge(1, 15, 1)
        .add_edge(2, 4, 1)
        .add_edge(3, 2, 1)
        .add_edge(3, 5, 1)
        .add_edge(3, 7, 1)
        .add_edge(4, 4, 1)
        .add_edge(4, 6, 1)
        .add_edge(15, 6, 1)
        .add_edge(15, 8, 1)
        .add_edge(15, 20, 1)
    )

    assert g.traverse_bfs(1) == [1, 2, 4, 15, 6, 8, 20]
    assert g.traverse_dfs(1) == [1, 2, 4, 6, 15, 8, 20]


def test_dijkstra():
    g = MyAdjListDirectedWeightedGraph()
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

    assert g.naive_distances(1) == [float("inf"), 0, 2, 9, 20, 5, 5, 14, 21]
    assert g.dijkstra_min_heap(1) == [float("inf"), 0, 2, 9, 20, 5, 5, 14, 21]
    assert g.dijkstra_path(1, 7) == (14, [1, 2, 6, 3, 7])
    assert g.dijkstra_narrowed_path(1, 7) == (14, [1, 2, 6, 3, 7])


def test_graph_with_negative_weights():
    g = MyAdjListDirectedWeightedGraph()
    (
        g.add_edge(1, 2, 50)
        .add_edge(1, 7, 20)
        .add_edge(1, 8, 45)
        .add_edge(2, 6, -10)
        .add_edge(4, 3, -5)
        .add_edge(5, 3, -5)
        .add_edge(6, 4, -10)
        .add_edge(6, 8, -20)
        .add_edge(7, 3, 30)
        .add_edge(8, 5, -10)
        .add_edge(8, 7, 5)
    )
    assert g.naive_distances(1) == [float("inf"), 0, 50, 5, 30, 10, 40, 20, 20]
    assert g.dijkstra_path(1, 3) == (30, [1, 8, 5, 3])
    assert g.dijkstra_narrowed_path(1, 3) == (25, [1, 2, 6, 4, 3])
    assert g.bellman_ford_path(1, 3) == (5, [1, 2, 6, 8, 5, 3])
