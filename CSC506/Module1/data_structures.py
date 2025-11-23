from __future__ import annotations
from collections import deque
from typing import Any, Optional, Iterable


class Stack:
    
    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        self._data: list[Any] = []
        if items is not None:
            for item in items:
                self.push(item)

    def push(self, item: Any) -> None:
        """Push an item onto the top of the stack"""
        self._data.append(item)

    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.
        Raises:
            IndexError: if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any:
        """
        Return the top item without removing it.

        Raises:
            IndexError: if the stack is empty.        
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no elements."""
        return len(self._data) == 0

    def size(self) -> int:
        """Return the number of elements in the stack."""
        return len(self._data)

    def clear(self) -> None:
        """Remove all elements from the stack."""
        self._data.clear()

    def __len__(self) -> int:
        return self.size()

    def __repr__(self) -> str:
        return f"Stack({self._data!r})"

    def __str__(self) -> str:
        """
        Visual representation.

        Example:
            [bottom] 1 <- 2 <- 3 [top]
        """
        if self.is_empty():
            return "[empty stack]"
        items = " <- ".join(repr(x) for x in self._data)
        return f"[bottom] {items} [top]"


class Queue:    

    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        self._data: deque[Any] = deque()
        if items is not None:
            for item in items:
                self.enqueue(item)

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the item from the front of the queue.

        Raises:
            IndexError: if the queue is empty.        
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Any:
        """
        Return the front item without removing it.

        Raises:
            IndexError: if the queue is empty.        
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[0]

    def is_empty(self) -> bool:
        """Return True if the queue has no elements."""
        return len(self._data) == 0

    def size(self) -> int:
        """Return the number of elements in the queue."""
        return len(self._data)

    def clear(self) -> None:
        """Remove all elements from the queue."""
        self._data.clear()

    def __len__(self) -> int:
        return self.size()

    def __repr__(self) -> str:
        return f"Queue({list(self._data)!r})"

    def __str__(self) -> str:
        """
        Visual representation.

        Example:
            [front] 1 <- 2 <- 3 [rear]
        """
        if self.is_empty():
            return "[empty queue]"
        items = " <- ".join(repr(x) for x in self._data)
        return f"[front] {items} [rear]"


class LinkedListNode:    

    def __init__(self, value: Any, next_node: Optional[LinkedListNode] = None) -> None:
        self.value: Any = value
        self.next: Optional[LinkedListNode] = next_node

    def __repr__(self) -> str:
        return f"LinkedListNode({self.value!r})"


class LinkedList:    

    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        self.head: Optional[LinkedListNode] = None
        self.tail: Optional[LinkedListNode] = None
        self._size: int = 0

        if items is not None:
            for item in items:
                self.append(item)

    def insert_at_head(self, value: Any) -> None:
        """
        Insert a new node at the beginning of the list.
        """
        new_node = LinkedListNode(value, self.head)
        self.head = new_node
        if self.tail is None:  # first element in the list
            self.tail = new_node
        self._size += 1

    def append(self, value: Any) -> None:
        """
        Insert a new node at the end of the list.
        """
        new_node = LinkedListNode(value)
        if self.tail is None:
            # List is empty; new node becomes both head and tail
            self.head = self.tail = new_node
        else:
            assert self.tail is not None  # for type checkers
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def search(self, value: Any) -> Optional[LinkedListNode]:
        """
        Search for the first node with the given value.

        Returns:
            The node if found, otherwise None.        
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value: Any) -> bool:
        """
        Delete the first node with the given value.

        Returns:
            True if a node was deleted, False otherwise.        
        """
        current = self.head
        prev: Optional[LinkedListNode] = None

        while current is not None:
            if current.value == value:
                # Node found: update links
                if prev is None:
                    # Deleting the head
                    self.head = current.next
                else:
                    prev.next = current.next

                if current is self.tail:
                    # Update tail if needed
                    self.tail = prev

                self._size -= 1
                return True

            prev = current
            current = current.next

        return False

    def to_list(self) -> list[Any]:
        """
        Convert the linked list into a regular Python list.        
        """
        result: list[Any] = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def is_empty(self) -> bool:
        """Return True if the list has no elements."""
        return self._size == 0

    def size(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def clear(self) -> None:
        """Remove all elements from the list."""
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self) -> int:
        return self.size()

    def __repr__(self) -> str:
        return f"LinkedList({self.to_list()!r})"

    def __str__(self) -> str:
        """
        Visual representation.

        Example:
            HEAD -> 1 -> 2 -> 3 -> NULL
        """
        if self.is_empty():
            return "HEAD -> NULL"
        values = " -> ".join(repr(x) for x in self.to_list())
        return f"HEAD -> {values} -> NULL"
