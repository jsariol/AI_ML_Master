from __future__ import annotations
from typing import Any, Dict, List, Tuple


class GraphList:
    def __init__(self, directed: bool = False) -> None:
        self.directed = directed
        self._adj: Dict[Any, Dict[Any, float]] = {}  # u -> {v: weight}

    def vertices(self) -> List[Any]:
        return list(self._adj.keys())

    def has_vertex(self, v: Any) -> bool:
        return v in self._adj

    def add_vertex(self, v: Any) -> None:
        if v not in self._adj:
            self._adj[v] = {}

    def remove_vertex(self, v: Any) -> bool:
        if v not in self._adj:
            return False
        # Remove outgoing
        self._adj.pop(v)
        # Remove incoming references
        for u in self._adj:
            self._adj[u].pop(v, None)
        return True

    def add_edge(self, u: Any, v: Any, weight: float = 1.0) -> None:
        if weight < 0:
            raise ValueError("Dijkstra requires non-negative weights.")
        self.add_vertex(u)
        self.add_vertex(v)
        self._adj[u][v] = float(weight)
        if not self.directed:
            self._adj[v][u] = float(weight)

    def remove_edge(self, u: Any, v: Any) -> bool:
        if u not in self._adj or v not in self._adj:
            return False
        existed = v in self._adj[u]
        self._adj[u].pop(v, None)
        if not self.directed:
            self._adj[v].pop(u, None)
        return existed

    def neighbors(self, u: Any) -> List[Tuple[Any, float]]:
        if u not in self._adj:
            return []
        items = [(v, w) for v, w in self._adj[u].items()]
        return items

    def display_connections(self) -> str:
        lines: List[str] = []
        for u in sorted(self._adj.keys(), key=lambda x: str(x)):
            nbrs = sorted(self.neighbors(u), key=lambda x: str(x[0]))
            lines.append(f"{u} -> {nbrs}")
        return "\n".join(lines) if lines else "(empty graph)"
