from typing import Optional


class Vertex:
    def __init__(self, position, name):
        self.position: int = position
        self.name: str = name


class MatrixGraph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix: list[list[int]] = [[0] * size for _ in range(size)]
        self.vertexes: list[Optional[Vertex]] = [None] * size

    def add_edge(self, left, right, capacity) -> "MatrixGraph":
        self.adj_matrix[left][right] = capacity
        return self

    def add_vertex_data(self, vertex: Vertex):
        if 0 <= vertex.position < self.size:
            self.vertexes[vertex.position] = vertex
        else:
            error = f"{vertex} position must be between 0 and {self.size}"
            raise ValueError(error)

    def dfs(self, s, t, visited=None, path=None):
        if visited is None:
            visited = [False] * self.size
        if path is None:
            path = []

        visited[s] = True
        path.append(s)

        if s == t:
            return path

        for index, capacity in enumerate(self.adj_matrix[s]):
            if not visited[index] and capacity > 0:
                result_path = self.dfs(index, t, visited, path.copy())
                if result_path:
                    return result_path

        return None

    def bfs(self, s, t, parents: list):
        visited = [False] * self.size
        queue = [s]
        visited[s] = True

        while queue:
            left = queue.pop(0)

            for right_index, right in enumerate(self.adj_matrix[left]):
                if not visited[right_index] and right > 0:
                    queue.append(right_index)
                    visited[right_index] = True
                    parents[right_index] = left

        return visited[t]
