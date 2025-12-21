from typing import Any, List, Tuple


class ListMap:
    def __init__(self) -> None:
        self._items: List[Tuple[Any, Any]] = []

    def __len__(self) -> int:
        return len(self._items)

    def set(self, key: Any, value: Any) -> None:
        for i, (k, _) in enumerate(self._items):
            if k == key:
                self._items[i] = (key, value)
                return
        self._items.append((key, value))

    def get(self, key: Any, default: Any = None) -> Any:
        for k, v in self._items:
            if k == key:
                return v
        return default

    def contains(self, key: Any) -> bool:
        for k, _ in self._items:
            if k == key:
                return True
        return False

    def delete(self, key: Any) -> bool:
        for i, (k, _) in enumerate(self._items):
            if k == key:
                self._items.pop(i)
                return True
        return False
