"""
Portfolio System - Unified Data Structures and Algorithms
==========================================================

A comprehensive integrated system containing all course data structures and algorithms:
- Search algorithms (linear, binary)
- Sorting algorithms (bubble, selection, insertion, quick, merge)
- Linear data structures (stack, queue, deque)
- Tree-based structures (BST, BST Map)
- Hash tables
- Graphs
- Sets with all operations
- Selection algorithms (quickselect)

"""

from typing import Any, List, Optional, Dict, Tuple
import sys
import os

# Import all modules (adjust paths as needed)
# Add CSC506 root and current directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Search algorithms
try:
    from Module2.linear_search import linear_search
    from Module2.binary_search import binary_search
except ImportError:
    print("Warning: Search algorithms not available")

# Sorting algorithms
try:
    from Module3.sorting_algorithms import bubble_sort, selection_sort, insertion_sort
    from bubble_sort_visualization import BubbleSortVisualizer, bubble_sort_simple
except ImportError:
    print("Warning: Sorting algorithms not available")

# Linear data structures
try:
    from Module4.linear_data_structures import Stack, Queue, Deque
except ImportError:
    print("Warning: Linear data structures not available")

# Hash tables
try:
    from Module5.hash_table import HashTable
except ImportError:
    print("Warning: Hash table not available")

# Trees and maps
try:
    from Module6.bst import BinarySearchTree, BSTNode
    from Module6.bst_map import BSTMap
    from Module6.list_map import ListMap
except ImportError:
    print("Warning: Tree structures not available")

# Graphs
try:
    from Module7.graph_list import GraphList
except ImportError:
    print("Warning: Graph not available")

# Set operations
try:
    from set_operations import Set
except ImportError:
    print("Warning: Set operations not available")

# Quickselect
try:
    from quickselect import QuickSelectVisualizer
except ImportError:
    print("Warning: Quickselect not available")


class PortfolioSystem:
    """
    Unified portfolio system containing all data structures and algorithms.
    
    This class provides a centralized interface to interact with all course concepts,
    demonstrating integration and understanding of their relationships.
    """
    
    def __init__(self):
        """Initialize the portfolio system."""
        self.name = "CSC506 - Algorithms and Data Structures Portfolio System"
        self.version = "1.0"
        self.systems = {}
        self._initialize_systems()
    
    def _initialize_systems(self):
        """Initialize all available subsystems."""
        self.systems = {
            'search': {
                'name': 'Search Algorithms',
                'algorithms': ['linear_search', 'binary_search'],
                'description': 'Linear and binary search implementations'
            },
            'sorting': {
                'name': 'Sorting Algorithms',
                'algorithms': ['bubble_sort', 'selection_sort', 'insertion_sort'],
                'description': 'Multiple sorting algorithm implementations'
            },
            'selection': {
                'name': 'Selection Algorithm',
                'algorithms': ['quickselect'],
                'description': 'Efficient kth smallest element finding'
            },
            'linear_structures': {
                'name': 'Linear Data Structures',
                'structures': ['Stack', 'Queue', 'Deque'],
                'description': 'LIFO, FIFO, and double-ended queue structures'
            },
            'trees': {
                'name': 'Tree-Based Structures',
                'structures': ['BinarySearchTree', 'BSTMap', 'ListMap'],
                'description': 'Binary search trees and map implementations'
            },
            'hash_structures': {
                'name': 'Hash-Based Structures',
                'structures': ['HashTable'],
                'description': 'Hash table with collision resolution'
            },
            'sets': {
                'name': 'Set Operations',
                'structures': ['Set'],
                'description': 'Complete set implementation with all operations'
            },
            'graphs': {
                'name': 'Graph Structures',
                'structures': ['GraphList'],
                'description': 'Graph implementations with adjacency lists'
            }
        }
    
    def display_portfolio(self) -> None:
        """Display the entire portfolio structure."""
        print("\n" + "=" * 80)
        print(f"{self.name} (v{self.version})")
        print("=" * 80)
        
        for category, info in self.systems.items():
            print(f"\n{info['name']}")
            print(f"  {info['description']}")
            
            if 'algorithms' in info:
                print(f"  Algorithms: {', '.join(info['algorithms'])}")
            if 'structures' in info:
                print(f"  Structures: {', '.join(info['structures'])}")
        
        print("\n" + "=" * 80 + "\n")
    
    def search_demo(self) -> None:
        """Demonstrate search algorithms."""
        print("\n" + "=" * 80)
        print("SEARCH ALGORITHMS DEMO")
        print("=" * 80)
        
        import random
        
        # Create sample data
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_data = sorted(data)
        target = 5
        
        print(f"\nUnsorted array: {data}")
        print(f"Sorted array: {sorted_data}")
        print(f"Target: {target}\n")
        
        # Linear search
        result = linear_search(data, target)
        print(f"Linear search result: {result} (index)")
        
        # Binary search
        result = binary_search(sorted_data, target)
        print(f"Binary search result: {result} (index)")
        
        print("=" * 80 + "\n")
    
    def sorting_demo(self) -> None:
        """Demonstrate sorting algorithms."""
        print("\n" + "=" * 80)
        print("SORTING ALGORITHMS DEMO")
        print("=" * 80)
        
        import random
        
        data = [64, 34, 25, 12, 22, 11, 90, 88]
        print(f"\nOriginal array: {data}\n")
        
        # Bubble sort
        result = bubble_sort(data)
        print(f"Bubble sort:     {result}")
        
        # Selection sort
        result = selection_sort(data)
        print(f"Selection sort:  {result}")
        
        # Insertion sort
        result = insertion_sort(data)
        print(f"Insertion sort:  {result}")
        
        print("=" * 80 + "\n")
    
    def selection_demo(self) -> None:
        """Demonstrate quickselect algorithm."""
        print("\n" + "=" * 80)
        print("QUICKSELECT ALGORITHM DEMO")
        print("=" * 80)
        
        data = [3, 7, 2, 9, 1, 8, 4]
        k = 3
        
        print(f"\nArray: {data}")
        print(f"Finding {k}rd smallest element\n")
        
        visualizer = QuickSelectVisualizer()
        result, stats = visualizer.quickselect(data, k)
        
        print(f"Result: {result}")
        print(f"Comparisons: {stats['comparisons']}")
        print(f"Partitions: {stats['partitions']}")
        print(f"Verification (sorted): {sorted(data)[k-1]}")
        
        print("=" * 80 + "\n")
    
    def linear_structures_demo(self) -> None:
        """Demonstrate linear data structures."""
        print("\n" + "=" * 80)
        print("LINEAR DATA STRUCTURES DEMO")
        print("=" * 80)
        
        # Stack
        print("\nStack (LIFO):")
        stack = Stack()
        for item in [1, 2, 3, 4, 5]:
            stack.push(item)
        print(f"  After pushing 1,2,3,4,5: {stack}")
        print(f"  Pop: {stack.pop()}")
        print(f"  Peek: {stack.peek()}")
        
        # Queue
        print("\nQueue (FIFO):")
        queue = Queue()
        for item in ['a', 'b', 'c', 'd']:
            queue.enqueue(item)
        print(f"  After enqueuing a,b,c,d: {queue}")
        print(f"  Dequeue: {queue.dequeue()}")
        print(f"  Front: {queue.front()}")
        
        # Deque
        print("\nDeque (Double-ended):")
        deque = Deque()
        deque.add_rear(1)
        deque.add_rear(2)
        deque.add_front(0)
        print(f"  After operations: {deque}")
        print(f"  Remove front: {deque.remove_front()}")
        print(f"  Remove rear: {deque.remove_rear()}")
        
        print("\n" + "=" * 80 + "\n")
    
    def tree_structures_demo(self) -> None:
        """Demonstrate tree-based structures."""
        print("\n" + "=" * 80)
        print("TREE-BASED STRUCTURES DEMO")
        print("=" * 80)
        
        import random
        
        # BST Map
        print("\nBinary Search Tree Map:")
        bst_map = BSTMap()
        
        keys = [50, 30, 70, 20, 40, 60, 80]
        for key in keys:
            bst_map.set(key, f"value_{key}")
        
        print(f"  Inserted keys: {keys}")
        print(f"  Contains 40: {bst_map.contains(40)}")
        print(f"  Contains 100: {bst_map.contains(100)}")
        print(f"  Get(50): {bst_map.get(50)}")
        print(f"  Min: {bst_map.min_item()}")
        print(f"  Max: {bst_map.max_item()}")
        print(f"  Is balanced: {bst_map.is_balanced()}")
        
        print("\n" + "=" * 80 + "\n")
    
    def hash_structures_demo(self) -> None:
        """Demonstrate hash-based structures."""
        print("\n" + "=" * 80)
        print("HASH-BASED STRUCTURES DEMO")
        print("=" * 80)
        
        print("\nHash Table (String keys):")
        ht = HashTable(capacity=11)
        
        data = [('apple', 10), ('banana', 20), ('cherry', 30), ('date', 40)]
        for key, value in data:
            ht.insert(key, value)
        
        print(f"  Inserted: {data}")
        print(f"  Search 'banana': {ht.search('banana')}")
        print(f"  Search 'orange': {ht.search('orange')}")
        print(f"  Size: {ht.size}")
        
        print("\n" + "=" * 80 + "\n")
    
    def set_operations_demo(self) -> None:
        """Demonstrate set operations."""
        print("\n" + "=" * 80)
        print("SET OPERATIONS DEMO")
        print("=" * 80)
        
        print("\nSet Operations:")
        set_a = Set(['a', 'b', 'c', 'd'])
        set_b = Set(['c', 'd', 'e', 'f'])
        
        print(f"  Set A: {set_a}")
        print(f"  Set B: {set_b}")
        
        print(f"\n  A ∪ B: {set_a.union(set_b)}")
        print(f"  A ∩ B: {set_a.intersection(set_b)}")
        print(f"  A - B: {set_a.difference(set_b)}")
        print(f"  A Δ B: {set_a.symmetric_difference(set_b)}")
        
        print(f"\n  A ⊆ B: {set_a.is_subset(set_b)}")
        print(f"  A ⊇ B: {set_a.is_superset(set_b)}")
        print(f"  A ∩ B = ∅: {set_a.is_disjoint(set_b)}")
        
        print("\n" + "=" * 80 + "\n")
    
    def graph_structures_demo(self) -> None:
        """Demonstrate graph structures."""
        print("\n" + "=" * 80)
        print("GRAPH STRUCTURES DEMO")
        print("=" * 80)
        
        print("\nGraph (Undirected):")
        graph = GraphList(directed=False)
        
        edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'A', 3), ('C', 'D', 4)]
        for u, v, w in edges:
            graph.add_edge(u, v, w)
        
        print(f"  Vertices: {graph.vertices()}")
        print(f"  Edges: {edges}")
        print(f"  Neighbors of 'C': {graph.neighbors('C')}")
        
        print("\n" + "=" * 80 + "\n")
    
    def run_all_demos(self) -> None:
        """Run all demonstration modules."""
        print("\n" + "=" * 80)
        print("RUNNING ALL PORTFOLIO DEMONSTRATIONS")
        print("=" * 80)
        
        demos = [
            ("Portfolio Overview", self.display_portfolio),
            ("Search Algorithms", self.search_demo),
            ("Sorting Algorithms", self.sorting_demo),
            ("Selection Algorithms", self.selection_demo),
            ("Linear Structures", self.linear_structures_demo),
            ("Tree Structures", self.tree_structures_demo),
            ("Hash Structures", self.hash_structures_demo),
            ("Set Operations", self.set_operations_demo),
            ("Graph Structures", self.graph_structures_demo),
        ]
        
        for i, (name, demo_func) in enumerate(demos, 1):
            try:
                demo_func()
            except Exception as e:
                print(f"\nError in {name}: {e}\n")
        
        print("\n" + "=" * 80)
        print("ALL DEMONSTRATIONS COMPLETED")
        print("=" * 80 + "\n")
    
    def get_system_info(self) -> str:
        """Get system information and structure."""
        info = f"\n{self.name} (v{self.version})\n"
        info += "=" * 80 + "\n"
        
        total_algorithms = 0
        total_structures = 0
        
        for category, sys_info in self.systems.items():
            if 'algorithms' in sys_info:
                total_algorithms += len(sys_info['algorithms'])
            if 'structures' in sys_info:
                total_structures += len(sys_info['structures'])
        
        info += f"Total Algorithm Types: {total_algorithms}\n"
        info += f"Total Data Structures: {total_structures}\n"
        info += f"Total Components: {total_algorithms + total_structures}\n"
        info += "=" * 80 + "\n"
        
        return info


if __name__ == "__main__":
    portfolio = PortfolioSystem()
    portfolio.run_all_demos()
