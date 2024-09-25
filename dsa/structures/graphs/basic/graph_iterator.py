from abc import ABC, abstractmethod
from collections.abc import Iterable


class MyGraphIterator(ABC):
    @abstractmethod
    def sub_graph_iterator(self, index) -> Iterable[tuple[int, int]]:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass
