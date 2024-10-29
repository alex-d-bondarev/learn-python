from collections import namedtuple
from heapq import heappop, heappush

from dsa.structures.graphs.adjacency_matrix_undirected_with_weight import (
    MyAdjMatrUnDirWeightedGraph,
)
from dsa.structures.graphs.minimum_spanning_tree.mst import MST

Visitor = namedtuple("Visitor", ["position", "parent"])


def find_mst(graph: MyAdjMatrUnDirWeightedGraph) -> MST:
    visited = [False] * graph.size
    parents = [-1] * graph.size
    weights = [None] * graph.size
    to_visit: list[Visitor] = []
    heappush(to_visit, (0, Visitor(position=0, parent=-1)))

    while len(to_visit) > 0:
        weight, visitor = heappop(to_visit)
        if not visited[visitor.position]:
            visited[visitor.position] = True
            if not weights[visitor.position] or weights[visitor.position] > weight:
                weights[visitor.position] = weight
                parents[visitor.position] = visitor.parent

                for neighbor in graph.get_neighbors(visitor.position):
                    if not visited[neighbor.position]:
                        heappush(to_visit, (
                            neighbor.weight,
                            Visitor(
                                position=neighbor.position,
                                parent=visitor.position),
                        ))
    return MST(parents=parents, weights=weights)


def test_prim_mst():
    graph = MyAdjMatrUnDirWeightedGraph(6)

    (
        graph
        .add_edge(0, 1, 1)
        .add_edge(0, 2, 8)
        .add_edge(0, 4, 6)
        .add_edge(1, 3, 2)
        .add_edge(2, 3, 4)
        .add_edge(2, 4, 5)
        .add_edge(3, 5, 3)
        .add_edge(4, 5, 9)
    )

    mst = find_mst(graph)
    assert mst.parents == [-1, 0, 3, 1, 2, 3]
    assert mst.weights == [0, 1, 4, 2, 5, 3]


def test_w3s_example():
    graph = MyAdjMatrUnDirWeightedGraph(8)

    (
        graph
        .add_edge(0, 1, 4)
        .add_edge(0, 3, 3)
        .add_edge(1, 2, 3)
        .add_edge(1, 3, 5)
        .add_edge(1, 4, 6)
        .add_edge(2, 4, 4)
        .add_edge(2, 7, 2)
        .add_edge(3, 4, 7)
        .add_edge(3, 5, 4)
        .add_edge(4, 5, 5)
        .add_edge(4, 6, 3)
        .add_edge(5, 6, 7)
        .add_edge(6, 7, 5)
    )

    mst = find_mst(graph)
    assert mst.parents == [-1, 0, 1, 0, 2, 3, 4, 2]
    assert mst.weights == [0, 4, 3, 3, 4, 4, 3, 2]