from dsa.structures.graphs.maximum_flow.mf_graph import MatrixGraph, Vertex


def edmonds_karp(graph: MatrixGraph, source, sink):
    parents = [-1] * graph.size
    max_flow = 0

    while graph.bfs(source, sink, parents):
        path_flow = float("Inf")
        vertex_ind = sink
        while vertex_ind != source:
            path_flow = min(path_flow, graph.adj_matrix[parents[vertex_ind]][vertex_ind])
            vertex_ind = parents[vertex_ind]

        max_flow += path_flow
        vertex_ind = sink
        while vertex_ind != source:
            parent = parents[vertex_ind]
            graph.adj_matrix[parent][vertex_ind] -= path_flow
            graph.adj_matrix[vertex_ind][parent] += path_flow
            vertex_ind = parents[vertex_ind]

        path = []
        vertex_ind = sink
        while vertex_ind != source:
            path.append(vertex_ind)
            vertex_ind = parents[vertex_ind]
        path.append(source)
        path.reverse()
        path_names = [graph.vertexes[node].name for node in path]
        print("Path:", " -> ".join(path_names), ", Flow:", path_flow)  # noqa: T201

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

    max_flow = edmonds_karp(g, 0, 3)
    print(f"Max flow = {max_flow}")  # noqa: T201
    assert max_flow == 9  # noqa: PLR2004
