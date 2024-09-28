from heapq import heappop, heappush

from with_iterable_subgraph import GraphWithIterableSubGraph


class DijkstraShortestPath:

    @staticmethod
    def get_all_distances_optimized(graph: GraphWithIterableSubGraph, start) -> list:
        """Does fewer loop iterations compared to get_all_distances()"""
        distances = [float("inf")] * graph.get_size()
        distances[start] = 0
        to_visit: list[tuple[int, int]] = []
        visited = [False] * graph.get_size()

        heappush(to_visit, (0, start))

        while len(to_visit) > 0:
            distance, current = heappop(to_visit)
            if visited[current]:
                continue

            for target, weight in graph.get_iterable_subgraph(current):
                if weight and weight > 0:
                    new_distance = distance + weight
                    if new_distance < distances[target]:
                        distances[target] = new_distance
                        heappush(to_visit, (new_distance, target))

            visited[current] = True

        return distances

    @staticmethod
    def get_path(
        graph: GraphWithIterableSubGraph, start_vertex, target_vertex
    ) -> tuple[int | float, list]:
        distance, predecessors = (
            DijkstraShortestPath._dijkstra_distances_and_predecessors(
                graph, start_vertex, target_vertex
            )
        )

        return DijkstraShortestPath._prepare_path_response(
            distance, predecessors, target_vertex
        )

    @staticmethod
    def _prepare_path_response(distance, predecessors, target_vertex):
        if distance == float("inf"):
            return float("inf"), []
        return distance, DijkstraShortestPath._prepare_path(predecessors, target_vertex)

    @staticmethod
    def _dijkstra_distances_and_predecessors(
        graph: GraphWithIterableSubGraph, start_vertex, target_vertex
    ) -> tuple[int | float, list]:
        distances = [float("inf")] * graph.get_size()
        distances[start_vertex] = 0
        predecessors = [None for _ in range(graph.get_size())]
        visited = [False for _ in range(graph.get_size())]
        to_visit: list[tuple[int:int]] = [(0, start_vertex)]

        while len(to_visit) > 0:
            distance, current = heappop(to_visit)
            visited[current] = True

            for target, weight in graph.get_iterable_subgraph(current):
                if weight:
                    next_distance = distance + weight

                    if not visited[target] and next_distance < distances[target]:
                        distances[target] = next_distance
                        predecessors[target] = current
                        heappush(to_visit, (next_distance, target))

        return distances[target_vertex], predecessors

    @staticmethod
    def _prepare_path(predecessors, target_vertex) -> list:
        predecessor = target_vertex
        path = []
        while predecessor:
            path.append(predecessor)
            predecessor = predecessors[predecessor]
        return list(reversed(path))

    @staticmethod
    def get_narrowed_path(
        graph: GraphWithIterableSubGraph, start_vertex, target_vertex,
    ) -> tuple[int | float, list]:
        """Unlike get_path() this method will stop looking if target is reached."""
        distance, predecessors = (
            DijkstraShortestPath._narrowed_dijkstra_distances_and_predecessors(
                graph,
                start_vertex,
                target_vertex,
            )
        )

        return DijkstraShortestPath._prepare_path_response(
            distance,
            predecessors,
            target_vertex,
        )

    @staticmethod
    def _narrowed_dijkstra_distances_and_predecessors(
        graph,
        start_vertex,
        target_vertex,
    ) -> tuple[int | float, list]:
        distances = [float("inf")] * graph.get_size()
        distances[start_vertex] = 0
        predecessors = [None for _ in range(graph.get_size())]
        visited = [False for _ in range(graph.get_size())]
        to_visit: list[tuple[int:int]] = [(0, start_vertex)]

        while len(to_visit) > 0:
            distance, current = heappop(to_visit)
            visited[current] = True

            for target, weight in graph.get_iterable_subgraph(current):
                if weight:
                    next_distance = distance + weight

                    if not visited[target] and next_distance < distances[target]:
                        distances[target] = next_distance
                        predecessors[target] = current
                        if target == target_vertex:
                            break
                        heappush(to_visit, (next_distance, target))

        return distances[target_vertex], predecessors
