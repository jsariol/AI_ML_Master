from typing import Any, Iterator, Tuple, Optional
from .bst import BinarySearchTree


class BSTMap:
    def __init__(self) -> None:
        self._bst = BinarySearchTree()

    def __len__(self) -> int:
        return len(self._bst)

    def set(self, key: Any, value: Any) -> None:
        self._bst.insert(key, value)

    def get(self, key: Any, default: Any = None) -> Any:
        node = self._bst.search(key)
        return node.value if node is not None else default

    def contains(self, key: Any) -> bool:
        return self._bst.search(key) is not None

    def delete(self, key: Any) -> bool:
        return self._bst.delete(key)

    def min_item(self) -> Optional[Tuple[Any, Any]]:
        return self._bst.min_item()

    def max_item(self) -> Optional[Tuple[Any, Any]]:
        return self._bst.max_item()

    def items_inorder(self) -> Iterator[Tuple[Any, Any]]:
        yield from self._bst.inorder()

    def items_preorder(self) -> Iterator[Tuple[Any, Any]]:
        yield from self._bst.preorder()

    def items_postorder(self) -> Iterator[Tuple[Any, Any]]:
        yield from self._bst.postorder()

    def is_balanced(self) -> bool:
        return self._bst.is_balanced()

    def ascii_tree(self) -> str:
        return self._bst.to_ascii()
