from dsa.structures.graphs.basic.with_iterable_subgraph import WithIterableSubGraph


class DijkstraShortestPath:
    @staticmethod
    def get_all_distances(graph: WithIterableSubGraph, start) -> list:
        distances = [float("inf")] * graph.get_size()
        distances[start] = 0
        to_visit = [start]

        while len(to_visit) > 0:
            current = to_visit.pop()
            for target, weight in graph.get_iterable_subgraph(current):
                if weight and weight > 0:
                    distance = distances[current] + weight
                    if distance < distances[target]:
                        distances[target] = distance
                        to_visit.append(target)

        return distances

    @staticmethod
    def get_path(
        graph: WithIterableSubGraph, start_vertex, target_vertex
    ) -> tuple[int | float, list]:
        distances, predecessors = (
            DijkstraShortestPath._dijkstra_distances_and_predecessors(graph, start_vertex)
        )
        distance = distances[target_vertex]

        if distance == float("inf"):
            return float("inf"), []

        return distance, DijkstraShortestPath._prepare_path(predecessors, target_vertex)

    @staticmethod
    def _dijkstra_distances_and_predecessors(
        graph: WithIterableSubGraph, start_vertex
    ) -> tuple[list, list]:
        distances = [float("inf")] * graph.get_size()
        distances[start_vertex] = 0
        predecessors = [None for _ in range(graph.get_size())]

        to_visit = [start_vertex]
        while len(to_visit) > 0:
            current = to_visit.pop()
            for target, weight in graph.get_iterable_subgraph(current):
                if weight and weight > 0:
                    distance = distances[current] + weight
                    if distance < distances[target]:
                        distances[target] = distance
                        predecessors[target] = current
                        to_visit.append(target)

        return distances, predecessors

    @staticmethod
    def _prepare_path(predecessors, target_vertex):
        predecessor = target_vertex
        path = []
        while predecessor:
            path.append(predecessor)
            predecessor = predecessors[predecessor]
        return list(reversed(path))
