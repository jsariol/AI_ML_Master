
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple


@dataclass
class Entry:
    key: str
    value: Any


class HashTable:    

    def __init__(self, capacity: int = 211) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.capacity = capacity
        self.buckets: List[List[Entry]] = [[] for _ in range(capacity)]
        self.size = 0

    def _hash(self, key: str) -> int:
        
        if not isinstance(key, str):
            raise TypeError("HashTable supports string keys only for this assignment.")

        base = 31
        h = 0
        for ch in key:
            h = (h * base + ord(ch)) % self.capacity
        return h

    def insert(self, key: str, value: Any) -> None:
        """Insert or update a key-value pair."""
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return

        bucket.append(Entry(key, value))
        self.size += 1

    def search(self, key: str) -> Optional[Any]:
        """Return the value if found; otherwise None."""
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for entry in bucket:
            if entry.key == key:
                return entry.value
        return None

    def delete(self, key: str) -> bool:
        """Delete a key if present. Return True if deleted, False otherwise."""
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, entry in enumerate(bucket):
            if entry.key == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def __len__(self) -> int:
        return self.size

    def debug_bucket_sizes(self) -> List[int]:
        """Useful to show collision distribution across buckets."""
        return [len(b) for b in self.buckets]
