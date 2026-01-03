from __future__ import annotations
from typing import Any, Dict, List, Optional, Protocol, Tuple
import heapq


class GraphLike(Protocol):
    def vertices(self) -> List[Any]:
        ...

    def neighbors(self, u: Any) -> List[Tuple[Any, float]]:
        ...


def bfs(graph: GraphLike, start: Any) -> Tuple[List[Any], List[str]]:
   
    visited = set()
    order: List[Any] = []
    steps: List[str] = []

    queue: List[Any] = [start]
    steps.append(f"INIT queue={queue}")

    while queue:
        u = queue.pop(0)
        steps.append(f"DEQUEUE {u}")

        if u in visited:
            steps.append(f"SKIP {u} (already visited)")
            continue

        visited.add(u)
        order.append(u)
        steps.append(f"VISIT {u}")

        nbrs = sorted(graph.neighbors(u), key=lambda x: str(x[0]))
        for v, _w in nbrs:
            if v not in visited:
                queue.append(v)
                steps.append(f"ENQUEUE {v} (from {u})")

    return order, steps


def dfs(graph: GraphLike, start: Any) -> Tuple[List[Any], List[str]]:
    
    visited = set()
    order: List[Any] = []
    steps: List[str] = []

    stack: List[Any] = [start]
    steps.append(f"INIT stack={stack}")

    while stack:
        u = stack.pop()
        steps.append(f"POP {u}")

        if u in visited:
            steps.append(f"SKIP {u} (already visited)")
            continue

        visited.add(u)
        order.append(u)
        steps.append(f"VISIT {u}")

        # Push neighbors in reverse sorted order so the smallest comes out first
        nbrs = sorted(graph.neighbors(u), key=lambda x: str(x[0]), reverse=True)
        for v, _w in nbrs:
            if v not in visited:
                stack.append(v)
                steps.append(f"PUSH {v} (from {u})")

    return order, steps


def dijkstra_shortest_path(graph: GraphLike, start: Any, goal: Any) -> Tuple[List[Any], float, List[str]]:
    
    steps: List[str] = []
    dist: Dict[Any, float] = {v: float("inf") for v in graph.vertices()}
    prev: Dict[Any, Optional[Any]] = {v: None for v in graph.vertices()}

    dist[start] = 0.0
    pq: List[Tuple[float, Any]] = [(0.0, start)]
    steps.append(f"INIT dist[{start}]=0, push({start})")

    visited = set()

    while pq:
        cur_dist, u = heapq.heappop(pq)
        steps.append(f"POP ({u}, dist={cur_dist})")

        if u in visited:
            steps.append(f"SKIP {u} (already finalized)")
            continue
        visited.add(u)

        if u == goal:
            steps.append(f"REACHED goal {goal}")
            break

        for v, w in graph.neighbors(u):
            if w < 0:
                raise ValueError("Negative edge weight found; Dijkstra not valid.")
            if v in visited:
                continue
            alt = cur_dist + w
            if alt < dist.get(v, float("inf")):
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))
                steps.append(f"RELAX {u}->{v} w={w}: dist[{v}]={alt}, prev[{v}]={u}")

    # Reconstruct path
    if dist.get(goal, float("inf")) == float("inf"):
        steps.append("NO PATH found")
        return [], float("inf"), steps

    path: List[Any] = []
    cur: Optional[Any] = goal
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    steps.append(f"PATH={path}, COST={dist[goal]}")
    return path, dist[goal], steps
