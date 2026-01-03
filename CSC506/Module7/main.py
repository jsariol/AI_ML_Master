from graph_matrix import GraphMatrix
from graph_list import GraphList
from graph_algorithms import bfs, dfs, dijkstra_shortest_path


def build_sample_graph(g) -> None:
    
    edges = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2),
        ("D", "F", 6),
        ("E", "F", 3),
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)


def run_demo(name: str, g) -> None:
    print(f"\n==============================")
    print(f"DEMO: {name}")
    print(f"==============================")

    print("\nGraph connections:")
    print(g.display_connections())

    # Matrix-only extra display
    if hasattr(g, "display_matrix"):
        print("\nAdjacency matrix:")
        print(g.display_matrix())

    start = "A"

    order_bfs, steps_bfs = bfs(g, start)
    print("\nBFS order:", order_bfs)
    print("BFS steps (first 12):")
    for s in steps_bfs[:12]:
        print("  -", s)

    order_dfs, steps_dfs = dfs(g, start)
    print("\nDFS order:", order_dfs)
    print("DFS steps (first 12):")
    for s in steps_dfs[:12]:
        print("  -", s)

    path, cost, steps_sp = dijkstra_shortest_path(g, "A", "F")
    print("\nShortest path A -> F:", path, "| cost=", cost)
    print("Dijkstra steps (first 12):")
    for s in steps_sp[:12]:
        print("  -", s)

    # Manipulation demo: remove edge and show impact
    print("\nRemove edge D-E and re-run shortest path A->F:")
    g.remove_edge("D", "E")
    path2, cost2, _ = dijkstra_shortest_path(g, "A", "F")
    print("Shortest path A -> F:", path2, "| cost=", cost2)


def main() -> None:
    gm = GraphMatrix(directed=False)
    gl = GraphList(directed=False)

    build_sample_graph(gm)
    build_sample_graph(gl)

    run_demo("Adjacency Matrix Graph", gm)
    run_demo("Adjacency List Graph", gl)

    # Vertex add/remove demo
    print("\n=== Vertex manipulation demo (List) ===")
    gl.add_vertex("Z")
    print("Added vertex Z. Has Z?", gl.has_vertex("Z"))
    gl.remove_vertex("Z")
    print("Removed vertex Z. Has Z?", gl.has_vertex("Z"))


if __name__ == "__main__":
    main()
