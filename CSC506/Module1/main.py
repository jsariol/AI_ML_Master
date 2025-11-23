from typing import Any

from data_structures import Stack, Queue, LinkedList
from complexity_analyzer import format_complexity


def prompt_value() -> Any:    
    return input("Enter value: ")


def handle_stack(stack: Stack) -> None:    
    while True:
        print("\n=== STACK MENU (LIFO) ===")
        print("1. Push (insert)")
        print("2. Pop (delete from top)")
        print("3. Peek (view top element)")
        print("4. Search")
        print("5. Show stack")
        print("6. Clear stack")
        print("0. Back to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            value = prompt_value()
            stack.push(value)
            print("\nCurrent stack:")
            print(stack)
            print()
            print(format_complexity("stack", "push"))

        elif choice == "2":
            try:
                popped = stack.pop()
                print(f"\nPopped value: {popped}")
            except IndexError as e:
                print(f"\nError: {e}")
            print("Current stack:")
            print(stack)
            print()
            print(format_complexity("stack", "pop"))

        elif choice == "3":
            try:
                top = stack.peek()
                print(f"\nTop value: {top}")
            except IndexError as e:
                print(f"\nError: {e}")
            print("Current stack:")
            print(stack)
            print()
            print(format_complexity("stack", "peek"))

        elif choice == "4":
            value = prompt_value()
            # Simple linear search using Python's "in"
            found = value in stack._data  # for demo purposes only
            print(f"\nSearch result: {'FOUND' if found else 'NOT FOUND'}")
            print("Current stack:")
            print(stack)
            print()
            print(format_complexity("stack", "search"))

        elif choice == "5":
            print("\nCurrent stack:")
            print(stack)

        elif choice == "6":
            stack.clear()
            print("\nStack cleared.")
            print(stack)

        elif choice == "0":
            break
        else:
            print("\nInvalid option. Please try again.")


def handle_queue(queue: Queue) -> None:
    """
    Menu for queue operations.
    """
    while True:
        print("\n=== QUEUE MENU (FIFO) ===")
        print("1. Enqueue (insert)")
        print("2. Dequeue (delete from front)")
        print("3. Peek (view front element)")
        print("4. Search")
        print("5. Show queue")
        print("6. Clear queue")
        print("0. Back to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            value = prompt_value()
            queue.enqueue(value)
            print("\nCurrent queue:")
            print(queue)
            print()
            print(format_complexity("queue", "enqueue"))

        elif choice == "2":
            try:
                removed = queue.dequeue()
                print(f"\nDequeued value: {removed}")
            except IndexError as e:
                print(f"\nError: {e}")
            print("Current queue:")
            print(queue)
            print()
            print(format_complexity("queue", "dequeue"))

        elif choice == "3":
            try:
                front = queue.peek()
                print(f"\nFront value: {front}")
            except IndexError as e:
                print(f"\nError: {e}")
            print("Current queue:")
            print(queue)
            print()
            print(format_complexity("queue", "peek"))

        elif choice == "4":
            value = prompt_value()
            found = value in queue._data  
            print(f"\nSearch result: {'FOUND' if found else 'NOT FOUND'}")
            print("Current queue:")
            print(queue)
            print()
            print(format_complexity("queue", "search"))

        elif choice == "5":
            print("\nCurrent queue:")
            print(queue)

        elif choice == "6":
            queue.clear()
            print("\nQueue cleared.")
            print(queue)

        elif choice == "0":
            break
        else:
            print("\nInvalid option. Please try again.")


def handle_linked_list(ll: LinkedList) -> None:
    """
    Menu for linked list operations.
    """
    while True:
        print("\n=== LINKED LIST MENU ===")
        print("1. Insert at head")
        print("2. Append at tail")
        print("3. Delete by value")
        print("4. Search by value")
        print("5. Show linked list")
        print("6. Clear linked list")
        print("0. Back to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            value = prompt_value()
            ll.insert_at_head(value)
            print("\nCurrent linked list:")
            print(ll)
            print()
            print(format_complexity("linked_list", "insert_at_head"))

        elif choice == "2":
            value = prompt_value()
            ll.append(value)
            print("\nCurrent linked list:")
            print(ll)
            print()
            print(format_complexity("linked_list", "append"))

        elif choice == "3":
            value = prompt_value()
            deleted = ll.delete(value)
            print(f"\nDelete result: {'DELETED' if deleted else 'NOT FOUND'}")
            print("Current linked list:")
            print(ll)
            print()
            print(format_complexity("linked_list", "delete"))

        elif choice == "4":
            value = prompt_value()
            node = ll.search(value)
            print(f"\nSearch result: {'FOUND' if node else 'NOT FOUND'}")
            print("Current linked list:")
            print(ll)
            print()
            print(format_complexity("linked_list", "search"))

        elif choice == "5":
            print("\nCurrent linked list:")
            print(ll)

        elif choice == "6":
            ll.clear()
            print("\nLinked list cleared.")
            print(ll)

        elif choice == "0":
            break
        else:
            print("\nInvalid option. Please try again.")


def main() -> None:    
    stack = Stack()
    queue = Queue()
    linked_list = LinkedList()

    while True:
        print("\n=== DATA STRUCTURE LEARNING TOOL ===")
        print("1. Work with Stack")
        print("2. Work with Queue")
        print("3. Work with Linked List")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            handle_stack(stack)
        elif choice == "2":
            handle_queue(queue)
        elif choice == "3":
            handle_linked_list(linked_list)
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()
