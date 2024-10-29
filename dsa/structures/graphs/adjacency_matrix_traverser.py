from typing import Optional

from dsa.structures.graphs.abc_base_graph import BaseGraph


class MyAdjMatrTraverser(BaseGraph):
    def are_connected(self, start: int, target: int) -> bool:
        pass

    def __init__(self, graph, size):
        self.graph: list[list[Optional[int]]] = graph
        self.size = size

    def get_targets(self, start) -> list:
        return [
            target
            for target, weight in enumerate(self.graph[start])
            if weight and weight > 0
        ]

    def get_size(self):
        return self.size

    def _traverse_dfs_recursively(self, vertex, visited, result):
        visited[vertex] = True
        result.append(vertex)

        for i in range(0, self.size):
            if self.graph[vertex][i] and self.graph[vertex][i] > 0 and not visited[i]:
                self._traverse_dfs_recursively(i, visited, result)
