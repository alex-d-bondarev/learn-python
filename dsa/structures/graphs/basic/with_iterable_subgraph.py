from abc import ABC, abstractmethod
from collections.abc import Iterable


class WithIterableSubGraph(ABC):
    @abstractmethod
    def get_iterable_subgraph(self, index) -> Iterable[tuple[int, int]]:
        pass
