from dsa.structures.graphs.maximum_flow.mf_graph import MatrixGraph, Vertex


def ford_fulkerson(graph: MatrixGraph, source, sink) -> int:
    max_flow = 0

    path = graph.dfs(source, sink)
    while path:
        path_flow = float("Inf")
        for i in range(len(path) - 1):
            left, right = path[i], path[i + 1]
            path_flow = min(path_flow, graph.adj_matrix[left][right])

        for i in range(len(path) - 1):
            left, right = path[i], path[i + 1]
            graph.adj_matrix[left][right] -= path_flow
            graph.adj_matrix[right][left] += path_flow

        max_flow += path_flow

        path_names = [graph.vertexes[node].name for node in path]
        print("Path:", " -> ".join(path_names), ", Flow:", path_flow)

        path = graph.dfs(source, sink)

    return max_flow


def test_small_graph():
    g = MatrixGraph(4)
    g.add_vertex_data(Vertex(0, "A"))
    g.add_vertex_data(Vertex(1, "B"))
    g.add_vertex_data(Vertex(2, "C"))
    g.add_vertex_data(Vertex(3, "D"))

    (
        g.add_edge(0, 1, 10)
        .add_edge(0, 2, 3)
        .add_edge(1, 2, 5)
        .add_edge(1, 3, 3)
        .add_edge(2, 3, 6)
    )

    max_flow = ford_fulkerson(g, 0, 3)
    print(f"Max flow = {max_flow}")
    assert max_flow == 9
