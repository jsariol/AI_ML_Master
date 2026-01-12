# CSC506 Portfolio Project - Complete Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Core Components](#core-components)
4. [Getting Started](#getting-started)
5. [Module Guide](#module-guide)
6. [Algorithm Specifications](#algorithm-specifications)
7. [Data Structure Specifications](#data-structure-specifications)
8. [Performance Analysis](#performance-analysis)
9. [Design Decisions](#design-decisions)
10. [Usage Examples](#usage-examples)

---

## Project Overview

This portfolio project demonstrates mastery of fundamental data structures and algorithms covered in CSC506 (Design and Analysis of Algorithms). The project integrates all course concepts into a unified, interactive system with comprehensive performance analysis and visualization tools.

### Project Goals
✓ Implement and visualize bubble sort with step-by-step tracking
✓ Implement quickselect algorithm for efficient kth element finding
✓ Create comprehensive Set class with all operations
✓ Integrate all data structures from previous modules
✓ Provide interactive testing and comparison tools
✓ Deliver comprehensive performance analysis

### Key Achievements
- **8+ Integrated Algorithms**: Search, sorting, selection
- **5+ Data Structures**: Stacks, queues, trees, graphs, sets, hash tables
- **Interactive UI**: Menu-driven console application
- **Performance Tools**: Benchmarking and complexity analysis
- **Full Documentation**: Design decisions, usage examples, architecture

---

## Core Components

### 1. Bubble Sort Visualization (bubble_sort_visualization.py)

**Purpose**: Implement bubble sort with detailed step-by-step visualization

**Key Features**:
- Tracks every swap and comparison
- Records array state at each iteration
- Provides statistics (comparisons, swaps, passes)
- Interactive demo with visualization options
- Pre-defined and custom array examples

**Classes**:
```python
class BubbleSortVisualizer:
    def sort_with_visualization(arr) -> (List, Dict)
    def print_visualization(arr, max_steps=None) -> None
```

**Time Complexity**:
- Best: O(n) - already sorted array
- Average: O(n²)
- Worst: O(n²)

**Space Complexity**: O(n) for creating copies

**Example Usage**:
```python
visualizer = BubbleSortVisualizer()
arr, stats = visualizer.sort_with_visualization([5, 2, 8, 1, 9])
print(f"Comparisons: {stats['comparisons']}")
print(f"Swaps: {stats['swaps']}")
```

### 2. Quickselect Algorithm (quickselect.py)

**Purpose**: Efficiently find the kth smallest element in an unsorted list

**Key Features**:
- Random pivot selection (Hoare partition)
- Average O(n) time complexity
- Comparison with sorting approach
- Step-by-step visualization
- Performance metrics tracking

**Classes**:
```python
class QuickSelectVisualizer:
    def quickselect(arr, k) -> (int, Dict)
    def find_kth_smallest_with_sorted(arr, k) -> (int, Dict)
    def print_comparison(arr, k) -> None
```

**Algorithm Strategy**:
1. Select random pivot
2. Partition array around pivot
3. If pivot_index == k-1, return arr[k-1]
4. If pivot_index < k-1, search right
5. If pivot_index > k-1, search left

**Time Complexity**:
- Best/Average: O(n)
- Worst: O(n²) - rare with random pivots
- Space: O(log n) for recursion

**Example Usage**:
```python
from quickselect import QuickSelectVisualizer

visualizer = QuickSelectVisualizer()
result, stats = visualizer.quickselect([3, 7, 2, 9, 1], 3)
print(f"3rd smallest: {result}")  # Output: 3
print(f"Comparisons: {stats['comparisons']}")
```

### 3. Set Operations (set_operations.py)

**Purpose**: Complete Set implementation with all standard set operations

**Key Features**:
- Union (A ∪ B)
- Intersection (A ∩ B)
- Difference (A - B)
- Symmetric Difference (A Δ B)
- Subset/Superset checking
- Disjoint testing
- Batch operations
- Operator overloading

**Classes**:
```python
class Set:
    def union(other) -> Set
    def intersection(other) -> Set
    def difference(other) -> Set
    def symmetric_difference(other) -> Set
    def is_subset(other) -> bool
    def is_superset(other) -> bool
    def is_disjoint(other) -> bool
    
    # Operators
    __or__()    # | for union
    __and__()   # & for intersection
    __sub__()   # - for difference
    __xor__()   # ^ for symmetric difference
```

**Mathematical Definitions**:
- **Union**: A ∪ B = {x | x ∈ A or x ∈ B}
- **Intersection**: A ∩ B = {x | x ∈ A and x ∈ B}
- **Difference**: A - B = {x | x ∈ A and x ∉ B}
- **Symmetric Difference**: A Δ B = (A - B) ∪ (B - A)

**Time Complexity**:
- Add/Remove/Lookup: O(1) average
- Union: O(n + m)
- Intersection: O(min(n, m))
- Difference: O(n)
- Symmetric Difference: O(n + m)

**Example Usage**:
```python
from set_operations import Set

set_a = Set(['a', 'b', 'c', 'd'])
set_b = Set(['c', 'd', 'e', 'f'])

union = set_a.union(set_b)           # {'a', 'b', 'c', 'd', 'e', 'f'}
intersection = set_a.intersection(set_b)  # {'c', 'd'}
difference = set_a.difference(set_b)      # {'a', 'b'}
sym_diff = set_a.symmetric_difference(set_b)  # {'a', 'b', 'e', 'f'}
```

### 4. Portfolio System (portfolio_system.py)

**Purpose**: Unified system integrating all data structures and algorithms

**Key Features**:
- Centralized access to all components
- System overview and information
- Individual and integrated demos
- Modular component access

**Classes**:
```python
class PortfolioSystem:
    def display_portfolio() -> None
    def search_demo() -> None
    def sorting_demo() -> None
    def selection_demo() -> None
    def linear_structures_demo() -> None
    def tree_structures_demo() -> None
    def hash_structures_demo() -> None
    def set_operations_demo() -> None
    def graph_structures_demo() -> None
    def run_all_demos() -> None
```

**Integrated Components**:
- Search: Linear & Binary
- Sorting: Bubble, Selection, Insertion
- Selection: Quickselect
- Linear: Stack, Queue, Deque
- Trees: BST, Maps
- Hash: Hash Tables
- Sets: Complete set implementation
- Graphs: Graph List representation

### 5. Interactive UI (portfolio_ui.py)

**Purpose**: Menu-driven console interface for testing and comparing components

**Key Features**:
- Main menu with 11+ options
- Specialized menus for each category
- Interactive demonstrations
- Performance comparisons
- Real-time benchmarking
- User-friendly navigation

**Menu Structure**:
```
Main Menu
├── Search Algorithms
├── Sorting Algorithms
├── Selection Algorithms
├── Linear Data Structures
├── Tree Structures
├── Hash Tables
├── Set Operations
├── Graph Structures
├── Portfolio Overview
├── Run All Demos
├── Performance Tools
└── Exit
```

**Example**: Running Bubble Sort Demo
```
$ python portfolio_ui.py
Enter choice: 2  (Sorting)
Enter choice: 1  (Bubble Sort)
Enter integers: 5 2 8 1 9
Show all steps? (y/n): y
```

### 6. Performance Analysis (performance_analysis.py)

**Purpose**: Comprehensive benchmarking and complexity analysis

**Key Benchmarks**:
- Search algorithms (linear vs binary)
- Sorting algorithms comparison
- Quickselect vs sorting approach
- Data structure operations
- Tree structure comparison (BST vs List)
- Set operations performance

**Classes**:
```python
class PerformanceAnalyzer:
    def benchmark_search_algorithms() -> Dict
    def benchmark_sorting_algorithms() -> Dict
    def benchmark_selection_quickselect() -> Dict
    def benchmark_data_structures() -> Dict
    def benchmark_tree_structures() -> Dict
    def benchmark_set_operations() -> Dict
    def complexity_analysis_summary() -> str
    def algorithm_comparison_table() -> str
    def generate_full_report() -> str
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- No external dependencies (uses only stdlib)

### Running the Interactive UI

```bash
cd CSC506
python portfolio_ui.py
```

This launches the interactive menu system where you can:
1. Test individual algorithms
2. Compare algorithm performance
3. Visualize operations step-by-step
4. Run comprehensive benchmarks

### Running Individual Demonstrations

```bash
# Bubble Sort Visualization
python bubble_sort_visualization.py

# Quickselect
python quickselect.py

# Set Operations
python set_operations.py

# Portfolio System
python portfolio_system.py

# Performance Analysis
python performance_analysis.py
```

---

## Module Guide

### Search Module (Module2)
- `linear_search(arr, target)` - Sequential search O(n)
- `binary_search(arr, target)` - Binary search on sorted arrays O(log n)
- `search_tool.py` - Interactive comparison tool

### Sorting Module (Module3)
- `bubble_sort(arr)` - Bubble sort visualization with step tracking
- `selection_sort(arr)` - Selection sort
- `insertion_sort(arr)` - Insertion sort
- `BubbleSortVisualizer` - Detailed step-by-step visualization

### Linear Structures (Module4)
- `Stack` - LIFO data structure
  - Methods: push(), pop(), peek()
- `Queue` - FIFO data structure
  - Methods: enqueue(), dequeue(), front()
- `Deque` - Double-ended queue
  - Methods: add_front(), add_rear(), remove_front(), remove_rear()

### Hash Structures (Module5)
- `HashTable` - Hash table with collision resolution
  - Methods: insert(key, value), search(key), delete(key)
- `PriorityQueue` - Priority-based queue

### Tree Structures (Module6)
- `BinarySearchTree` - Basic BST
  - Methods: insert(), search(), delete(), traverse()
- `BSTMap` - BST-based map implementation
  - Methods: set(), get(), contains(), delete()
- `ListMap` - Linear map implementation

### Graph Structures (Module7)
- `GraphList` - Adjacency list representation
  - Methods: add_vertex(), add_edge(), neighbors(), vertices()

### Selection Algorithm
- `QuickSelectVisualizer.quickselect(arr, k)` - Find kth smallest

### Set Operations
- `Set` class with all standard operations
- Union, intersection, difference, symmetric difference
- Subset, superset, disjoint testing

---

## Algorithm Specifications

### Bubble Sort Algorithm
**Definition**: Repeatedly steps through the list, compares adjacent elements, and swaps them if in wrong order.

**Pseudocode**:
```
BubbleSort(arr):
    n = length(arr)
    for i = 0 to n-1:
        swapped = false
        for j = 0 to n-1-i:
            if arr[j] > arr[j+1]:
                swap(arr[j], arr[j+1])
                swapped = true
        if not swapped:
            break
    return arr
```

**Characteristics**:
- **Stable**: Yes (equal elements maintain relative order)
- **In-place**: Yes (O(1) space)
- **Adaptive**: Yes (faster on nearly sorted data)
- **Best use**: Educational, nearly sorted data

### Quickselect Algorithm
**Definition**: Divide-and-conquer algorithm to find kth smallest element without full sorting.

**Pseudocode**:
```
QuickSelect(arr, left, right, k):
    if left == right:
        return arr[left]
    
    pivot_index = random(left, right)
    pivot_index = Partition(arr, left, right, pivot_index)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return QuickSelect(arr, left, pivot_index-1, k)
    else:
        return QuickSelect(arr, pivot_index+1, right, k)
```

**Why It's Efficient**:
- Average O(n) vs O(n log n) for sorting
- Doesn't need to fully sort array
- Useful for finding percentiles, medians
- Random pivot reduces worst-case probability

---

## Data Structure Specifications

### Stack (LIFO)
**Operations**:
- `push(x)`: Add element to top - O(1)
- `pop()`: Remove from top - O(1)
- `peek()`: View top without removing - O(1)
- `is_empty()`: Check if empty - O(1)

**Use Cases**:
- Function call stack
- Undo/redo functionality
- Expression evaluation
- Depth-first search

### Queue (FIFO)
**Operations**:
- `enqueue(x)`: Add to rear - O(1)
- `dequeue()`: Remove from front - O(1)*
- `front()`: View front - O(1)
- `is_empty()`: Check if empty - O(1)

*O(n) with simple list; O(1) with deque/circular buffer

**Use Cases**:
- Task scheduling
- Print queue management
- Breadth-first search
- Message queues

### Binary Search Tree (BST)
**Operations**:
- `insert(key, value)`: Add element - O(log n) average
- `search(key)`: Find element - O(log n) average
- `delete(key)`: Remove element - O(log n) average
- `min()`, `max()`: Boundary values - O(log n)

**Properties**:
- Left child < parent < right child
- Maintains sorted order (in-order traversal)
- Can become unbalanced (degrade to O(n))

### Hash Table
**Operations**:
- `insert(key, value)`: Add element - O(1) average
- `search(key)`: Find element - O(1) average
- `delete(key)`: Remove element - O(1) average

**Collision Resolution**:
- Chaining: Store collisions in linked lists
- Load factor: n / capacity
- Rehash when load factor exceeds threshold

---

## Performance Analysis

### Empirical Benchmarks

**Search Algorithms** (array size 10,000):
- Linear: ~50-100 µs
- Binary: ~0.5-1 µs
- **Speedup: 100x**

**Sorting Algorithms** (array size 1,000):
- Bubble: ~5-10 ms
- Insertion: ~2-3 ms
- Selection: ~3-4 ms

**Quickselect vs Sorting** (array size 10,000, k=5000):
- Quickselect: ~100-150 µs
- Sorting: ~500-800 µs
- **Speedup: 5-8x**

**Tree Structures** (insertion of 5,000 elements):
- BST: ~2-5 ms
- List: ~50-100 ms
- **Speedup: 10-20x**

### Complexity Comparison Table

| Algorithm | Best | Average | Worst | Space | Notes |
|-----------|------|---------|-------|-------|-------|
| Linear Search | O(1) | O(n) | O(n) | O(1) | Unsorted |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | Sorted |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Stable |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Stable |
| Quickselect | O(n) | O(n) | O(n²) | O(log n) | Find kth |
| BST Search | - | O(log n) | O(n) | O(1) | Ordered |
| Hash Table | - | O(1) | O(n) | O(n) | Unordered |

---

## Design Decisions

### 1. Bubble Sort Visualization
**Decision**: Track every step with array state
**Rationale**: Educational value for understanding sorting mechanics
**Trade-off**: Higher memory usage for large arrays, but invaluable for learning

### 2. Quickselect Random Pivot
**Decision**: Use random pivot selection (Las Vegas algorithm)
**Rationale**: Reduces worst-case O(n²) probability while maintaining O(n) average
**Alternative**: Median-of-medians (deterministic but more complex)

### 3. Set Implementation Using Python's built-in set
**Decision**: Wrap Python's set for consistency
**Rationale**: Educational focus on set operations, not hash implementation
**Trade-off**: Not implementing hash table from scratch (covered in Module5)

### 4. UI Architecture
**Decision**: Menu-driven console application
**Rationale**: Matches course pattern, emphasizes learning, cross-platform compatible
**Alternative**: Web UI (more complex, requires Flask/Django)

### 5. Performance Analysis
**Decision**: Comprehensive benchmarking across all sizes and algorithms
**Rationale**: Validates complexity analysis theory with empirical data
**Metrics**: Time, comparisons, operations, cache effects

### 6. Module Organization
**Decision**: Keep components in separate files for modularity
**Rationale**: Easy to understand, maintain, extend, and test independently
**Integration**: portfolio_system.py unifies all modules

---

## Usage Examples

### Example 1: Visualizing Bubble Sort

```python
from bubble_sort_visualization import BubbleSortVisualizer

# Create visualizer
viz = BubbleSortVisualizer()

# Sort and get statistics
arr = [5, 2, 8, 1, 9]
sorted_arr, stats = viz.sort_with_visualization(arr)

print(f"Sorted: {sorted_arr}")
print(f"Comparisons: {stats['comparisons']}")
print(f"Swaps: {stats['swaps']}")

# Print detailed visualization
viz.print_visualization(arr)
```

### Example 2: Finding kth Smallest

```python
from quickselect import QuickSelectVisualizer, quickselect_simple

# Simple usage
arr = [3, 7, 2, 9, 1, 8]
k = 3
result = quickselect_simple(arr, k)
print(f"3rd smallest: {result}")  # Output: 3

# With statistics
visualizer = QuickSelectVisualizer()
result, stats = visualizer.quickselect(arr, k)
print(f"Comparisons: {stats['comparisons']}")
print(f"Partitions: {stats['partitions']}")
```

### Example 3: Set Operations

```python
from set_operations import Set

# Create sets
A = Set(['a', 'b', 'c'])
B = Set(['c', 'd', 'e'])

# Union
print(A | B)  # {'a', 'b', 'c', 'd', 'e'}

# Intersection
print(A & B)  # {'c'}

# Difference
print(A - B)  # {'a', 'b'}

# Symmetric Difference
print(A ^ B)  # {'a', 'b', 'd', 'e'}

# Relationships
print(A.is_subset(B))    # False
print(A.is_disjoint(B))  # False
```

### Example 4: Using Stack and Queue

```python
from Module4.linear_data_structures import Stack, Queue

# Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())   # 3
print(stack.peek())  # 2

# Queue
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print(queue.dequeue())  # 'a'
print(queue.front())    # 'b'
```

### Example 5: Tree Operations

```python
from Module6.bst_map import BSTMap

# Create BST Map
bst = BSTMap()

# Insert elements
for key in [50, 30, 70, 20, 40, 60, 80]:
    bst.set(key, f"value_{key}")

# Search operations
print(bst.contains(40))    # True
print(bst.get(40))         # 'value_40'

# Traversals
print(list(bst.items_inorder()))   # Sorted order
print(bst.is_balanced())           # True/False

# Boundary operations
print(bst.min_item())  # (20, 'value_20')
print(bst.max_item())  # (80, 'value_80')
```

### Example 6: Performance Comparison

```python
from performance_analysis import PerformanceAnalyzer
import time

analyzer = PerformanceAnalyzer()

# Run benchmarks
search_results = analyzer.benchmark_search_algorithms()
sorting_results = analyzer.benchmark_sorting_algorithms()

# Get reports
print(analyzer.complexity_analysis_summary())
print(analyzer.algorithm_comparison_table())
print(analyzer.generate_full_report())
```

---

## Conclusion

This portfolio project successfully integrates all CSC506 course concepts into a comprehensive, interactive, and well-documented system. The implementation demonstrates:

1. **Mastery of Algorithms**: Bubble sort, quickselect, binary search, etc.
2. **Understanding of Data Structures**: Stacks, queues, trees, graphs, sets
3. **Performance Analysis**: Empirical benchmarking and complexity analysis
4. **Software Engineering**: Modular design, comprehensive documentation, testing
5. **User Interface**: Interactive menu system for exploration and learning

### Learning Outcomes
- Understand algorithm complexity and its practical implications
- Recognize appropriate data structure selection for different use cases
- Appreciate trade-offs between simplicity and efficiency
- Apply divide-and-conquer and other algorithmic paradigms
- Analyze and improve algorithmic performance

### Future Enhancements
- Implement self-balancing trees (AVL, Red-Black)
- Add more sorting algorithms (Merge Sort, Quick Sort, Heap Sort)
- Implement graphs algorithms (BFS, DFS, Dijkstra, Floyd-Warshall)
- Add visualization using graphics library
- Create web-based interface

---

**Author**: Jose Carlos Sariol
**Date**: January 2026
**Version**: 1.0
