from with_iterable_subgraph import GraphWithIterableSubGraph


class MyNaivePath:
    @staticmethod
    def get_naive_distances(graph: GraphWithIterableSubGraph, start) -> list:
        """Infinite! loop in case of negative weight cycles"""
        distances = [float("inf")] * graph.get_size()
        distances[start] = 0
        to_visit = [start]

        while len(to_visit) > 0:
            current = to_visit.pop()
            for target, weight in graph.get_iterable_subgraph(current):
                if weight:
                    distance = distances[current] + weight
                    if distance < distances[target]:
                        distances[target] = distance
                        to_visit.append(target)

        return distances
