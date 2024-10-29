# Based on https://www.w3schools.com/dsa/dsa_algo_mst_prim.php
from collections import namedtuple

Neighbor = namedtuple("Neighbor", ["position", "weight"])


class MyAdjMatrUnDirWeightedGraph:
    def __init__(self, size):
        self.matrix = [[None] * size for _ in range(size)]
        self.size = size

    def add_edge(self, first, second, weight) -> "MyAdjMatrUnDirWeightedGraph":
        if 0 <= first < self.size and 0 <= second < self.size:
            self.matrix[first][second] = weight
            self.matrix[second][first] = weight
        return self

    def get_neighbors(self, index) -> list[Neighbor]:
        return [
            Neighbor(position=position, weight=weight)
            for position, weight in enumerate(self.matrix[index])
            if weight
        ]
