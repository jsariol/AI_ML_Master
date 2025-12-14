
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class PQItem:
    priority: int
    value: Any


class PriorityQueue:
   

    def __init__(self) -> None:
        self.heap: List[PQItem] = []

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i: int) -> None:
        while i > 0:
            p = self._parent(i)
            if self.heap[i].priority < self.heap[p].priority:
                self._swap(i, p)
                i = p
            else:
                break

    def _heapify_down(self, i: int) -> None:
        n = len(self.heap)
        while True:
            left = self._left(i)
            right = self._right(i)
            smallest = i

            if left < n and self.heap[left].priority < self.heap[smallest].priority:
                smallest = left
            if right < n and self.heap[right].priority < self.heap[smallest].priority:
                smallest = right

            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def insert(self, priority: int, value: Any) -> None:
        item = PQItem(priority, value)
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def peek(self) -> PQItem:
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self.heap[0]

    def extract_min(self) -> PQItem:
        if self.is_empty():
            raise IndexError("extract_min from empty priority queue")

        self._swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        if not self.is_empty():
            self._heapify_down(0)
        return item

    def search(self, value: Any) -> Optional[PQItem]:
        for item in self.heap:
            if item.value == value:
                return item
        return None

    def delete(self, value: Any) -> bool:
        
        n = len(self.heap)
        for i in range(n):
            if self.heap[i].value == value:
                self._swap(i, n - 1)
                self.heap.pop()
                if i < len(self.heap):
                    # Fix heap property from this index
                    self._heapify_down(i)
                    self._heapify_up(i)
                return True
        return False

    def __len__(self) -> int:
        return len(self.heap)
