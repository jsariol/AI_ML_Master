"""
Portfolio User Interface - Interactive Console Application
==========================================================

A comprehensive interactive console UI that allows users to test, compare,
and visualize all portfolio components including algorithms and data structures.

This provides an intuitive menu-driven interface for exploring the portfolio.
"""

import sys
import os
import time
import random
from typing import Optional

# Add parent directory to path for imports (CSC506 root)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Also add current directory for local imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from portfolio_system import PortfolioSystem

# Import individual modules for direct access
linear_search = None
binary_search = None
bubble_sort = None
selection_sort = None
insertion_sort = None
BubbleSortVisualizer = None
Stack = None
Queue = None
Deque = None
HashTable = None
BSTMap = None
ListMap = None
GraphList = None
Set = None
QuickSelectVisualizer = None

try:
    from Module2.linear_search import linear_search
except ImportError:
    print("Warning: Search algorithms not available")

try:
    from Module2.binary_search import binary_search
except ImportError:
    pass

try:
    from Module3.sorting_algorithms import bubble_sort, selection_sort, insertion_sort
except ImportError:
    print("Warning: Sorting algorithms not available")

try:
    from bubble_sort_visualization import BubbleSortVisualizer
except ImportError:
    pass

try:
    from Module4.linear_data_structures import Stack, Queue, Deque
except ImportError:
    print("Warning: Linear data structures not available")

try:
    from Module5.hash_table import HashTable
except ImportError:
    print("Warning: Hash table not available")

try:
    from Module6.bst_map import BSTMap
except ImportError:
    print("Warning: BST map not available")

try:
    from Module6.list_map import ListMap
except ImportError:
    pass

try:
    from Module7.graph_list import GraphList
except ImportError:
    print("Warning: Graph structures not available")

try:
    from set_operations import Set
except ImportError:
    print("Warning: Set operations not available")

try:
    from quickselect import QuickSelectVisualizer
except ImportError:
    print("Warning: Quickselect not available")


class PortfolioUI:
    """
    Interactive user interface for the portfolio system.
    
    Provides menus for testing algorithms, visualizing operations,
    and comparing performance metrics.
    """
    
    def __init__(self):
        """Initialize the portfolio UI."""
        self.portfolio = PortfolioSystem()
        self.running = True
    
    def clear_screen(self) -> None:
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_main_menu(self) -> None:
        """Display the main menu."""
        print("\n" + "=" * 80)
        print("PORTFOLIO PROJECT - MAIN MENU")
        print("=" * 80)
        print("\n1.  Search Algorithms")
        print("2.  Sorting Algorithms")
        print("3.  Selection Algorithms (Quickselect)")
        print("4.  Linear Data Structures (Stack, Queue, Deque)")
        print("5.  Tree Structures (BST, Maps)")
        print("6.  Hash Tables")
        print("7.  Set Operations")
        print("8.  Graph Structures")
        print("9.  Portfolio System Overview")
        print("10. Run All Demonstrations")
        print("11. Performance Comparison Tools")
        print("0.  Exit")
        print("\n" + "=" * 80)
    
    def search_menu(self) -> None:
        """Menu for search algorithms."""
        while True:
            print("\n" + "=" * 80)
            print("SEARCH ALGORITHMS")
            print("=" * 80)
            print("\n1. Linear Search Demo")
            print("2. Binary Search Demo")
            print("3. Compare Linear vs Binary")
            print("4. Back to Main Menu")
            print("0. Exit")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self._linear_search_demo()
            elif choice == "2":
                self._binary_search_demo()
            elif choice == "3":
                self._search_comparison()
            elif choice == "4":
                break
            elif choice == "0":
                self.running = False
                return
            else:
                print("Invalid choice. Try again.")
    
    def sorting_menu(self) -> None:
        """Menu for sorting algorithms."""
        while True:
            print("\n" + "=" * 80)
            print("SORTING ALGORITHMS")
            print("=" * 80)
            print("\n1. Bubble Sort with Visualization")
            print("2. Selection Sort")
            print("3. Insertion Sort")
            print("4. Compare All Sorting Algorithms")
            print("5. Back to Main Menu")
            print("0. Exit")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self._bubble_sort_demo()
            elif choice == "2":
                self._selection_sort_demo()
            elif choice == "3":
                self._insertion_sort_demo()
            elif choice == "4":
                self._sorting_comparison()
            elif choice == "5":
                break
            elif choice == "0":
                self.running = False
                return
            else:
                print("Invalid choice. Try again.")
    
    def selection_menu(self) -> None:
        """Menu for selection algorithms."""
        while True:
            print("\n" + "=" * 80)
            print("SELECTION ALGORITHMS")
            print("=" * 80)
            print("\n1. Quickselect Demo")
            print("2. Find kth Element Interactive")
            print("3. Compare Quickselect vs Sorting")
            print("4. Back to Main Menu")
            print("0. Exit")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self._quickselect_demo()
            elif choice == "2":
                self._quickselect_interactive()
            elif choice == "3":
                self._quickselect_comparison()
            elif choice == "4":
                break
            elif choice == "0":
                self.running = False
                return
            else:
                print("Invalid choice. Try again.")
    
    def linear_structures_menu(self) -> None:
        """Menu for linear data structures."""
        while True:
            print("\n" + "=" * 80)
            print("LINEAR DATA STRUCTURES")
            print("=" * 80)
            print("\n1. Stack Operations (LIFO)")
            print("2. Queue Operations (FIFO)")
            print("3. Deque Operations (Double-ended)")
            print("4. Back to Main Menu")
            print("0. Exit")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self._stack_demo()
            elif choice == "2":
                self._queue_demo()
            elif choice == "3":
                self._deque_demo()
            elif choice == "4":
                break
            elif choice == "0":
                self.running = False
                return
            else:
                print("Invalid choice. Try again.")
    
    def tree_structures_menu(self) -> None:
        """Menu for tree structures."""
        while True:
            print("\n" + "=" * 80)
            print("TREE STRUCTURES")
            print("=" * 80)
            print("\n1. Binary Search Tree Map")
            print("2. List Map (Linear)")
            print("3. Compare BST vs List Map")
            print("4. Back to Main Menu")
            print("0. Exit")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self._bst_map_demo()
            elif choice == "2":
                self._list_map_demo()
            elif choice == "3":
                self._tree_comparison()
            elif choice == "4":
                break
            elif choice == "0":
                self.running = False
                return
            else:
                print("Invalid choice. Try again.")
    
    def set_operations_menu(self) -> None:
        """Menu for set operations."""
        while True:
            print("\n" + "=" * 80)
            print("SET OPERATIONS")
            print("=" * 80)
            print("\n1. Set Operations Interactive Demo")
            print("2. Union, Intersection, Difference Examples")
            print("3. Symmetric Difference & Relationships")
            print("4. Back to Main Menu")
            print("0. Exit")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self._set_interactive()
            elif choice == "2":
                self._set_operations_demo()
            elif choice == "3":
                self._set_relationships()
            elif choice == "4":
                break
            elif choice == "0":
                self.running = False
                return
            else:
                print("Invalid choice. Try again.")
    
    def graph_menu(self) -> None:
        """Menu for graph structures."""
        while True:
            print("\n" + "=" * 80)
            print("GRAPH STRUCTURES")
            print("=" * 80)
            print("\n1. Graph Creation & Operations")
            print("2. Graph Traversal & Neighbors")
            print("3. Back to Main Menu")
            print("0. Exit")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self._graph_demo()
            elif choice == "2":
                self._graph_traversal()
            elif choice == "3":
                break
            elif choice == "0":
                self.running = False
                return
            else:
                print("Invalid choice. Try again.")
    
    # ========== DEMO IMPLEMENTATIONS ==========
    
    def _linear_search_demo(self) -> None:
        """Linear search demonstration."""
        if linear_search is None:
            print("Linear search not available. Check imports.")
            return
        print("\nLinear Search - Scans array sequentially")
        try:
            input_str = input("Enter integers (space-separated): ").strip()
            arr = list(map(int, input_str.split()))
            target = int(input("Enter target value: "))
            
            result = linear_search(arr, target)
            if result is not None:
                print(f"\n[FOUND] Found at index {result}")
            else:
                print(f"\n[NOT FOUND] Not found in array")
        except ValueError:
            print("Invalid input")
    
    def _binary_search_demo(self) -> None:
        """Binary search demonstration."""
        if binary_search is None:
            print("Binary search not available. Check imports.")
            return
        print("\nBinary Search - Requires sorted array")
        try:
            input_str = input("Enter integers (space-separated): ").strip()
            arr = sorted(list(map(int, input_str.split())))
            target = int(input("Enter target value: "))
            
            result = binary_search(arr, target)
            if result is not None:
                print(f"\n[FOUND] Found at index {result}")
            else:
                print(f"\n[NOT FOUND] Not found in array")
        except ValueError:
            print("Invalid input")
    
    def _search_comparison(self) -> None:
        """Compare search algorithms."""
        if linear_search is None or binary_search is None:
            print("Search algorithms not available. Check imports.")
            return
        print("\nSearch Comparison")
        size = int(input("Array size (default 1000): ") or "1000")
        arr = [random.randint(0, size * 10) for _ in range(size)]
        sorted_arr = sorted(arr)
        target = arr[size // 2]
        
        # Time linear search
        start = time.perf_counter()
        for _ in range(100):
            linear_search(arr, target)
        time_linear = time.perf_counter() - start
        
        # Time binary search
        start = time.perf_counter()
        for _ in range(100):
            binary_search(sorted_arr, target)
        time_binary = time.perf_counter() - start
        
        print(f"\nArray size: {size} (100 iterations)")
        print(f"Linear Search: {time_linear:.6f}s")
        print(f"Binary Search: {time_binary:.6f}s")
        print(f"Speedup: {time_linear/time_binary:.2f}x")
    
    def _bubble_sort_demo(self) -> None:
        """Bubble sort with visualization."""
        if BubbleSortVisualizer is None:
            print("Bubble sort visualizer not available. Check imports.")
            return
        try:
            input_str = input("Enter integers (space-separated): ").strip()
            arr = list(map(int, input_str.split()))
            
            visualizer = BubbleSortVisualizer()
            show_steps = input("Show all steps? (y/n): ").strip().lower() == 'y'
            
            if show_steps:
                visualizer.print_visualization(arr)
            else:
                sorted_arr, stats = visualizer.sort_with_visualization(arr)
                print(f"\nOriginal: {arr}")
                print(f"Sorted:   {sorted_arr}")
                print(f"Comparisons: {stats['comparisons']}")
                print(f"Swaps: {stats['swaps']}")
        except ValueError:
            print("Invalid input")
    
    def _selection_sort_demo(self) -> None:
        """Selection sort demonstration."""
        if selection_sort is None:
            print("Selection sort not available. Check imports.")
            return
        try:
            input_str = input("Enter integers (space-separated): ").strip()
            arr = list(map(int, input_str.split()))
            
            result = selection_sort(arr)
            print(f"\nOriginal: {arr}")
            print(f"Sorted:   {result}")
        except ValueError:
            print("Invalid input")
    
    def _insertion_sort_demo(self) -> None:
        """Insertion sort demonstration."""
        if insertion_sort is None:
            print("Insertion sort not available. Check imports.")
            return
        try:
            input_str = input("Enter integers (space-separated): ").strip()
            arr = list(map(int, input_str.split()))
            
            result = insertion_sort(arr)
            print(f"\nOriginal: {arr}")
            print(f"Sorted:   {result}")
        except ValueError:
            print("Invalid input")
    
    def _sorting_comparison(self) -> None:
        """Compare all sorting algorithms."""
        if None in [bubble_sort, selection_sort, insertion_sort]:
            print("Sorting algorithms not available. Check imports.")
            return
        size = int(input("Array size (default 100): ") or "100")
        arr = [random.randint(0, 1000) for _ in range(size)]
        
        algorithms = [
            ("Bubble Sort", bubble_sort),
            ("Selection Sort", selection_sort),
            ("Insertion Sort", insertion_sort),
        ]
        
        print(f"\nSorting {size} random integers:\n")
        
        for name, func in algorithms:
            start = time.perf_counter()
            result = func(arr)
            elapsed = time.perf_counter() - start
            print(f"{name:20} {elapsed:.8f}s")
    
    def _quickselect_demo(self) -> None:
        """Quickselect demonstration."""
        if QuickSelectVisualizer is None:
            print("Quickselect visualizer not available. Check imports.")
            return
        size = int(input("Array size (default 20): ") or "20")
        arr = [random.randint(0, 100) for _ in range(size)]
        k = int(input(f"Find kth smallest (1-{size}): "))
        
        visualizer = QuickSelectVisualizer()
        visualizer.print_comparison(arr, k)
    
    def _quickselect_interactive(self) -> None:
        """Interactive quickselect."""
        try:
            input_str = input("Enter integers (space-separated): ").strip()
            arr = list(map(int, input_str.split()))
            k = int(input(f"Find kth smallest (1-{len(arr)}): "))
            
            from quickselect import quickselect_simple
            result = quickselect_simple(arr, k)
            print(f"\n[RESULT] The {k}{'st' if k==1 else 'nd' if k==2 else 'rd' if k==3 else 'th'} smallest: {result}")
            print(f"  Verification: {sorted(arr)[k-1]}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def _quickselect_comparison(self) -> None:
        """Compare quickselect with sorting."""
        size = int(input("Array size (default 1000): ") or "1000")
        arr = [random.randint(0, size * 10) for _ in range(size)]
        k = size // 2
        
        # Quickselect
        visualizer = QuickSelectVisualizer()
        start = time.perf_counter()
        result_qs, stats_qs = visualizer.quickselect(arr[:], k)
        time_qs = time.perf_counter() - start
        
        # Sorting
        start = time.perf_counter()
        result_sort = sorted(arr)[k - 1]
        time_sort = time.perf_counter() - start
        
        print(f"\nArray size: {size}, finding {k}th smallest")
        print(f"Quickselect: {time_qs:.8f}s (comps: {stats_qs['comparisons']})")
        print(f"Sorting:     {time_sort:.8f}s")
        print(f"Speedup: {time_sort/time_qs:.2f}x")
    
    def _stack_demo(self) -> None:
        """Stack operations demo."""
        if Stack is None:
            print("Stack not available. Check imports.")
            return
        print("\nStack (LIFO) Demo")
        stack = Stack()
        
        while True:
            print(f"\nCurrent stack: {stack}")
            print("1. Push  2. Pop  3. Peek  4. Back")
            choice = input("Choice: ").strip()
            
            if choice == "1":
                try:
                    val = int(input("Value: "))
                    stack.push(val)
                except ValueError:
                    print("Invalid value")
            elif choice == "2":
                try:
                    print(f"Popped: {stack.pop()}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif choice == "3":
                try:
                    print(f"Top: {stack.peek()}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif choice == "4":
                break
    
    def _queue_demo(self) -> None:
        """Queue operations demo."""
        if Queue is None:
            print("Queue not available. Check imports.")
            return
        print("\nQueue (FIFO) Demo")
        queue = Queue()
        
        while True:
            print(f"\nCurrent queue: {queue}")
            print("1. Enqueue  2. Dequeue  3. Front  4. Back")
            choice = input("Choice: ").strip()
            
            if choice == "1":
                try:
                    val = input("Value: ")
                    queue.enqueue(val)
                except ValueError:
                    print("Invalid value")
            elif choice == "2":
                try:
                    print(f"Dequeued: {queue.dequeue()}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif choice == "3":
                try:
                    print(f"Front: {queue.front()}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif choice == "4":
                break
    
    def _deque_demo(self) -> None:
        """Deque operations demo."""
        if Deque is None:
            print("Deque not available. Check imports.")
            return
        print("\nDeque (Double-ended Queue) Demo")
        deque = Deque()
        
        while True:
            print(f"\nCurrent deque: {deque}")
            print("1. Add Front  2. Add Rear  3. Remove Front  4. Remove Rear  5. Back")
            choice = input("Choice: ").strip()
            
            if choice == "1":
                val = input("Value: ")
                deque.add_front(val)
            elif choice == "2":
                val = input("Value: ")
                deque.add_rear(val)
            elif choice == "3":
                try:
                    print(f"Removed: {deque.remove_front()}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif choice == "4":
                try:
                    print(f"Removed: {deque.remove_rear()}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif choice == "5":
                break
    
    def _bst_map_demo(self) -> None:
        """BST Map demonstration."""
        if BSTMap is None:
            print("BST Map not available. Check imports.")
            return
        print("\nBinary Search Tree Map")
        bst = BSTMap()
        keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
        
        for key in keys:
            bst.set(key, f"val_{key}")
        
        print(f"Inserted keys: {keys}")
        print(f"In-order: {list(bst.items_inorder())}")
        print(f"Min: {bst.min_item()}")
        print(f"Max: {bst.max_item()}")
        print(f"Is balanced: {bst.is_balanced()}")
    
    def _list_map_demo(self) -> None:
        """List Map demonstration."""
        if ListMap is None:
            print("List Map not available. Check imports.")
            return
        print("\nList Map (Linear)")
        list_map = ListMap()
        keys = [50, 30, 70, 20, 40]
        
        for key in keys:
            list_map.set(key, f"val_{key}")
        
        print(f"Inserted keys: {keys}")
        print(f"Get(40): {list_map.get(40)}")
        print(f"Contains(20): {list_map.contains(20)}")
    
    def _tree_comparison(self) -> None:
        """Compare BST vs List map performance."""
        if BSTMap is None or ListMap is None:
            print("Tree structures not available. Check imports.")
            return
        size = int(input("Size (default 1000): ") or "1000")
        keys = [random.randint(0, size * 10) for _ in range(size)]
        
        # BST
        bst = BSTMap()
        start = time.perf_counter()
        for key in keys:
            bst.set(key, key)
        for _ in range(100):
            bst.contains(keys[size//2])
        time_bst = time.perf_counter() - start
        
        # List
        list_map = ListMap()
        start = time.perf_counter()
        for key in keys:
            list_map.set(key, key)
        for _ in range(100):
            list_map.contains(keys[size//2])
        time_list = time.perf_counter() - start
        
        print(f"\nSize: {size} elements")
        print(f"BST:  {time_bst:.6f}s")
        print(f"List: {time_list:.6f}s")
        print(f"Speedup: {time_list/time_bst:.2f}x")
    
    def _set_interactive(self) -> None:
        """Interactive set operations."""
        set_a = Set()
        set_b = Set()
        
        print("\nSet A and Set B Operations")
        while True:
            print(f"\nA: {set_a}  B: {set_b}")
            print("1. Create A  2. Create B  3. Union  4. Intersection")
            print("5. Difference  6. Sym Diff  7. Relations  8. Back")
            choice = input("Choice: ").strip()
            
            if choice == "1":
                input_str = input("Elements (space-separated): ").strip()
                set_a = Set(input_str.split())
            elif choice == "2":
                input_str = input("Elements (space-separated): ").strip()
                set_b = Set(input_str.split())
            elif choice == "3":
                print(f"A ∪ B = {set_a.union(set_b)}")
            elif choice == "4":
                print(f"A ∩ B = {set_a.intersection(set_b)}")
            elif choice == "5":
                print(f"A - B = {set_a.difference(set_b)}")
            elif choice == "6":
                print(f"A Δ B = {set_a.symmetric_difference(set_b)}")
            elif choice == "7":
                print(f"A ⊆ B: {set_a.is_subset(set_b)}")
                print(f"A ⊇ B: {set_a.is_superset(set_b)}")
                print(f"Disjoint: {set_a.is_disjoint(set_b)}")
            elif choice == "8":
                break
    
    def _set_operations_demo(self) -> None:
        """Set operations examples."""
        if Set is None:
            print("Set operations not available. Check imports.")
            return
        set_a = Set(['a', 'b', 'c', 'd'])
        set_b = Set(['c', 'd', 'e', 'f'])
        
        print(f"\nSet A: {set_a}")
        print(f"Set B: {set_b}")
        print(f"\nA ∪ B = {set_a.union(set_b)}")
        print(f"A ∩ B = {set_a.intersection(set_b)}")
        print(f"A - B = {set_a.difference(set_b)}")
        print(f"B - A = {set_b.difference(set_a)}")
        print(f"A Δ B = {set_a.symmetric_difference(set_b)}")
    
    def _set_relationships(self) -> None:
        """Set relationships demo."""
        set_a = Set([1, 2, 3])
        set_b = Set([1, 2, 3, 4, 5])
        set_c = Set([6, 7, 8])
        
        print(f"\nSet A: {set_a}")
        print(f"Set B: {set_b}")
        print(f"Set C: {set_c}")
        print(f"\nA ⊆ B: {set_a.is_subset(set_b)}")
        print(f"B ⊇ A: {set_b.is_superset(set_a)}")
        print(f"A ∩ C = ∅ (disjoint): {set_a.is_disjoint(set_c)}")
    
    def _graph_demo(self) -> None:
        """Graph demonstration."""
        if GraphList is None:
            print("Graph structures not available. Check imports.")
            return
        print("\nGraph Creation Demo")
        graph = GraphList(directed=False)
        
        edges = [
            ('A', 'B', 1),
            ('B', 'C', 2),
            ('C', 'A', 3),
            ('C', 'D', 4),
            ('D', 'E', 1),
        ]
        
        for u, v, w in edges:
            graph.add_edge(u, v, w)
        
        print(f"Vertices: {graph.vertices()}")
        print(f"Neighbors of C: {graph.neighbors('C')}")
    
    def _graph_traversal(self) -> None:
        """Graph traversal demo."""
        print("\nGraph with paths from A")
        graph = GraphList(directed=False)
        
        for u, v in [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]:
            graph.add_edge(u, v)
        
        print(f"Vertices: {graph.vertices()}")
        for v in graph.vertices():
            print(f"  From A to {v}: {graph.neighbors(v)}")
    
    def run(self) -> None:
        """Run the interactive UI."""
        while self.running:
            self.display_main_menu()
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self.search_menu()
            elif choice == "2":
                self.sorting_menu()
            elif choice == "3":
                self.selection_menu()
            elif choice == "4":
                self.linear_structures_menu()
            elif choice == "5":
                self.tree_structures_menu()
            elif choice == "6":
                self._hash_demo()
            elif choice == "7":
                self.set_operations_menu()
            elif choice == "8":
                self.graph_menu()
            elif choice == "9":
                print(self.portfolio.get_system_info())
                self.portfolio.display_portfolio()
            elif choice == "10":
                self.portfolio.run_all_demos()
            elif choice == "11":
                self._performance_tools()
            elif choice == "0":
                print("\nExiting Portfolio System. Goodbye!")
                self.running = False
            else:
                print("Invalid choice. Try again.")
    
    def _hash_demo(self) -> None:
        """Hash table demonstration."""
        if HashTable is None:
            print("Hash table not available. Check imports.")
            return
        print("\nHash Table Demo")
        ht = HashTable(capacity=11)
        
        data = [('apple', 10), ('banana', 20), ('cherry', 30)]
        for key, value in data:
            ht.insert(key, value)
        
        print(f"Inserted: {data}")
        print(f"Search 'banana': {ht.search('banana')}")
        print(f"Size: {ht.size}")
    
    def _performance_tools(self) -> None:
        """Performance comparison tools."""
        while True:
            print("\n" + "=" * 80)
            print("PERFORMANCE COMPARISON TOOLS")
            print("=" * 80)
            print("\n1. Sorting Algorithms Comparison")
            print("2. Search Algorithms Comparison")
            print("3. Tree Structures Comparison")
            print("4. Quickselect vs Sorting")
            print("5. Back to Main Menu")
            print("0. Exit")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self._sorting_comparison()
            elif choice == "2":
                self._search_comparison()
            elif choice == "3":
                self._tree_comparison()
            elif choice == "4":
                self._quickselect_comparison()
            elif choice == "5":
                break
            elif choice == "0":
                self.running = False
                return


def main() -> None:
    """Main entry point."""
    ui = PortfolioUI()
    ui.run()


if __name__ == "__main__":
    main()
