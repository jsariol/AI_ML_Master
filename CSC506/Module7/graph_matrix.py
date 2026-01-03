from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple


class GraphMatrix:
    def __init__(self, directed: bool = False) -> None:
        self.directed = directed
        self._index: Dict[Any, int] = {}        
        self._vertices: List[Any] = []          
        self._matrix: List[List[Optional[float]]] = []  

    def vertices(self) -> List[Any]:
        return list(self._vertices)

    def has_vertex(self, v: Any) -> bool:
        return v in self._index

    def add_vertex(self, v: Any) -> None:
        """Add a vertex if it does not exist."""
        if v in self._index:
            return
        idx = len(self._vertices)
        self._index[v] = idx
        self._vertices.append(v)

        # Expand existing rows
        for row in self._matrix:
            row.append(None)

        # Add new row
        self._matrix.append([None] * (idx + 1))

    def remove_vertex(self, v: Any) -> bool:
        """Remove a vertex and all incident edges."""
        if v not in self._index:
            return False

        idx = self._index[v]

        # Remove row
        self._matrix.pop(idx)

        # Remove column
        for row in self._matrix:
            row.pop(idx)

        # Remove from vertices list
        self._vertices.pop(idx)

        # Rebuild index map
        self._index.clear()
        for i, vert in enumerate(self._vertices):
            self._index[vert] = i

        return True

    def add_edge(self, u: Any, v: Any, weight: float = 1.0) -> None:
        
        if weight < 0:
            raise ValueError("Dijkstra requires non-negative weights.")
        self.add_vertex(u)
        self.add_vertex(v)
        i, j = self._index[u], self._index[v]
        self._matrix[i][j] = float(weight)
        if not self.directed:
            self._matrix[j][i] = float(weight)

    def remove_edge(self, u: Any, v: Any) -> bool:
        if u not in self._index or v not in self._index:
            return False
        i, j = self._index[u], self._index[v]
        existed = self._matrix[i][j] is not None
        self._matrix[i][j] = None
        if not self.directed:
            self._matrix[j][i] = None
        return existed

    def neighbors(self, u: Any) -> List[Tuple[Any, float]]:
        """Return neighbors of u as a list of (neighbor, weight)."""
        if u not in self._index:
            return []
        i = self._index[u]
        result: List[Tuple[Any, float]] = []
        for j, w in enumerate(self._matrix[i]):
            if w is not None:
                result.append((self._vertices[j], float(w)))
        return result

    def display_connections(self) -> str:
        """Readable connections list."""
        lines: List[str] = []
        for u in self._vertices:
            nbrs = self.neighbors(u)
            nbrs_sorted = sorted(nbrs, key=lambda x: str(x[0]))
            lines.append(f"{u} -> {nbrs_sorted}")
        return "\n".join(lines) if lines else "(empty graph)"

    def display_matrix(self) -> str:
        """Pretty print the adjacency matrix."""
        if not self._vertices:
            return "(empty matrix)"
        header = "     " + "  ".join(f"{str(v):>5}" for v in self._vertices)
        lines = [header]
        for i, u in enumerate(self._vertices):
            row_vals = []
            for w in self._matrix[i]:
                row_vals.append("  .  " if w is None else f"{w:5.0f}")
            lines.append(f"{str(u):>5} " + " ".join(row_vals))
        return "\n".join(lines)
