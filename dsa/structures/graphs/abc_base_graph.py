from abc import ABC, abstractmethod


class BaseGraph(ABC):
    @abstractmethod
    def add_edge(self, *args, **kwargs) -> "BaseGraph":
        pass

    @abstractmethod
    def are_connected(self, start: int, target: int) -> bool:
        pass

    @abstractmethod
    def get_targets(self, start) -> list:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def _traverse_dfs_recursively(self, vertex, visited, result) -> None:
        pass

    def traverse_bfs(self, start) -> list:
        """Breadth First Search Traversal"""
        visited = [False for _ in range(self.get_size())]
        to_visit = [start]
        result = []

        while len(to_visit) > 0:
            current = to_visit.pop(0)
            if not visited[current]:
                visited[current] = True
                result.append(current)
                to_visit += self.get_targets(current)

        return result

    def traverse_dfs(self, start) -> list:
        """Depth First Search Traversal"""
        visited = [False for _ in range(self.get_size())]
        result = []

        self._traverse_dfs_recursively(start, visited, result)

        return result
