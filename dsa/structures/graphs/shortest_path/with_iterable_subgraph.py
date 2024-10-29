from abc import ABC, abstractmethod
from collections.abc import Iterable

from dsa.structures.graphs.shortest_path.abc_base_graph import BaseGraph


class GraphWithIterableSubGraph(BaseGraph, ABC):
    @abstractmethod
    def get_iterable_subgraph(self, index) -> Iterable[tuple[int, int]]:
        pass
