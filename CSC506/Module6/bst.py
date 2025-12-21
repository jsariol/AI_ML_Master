# bst.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Generator, Optional, Tuple, List


@dataclass
class BSTNode:
    key: Any
    value: Any = None
    left: Optional["BSTNode"] = None
    right: Optional["BSTNode"] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    
    # Core operations    
    def insert(self, key: Any, value: Any = None) -> None:
        """Insert (key, value). If key exists, overwrite value."""
        if self.root is None:
            self.root = BSTNode(key, value)
            self._size = 1
            return

        cur = self.root
        while True:
            if key == cur.key:
                cur.value = value
                return
            elif key < cur.key:
                if cur.left is None:
                    cur.left = BSTNode(key, value)
                    self._size += 1
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = BSTNode(key, value)
                    self._size += 1
                    return
                cur = cur.right

    def search(self, key: Any) -> Optional[BSTNode]:
        """Return the node with matching key, or None."""
        cur = self.root
        while cur is not None:
            if key == cur.key:
                return cur
            cur = cur.left if key < cur.key else cur.right
        return None

    def delete(self, key: Any) -> bool:
        """Delete by key. Returns True if deleted, False if not found."""
        self.root, deleted = self._delete_recursive(self.root, key)
        if deleted:
            self._size -= 1
        return deleted

    def _delete_recursive(self, node: Optional[BSTNode], key: Any) -> Tuple[Optional[BSTNode], bool]:
        if node is None:
            return None, False

        if key < node.key:
            node.left, deleted = self._delete_recursive(node.left, key)
            return node, deleted
        elif key > node.key:
            node.right, deleted = self._delete_recursive(node.right, key)
            return node, deleted

        # node.key == key => delete this node
        if node.left is None and node.right is None:
            return None, True
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True

        # Two children: replace with inorder successor (min in right subtree)
        successor = self._min_node(node.right)
        node.key, node.value = successor.key, successor.value
        node.right, _ = self._delete_recursive(node.right, successor.key)
        return node, True

    
    # Min / Max    
    def min_item(self) -> Optional[Tuple[Any, Any]]:
        """Return (min_key, value) or None."""
        if self.root is None:
            return None
        n = self._min_node(self.root)
        return n.key, n.value

    def max_item(self) -> Optional[Tuple[Any, Any]]:
        """Return (max_key, value) or None."""
        if self.root is None:
            return None
        n = self._max_node(self.root)
        return n.key, n.value

    def _min_node(self, node: BSTNode) -> BSTNode:
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur

    def _max_node(self, node: BSTNode) -> BSTNode:
        cur = node
        while cur.right is not None:
            cur = cur.right
        return cur

    
    # Traversals (yield)    
    def inorder(self) -> Generator[Tuple[Any, Any], None, None]:
        yield from self._inorder(self.root)

    def _inorder(self, node: Optional[BSTNode]) -> Generator[Tuple[Any, Any], None, None]:
        if node is None:
            return
        yield from self._inorder(node.left)
        yield (node.key, node.value)
        yield from self._inorder(node.right)

    def preorder(self) -> Generator[Tuple[Any, Any], None, None]:
        yield from self._preorder(self.root)

    def _preorder(self, node: Optional[BSTNode]) -> Generator[Tuple[Any, Any], None, None]:
        if node is None:
            return
        yield (node.key, node.value)
        yield from self._preorder(node.left)
        yield from self._preorder(node.right)

    def postorder(self) -> Generator[Tuple[Any, Any], None, None]:
        yield from self._postorder(self.root)

    def _postorder(self, node: Optional[BSTNode]) -> Generator[Tuple[Any, Any], None, None]:
        if node is None:
            return
        yield from self._postorder(node.left)
        yield from self._postorder(node.right)
        yield (node.key, node.value)

    
    # Balance detection    
    def height(self) -> int:
        """Height of the tree. Empty tree => -1. Single node => 0."""
        return self._height(self.root)

    def _height(self, node: Optional[BSTNode]) -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def is_balanced(self) -> bool:
        """Detect if the tree is height-balanced (AVL-like condition)."""
        balanced, _ = self._check_balance(self.root)
        return balanced

    def _check_balance(self, node: Optional[BSTNode]) -> Tuple[bool, int]:
        """
        Returns (is_balanced, height).
        Height of empty node => -1.
        """
        if node is None:
            return True, -1

        left_bal, left_h = self._check_balance(node.left)
        if not left_bal:
            return False, 0

        right_bal, right_h = self._check_balance(node.right)
        if not right_bal:
            return False, 0

        if abs(left_h - right_h) > 1:
            return False, 0

        return True, 1 + max(left_h, right_h)

    
    # Visual representation (ASCII)    
    def to_ascii(self) -> str:
        """Return a sideways ASCII representation of the tree."""
        lines: List[str] = []
        self._build_ascii(self.root, lines, level=0, label="ROOT")
        return "\n".join(lines) if lines else "(empty tree)"

    def _build_ascii(self, node: Optional[BSTNode], lines: List[str], level: int, label: str) -> None:
        if node is None:
            return
        # Print right subtree first so it appears on top
        self._build_ascii(node.right, lines, level + 1, "R")
        lines.append("    " * level + f"{label}: {node.key}")
        self._build_ascii(node.left, lines, level + 1, "L")
