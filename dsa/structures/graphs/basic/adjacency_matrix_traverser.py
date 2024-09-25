from typing import Optional


class MyAdjMatrTraverser:
    def __init__(self, graph, size):
        self.graph: list[list[Optional[int]]] = graph
        self.size = size

    def get_size(self):
        return self.size

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
                for target, weight in enumerate(self.graph[current]):
                    if weight and weight > 0:
                        to_visit.append(target)

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
            if self.graph[vertex][i] and self.graph[vertex][i] > 0 and not visited[i]:
                self._traverse_dfs(i, visited, result)
