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
