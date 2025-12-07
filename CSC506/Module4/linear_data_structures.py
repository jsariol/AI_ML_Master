# --------------------------
# Stack implementation
# --------------------------

class Stack:
    """Simple stack implementation using a Python list (LIFO)."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if the stack has no elements."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def __repr__(self):
        return f"Stack({self.items})"


# --------------------------
# Queue implementation
# --------------------------

class Queue:
    """Simple queue implementation using a Python list (FIFO)."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if the queue has no elements."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item of the queue.
        Raises IndexError if the queue is empty.        
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        """
        Return the front item without removing it.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]

    def __repr__(self):
        return f"Queue({self.items})"


# --------------------------
# Deque implementation
# --------------------------

class Deque:
    """Double-ended queue implementation using a Python list."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if the deque has no elements."""
        return len(self.items) == 0

    def add_front(self, item):
        """Insert an item at the front of the deque."""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Insert an item at the rear of the deque."""
        self.items.append(item)

    def remove_front(self):
        """
        Remove and return the front item.
        Raises IndexError if the deque is empty.
        """
        if self.is_empty():
            raise IndexError("remove_front from empty deque")
        return self.items.pop(0)

    def remove_rear(self):
        """
        Remove and return the rear item.
        Raises IndexError if the deque is empty.
        """
        if self.is_empty():
            raise IndexError("remove_rear from empty deque")
        return self.items.pop()

    def __repr__(self):
        return f"Deque({self.items})"


# --------------------------
# LinkedList implementation
# --------------------------

class Node:
    """Node for a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Singly linked list with basic operations:
    insert, delete, search, and display.
    """

    def __init__(self):
        self.head = None

    def insert(self, data):
        """
        Insert a new node at the end of the list.
        Time complexity: O(n).
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, data):
        """
        Delete the first node with the given data.
        Raises ValueError if the data is not found.
        """
        if self.head is None:
            raise ValueError("Cannot delete from an empty list")
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        prev = self.head
        current = self.head.next
        while current is not None and current.data != data:
            prev = current
            current = current.next

        if current is None:
            raise ValueError(f"Value {data} not found in list")

        prev.next = current.next

    def search(self, data):
        """
        Search for the first node with the given data.
        Return True if found, False otherwise.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """Return a Python list with all node values."""
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        return elements

    def __repr__(self):
        return f"LinkedList({self.display()})"


# --------------------------
# Algorithms using the data structures
# --------------------------

def is_parentheses_balanced(expression):
    """
    Example use-case of a Stack:
    Check if parentheses in an expression are balanced.
    """
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if pairs[char] != top:
                return False

    return stack.is_empty()


def simulate_print_queue(jobs):
    """
    Example use-case of a Queue:
    Process print jobs in FIFO order.
    'jobs' is a list of strings representing job names.
    """
    q = Queue()
    for job in jobs:
        q.enqueue(job)

    processed = []
    while not q.is_empty():
        current_job = q.dequeue()        
        processed.append(current_job)

    return processed


def is_palindrome_using_deque(text):
    """
    Example use-case of a Deque:
    Check if a string is a palindrome, ignoring spaces and case.
    """
    d = Deque()
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

    for ch in cleaned:
        d.add_rear(ch)

    while len(d.items) > 1:
        front = d.remove_front()
        rear = d.remove_rear()
        if front != rear:
            return False
    return True


def demo_linked_list_contacts():
    """
    Example use-case of a LinkedList:
    Maintain a simple list of contact names.
    """
    contacts = LinkedList()
    contacts.insert("Alice")
    contacts.insert("Bob")
    contacts.insert("Carol")

    # Delete one contact and search for another
    contacts.delete("Bob")
    found_alice = contacts.search("Alice")
    found_bob = contacts.search("Bob")

    return contacts.display(), found_alice, found_bob


# --------------------------
# Simple test program
# --------------------------

if __name__ == "__main__":
    # Stack demo
    expr = "((2 + 3) * [5 - 1])"
    print("Expression:", expr)
    print("Balanced parentheses?", is_parentheses_balanced(expr))

    # Queue demo
    jobs = ["Job1", "Job2", "Job3"]
    print("\nPrint queue input:", jobs)
    print("Processed order:", simulate_print_queue(jobs))

    # Deque demo
    text = "A man a plan a canal Panama"
    print("\nText:", text)
    print("Is palindrome?", is_palindrome_using_deque(text))

    # LinkedList demo
    contacts_list, has_alice, has_bob = demo_linked_list_contacts()
    print("\nContacts after operations:", contacts_list)
    print("Alice found?", has_alice)
    print("Bob found?", has_bob)
