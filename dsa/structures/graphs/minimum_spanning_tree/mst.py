from dataclasses import dataclass


@dataclass(frozen=True)
class MST:
    parents: list[str | int]
    weights: list[int]
