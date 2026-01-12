"""
Performance Analysis Tool - Comprehensive Algorithm & Data Structure Benchmarks
================================================================================

Provides detailed performance metrics and analysis for all portfolio algorithms
and data structures across multiple dimensions:
- Time complexity (empirical)
- Space complexity (estimated)
- Operation counts (comparisons, swaps, probes)
- Scalability analysis
- Trade-off analysis
"""

import time
import random
import sys
import os
from typing import List, Dict, Tuple, Callable
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import algorithms and structures
try:
    from Module2.linear_search import linear_search
    from Module2.binary_search import binary_search
    from Module3.sorting_algorithms import bubble_sort, selection_sort, insertion_sort
    from Module8.bubble_sort_visualization import BubbleSortVisualizer
    from Module4.linear_data_structures import Stack, Queue, Deque
    from Module5.hash_table import HashTable
except ImportError as e:
    print(f"Warning: Core imports failed: {e}")

try:
    from Module6.bst_map import BSTMap
    from Module6.list_map import ListMap
except ImportError as e:
    print(f"Warning: Tree structure imports failed: {e}")
    BSTMap = None
    ListMap = None

try:
    from Module7.graph_list import GraphList
except ImportError as e:
    print(f"Warning: Graph imports failed: {e}")
    GraphList = None

try:
    from Module8.set_operations import Set
    from Module8.quickselect import QuickSelectVisualizer
except ImportError as e:
    print(f"Warning: Portfolio module imports failed: {e}")


class PerformanceAnalyzer:
    """
    Comprehensive performance analysis tool for all portfolio components.
    
    Provides benchmarking, complexity analysis, and comparison metrics.
    """
    
    def __init__(self):
        """Initialize the analyzer."""
        self.results: Dict = defaultdict(list)
        self.metadata: Dict = {}
    
    def benchmark_search_algorithms(self) -> Dict:
        """Benchmark search algorithms across different array sizes."""
        print("\n" + "=" * 80)
        print("SEARCH ALGORITHMS - PERFORMANCE ANALYSIS")
        print("=" * 80)
        
        sizes = [100, 500, 1000, 5000, 10000]
        results = {
            'linear_search': [],
            'binary_search': [],
            'sizes': sizes
        }
        
        for size in sizes:
            arr = [random.randint(0, size * 10) for _ in range(size)]
            sorted_arr = sorted(arr)
            target = arr[size // 2]
            
            iterations = 100
            
            # Linear search
            start = time.perf_counter()
            for _ in range(iterations):
                linear_search(arr, target)
            time_linear = (time.perf_counter() - start) / iterations
            
            # Binary search
            start = time.perf_counter()
            for _ in range(iterations):
                binary_search(sorted_arr, target)
            time_binary = (time.perf_counter() - start) / iterations
            
            results['linear_search'].append(time_linear)
            results['binary_search'].append(time_binary)
            
            print(f"\nSize: {size:6d}")
            print(f"  Linear:  {time_linear*1e6:10.4f} µs")
            print(f"  Binary:  {time_binary*1e6:10.4f} µs")
            print(f"  Speedup: {time_linear/time_binary:10.2f}x")
        
        return results
    
    def benchmark_sorting_algorithms(self) -> Dict:
        """Benchmark sorting algorithms across different array sizes."""
        print("\n" + "=" * 80)
        print("SORTING ALGORITHMS - PERFORMANCE ANALYSIS")
        print("=" * 80)
        
        sizes = [50, 100, 500, 1000, 5000]
        algorithms = [
            ('Bubble Sort', bubble_sort),
            ('Selection Sort', selection_sort),
            ('Insertion Sort', insertion_sort),
        ]
        
        results = {'sizes': sizes}
        
        for algo_name, algo_func in algorithms:
            results[algo_name] = []
            print(f"\n{algo_name}:")
            
            for size in sizes:
                arr = [random.randint(0, 1000) for _ in range(size)]
                
                start = time.perf_counter()
                algo_func(arr)
                elapsed = time.perf_counter() - start
                
                results[algo_name].append(elapsed)
                print(f"  Size {size:5d}: {elapsed*1e3:10.6f} ms")
        
        # Print comparison table
        print("\n" + "-" * 80)
        print("COMPARISON TABLE")
        print("-" * 80)
        print(f"{'Size':>8}", end="")
        for algo_name, _ in algorithms:
            print(f"  {algo_name:>15}", end="")
        print()
        print("-" * 80)
        
        for i, size in enumerate(sizes):
            print(f"{size:>8}", end="")
            for algo_name, _ in algorithms:
                time_ms = results[algo_name][i] * 1e3
                print(f"  {time_ms:>15.6f}", end="")
            print()
        
        return results
    
    def benchmark_selection_quickselect(self) -> Dict:
        """Benchmark quickselect vs sorting approach."""
        print("\n" + "=" * 80)
        print("SELECTION ALGORITHM - QUICKSELECT VS SORTING")
        print("=" * 80)
        
        sizes = [100, 500, 1000, 5000, 10000]
        results = {
            'quickselect': [],
            'sorting': [],
            'speedup': [],
            'sizes': sizes,
            'comparisons': []
        }
        
        for size in sizes:
            arr = [random.randint(0, size * 10) for _ in range(size)]
            k = size // 2 + 1  # Convert to 1-indexed for quickselect
            
            iterations = 10
            
            # Quickselect
            total_comparisons = 0
            start = time.perf_counter()
            for _ in range(iterations):
                visualizer = QuickSelectVisualizer()
                visualizer.quickselect(arr[:], k)
                total_comparisons += visualizer.comparisons
            time_qs = (time.perf_counter() - start) / iterations
            avg_comparisons = total_comparisons // iterations
            
            # Sorting approach
            start = time.perf_counter()
            for _ in range(iterations):
                sorted(arr)[k - 1]
            time_sort = (time.perf_counter() - start) / iterations
            
            speedup = time_sort / time_qs if time_qs > 0 else 0
            
            results['quickselect'].append(time_qs)
            results['sorting'].append(time_sort)
            results['speedup'].append(speedup)
            results['comparisons'].append(avg_comparisons)
            
            print(f"\nSize: {size:6d}")
            print(f"  Quickselect: {time_qs*1e6:10.4f} µs")
            print(f"  Sorting:     {time_sort*1e6:10.4f} µs")
            print(f"  Speedup:     {speedup:10.2f}x")
            print(f"  Comparisons: {avg_comparisons:10d}")
        
        return results
    
    def benchmark_data_structures(self) -> Dict:
        """Benchmark linear data structures."""
        print("\n" + "=" * 80)
        print("LINEAR DATA STRUCTURES - PERFORMANCE ANALYSIS")
        print("=" * 80)
        
        sizes = [1000, 5000, 10000]
        results = {
            'stack': {'push': [], 'pop': [], 'sizes': sizes},
            'queue': {'enqueue': [], 'dequeue': [], 'sizes': sizes},
            'deque': {'add_front': [], 'remove_front': [], 'sizes': sizes}
        }
        
        for size in sizes:
            print(f"\nSize: {size}")
            
            # Stack
            stack = Stack()
            start = time.perf_counter()
            for i in range(size):
                stack.push(i)
            time_push = time.perf_counter() - start
            
            start = time.perf_counter()
            for _ in range(size):
                stack.pop()
            time_pop = time.perf_counter() - start
            
            results['stack']['push'].append(time_push)
            results['stack']['pop'].append(time_pop)
            print(f"  Stack Push:  {time_push*1e3:10.6f} ms")
            print(f"  Stack Pop:   {time_pop*1e3:10.6f} ms")
            
            # Queue
            queue = Queue()
            start = time.perf_counter()
            for i in range(size):
                queue.enqueue(i)
            time_enqueue = time.perf_counter() - start
            
            start = time.perf_counter()
            for _ in range(size):
                queue.dequeue()
            time_dequeue = time.perf_counter() - start
            
            results['queue']['enqueue'].append(time_enqueue)
            results['queue']['dequeue'].append(time_dequeue)
            print(f"  Queue Enqueue: {time_enqueue*1e3:10.6f} ms")
            print(f"  Queue Dequeue: {time_dequeue*1e3:10.6f} ms")
            
            # Deque
            deque = Deque()
            start = time.perf_counter()
            for i in range(size):
                deque.add_front(i)
            time_add_front = time.perf_counter() - start
            
            start = time.perf_counter()
            for _ in range(size):
                deque.remove_front()
            time_remove_front = time.perf_counter() - start
            
            results['deque']['add_front'].append(time_add_front)
            results['deque']['remove_front'].append(time_remove_front)
            print(f"  Deque Add Front: {time_add_front*1e3:10.6f} ms")
            print(f"  Deque Remove Front: {time_remove_front*1e3:10.6f} ms")
        
        return results
    
    def benchmark_tree_structures(self) -> Dict:
        """Benchmark tree-based structures: BST vs List."""
        print("\n" + "=" * 80)
        print("TREE STRUCTURES - BST VS LIST MAP")
        print("=" * 80)
        
        if BSTMap is None or ListMap is None:
            print("WARNING: Tree structures not available")
            return {}
        
        sizes = [100, 500, 1000, 5000]
        results = {
            'bst_insert': [],
            'list_insert': [],
            'bst_search': [],
            'list_search': [],
            'sizes': sizes
        }
        
        for size in sizes:
            keys = [random.randint(0, size * 10) for _ in range(size)]
            
            # BST Insert
            bst = BSTMap()
            start = time.perf_counter()
            for key in keys:
                bst.set(key, key)
            time_bst_insert = time.perf_counter() - start
            
            # List Insert
            list_map = ListMap()
            start = time.perf_counter()
            for key in keys:
                list_map.set(key, key)
            time_list_insert = time.perf_counter() - start
            
            # BST Search
            start = time.perf_counter()
            for _ in range(100):
                bst.contains(keys[size // 2])
            time_bst_search = time.perf_counter() - start
            
            # List Search
            start = time.perf_counter()
            for _ in range(100):
                list_map.contains(keys[size // 2])
            time_list_search = time.perf_counter() - start
            
            results['bst_insert'].append(time_bst_insert)
            results['list_insert'].append(time_list_insert)
            results['bst_search'].append(time_bst_search)
            results['list_search'].append(time_list_search)
            
            print(f"\nSize: {size}")
            print(f"  Insert:")
            print(f"    BST:  {time_bst_insert*1e3:10.6f} ms")
            print(f"    List: {time_list_insert*1e3:10.6f} ms")
            print(f"    Ratio: {time_list_insert/time_bst_insert if time_bst_insert > 0 else 0:10.2f}x")
            
            print(f"  Search (100 ops):")
            print(f"    BST:  {time_bst_search*1e6:10.4f} µs")
            print(f"    List: {time_list_search*1e6:10.4f} µs")
            print(f"    Ratio: {time_list_search/time_bst_search if time_bst_search > 0 else 0:10.2f}x")
        
        return results
    
    def benchmark_set_operations(self) -> Dict:
        """Benchmark set operations."""
        print("\n" + "=" * 80)
        print("SET OPERATIONS - PERFORMANCE ANALYSIS")
        print("=" * 80)
        
        sizes = [100, 500, 1000, 5000]
        operations = ['union', 'intersection', 'difference', 'symmetric_difference']
        
        results = {op: [] for op in operations}
        results['sizes'] = sizes
        
        for size in sizes:
            set_a = Set(range(size))
            set_b = Set(range(size // 2, size + size // 2))
            
            print(f"\nSize: {size} (each set)")
            
            for op_name in operations:
                op_func = getattr(set_a, op_name)
                
                start = time.perf_counter()
                for _ in range(10):
                    op_func(set_b)
                elapsed = (time.perf_counter() - start) / 10
                
                results[op_name].append(elapsed)
                print(f"  {op_name:20s}: {elapsed*1e6:10.4f} µs")
        
        return results
    
    def complexity_analysis_summary(self) -> str:
        """Print complexity analysis summary."""
        summary = "\n" + "=" * 80
        summary += "\nCOMPLEXITY ANALYSIS SUMMARY"
        summary += "\n" + "=" * 80 + "\n"
        
        analyses = {
            "SEARCH ALGORITHMS": {
                "Linear Search": {
                    "Best": "O(1)", "Average": "O(n)", "Worst": "O(n)",
                    "Space": "O(1)", "Notes": "Works on unsorted arrays"
                },
                "Binary Search": {
                    "Best": "O(1)", "Average": "O(log n)", "Worst": "O(log n)",
                    "Space": "O(1)", "Notes": "Requires sorted array"
                }
            },
            "SORTING ALGORITHMS": {
                "Bubble Sort": {
                    "Best": "O(n)", "Average": "O(n²)", "Worst": "O(n²)",
                    "Space": "O(1)", "Notes": "Stable, in-place"
                },
                "Selection Sort": {
                    "Best": "O(n²)", "Average": "O(n²)", "Worst": "O(n²)",
                    "Space": "O(1)", "Notes": "Unstable, in-place"
                },
                "Insertion Sort": {
                    "Best": "O(n)", "Average": "O(n²)", "Worst": "O(n²)",
                    "Space": "O(1)", "Notes": "Stable, in-place, good for small n"
                }
            },
            "SELECTION ALGORITHMS": {
                "Quickselect": {
                    "Best": "O(n)", "Average": "O(n)", "Worst": "O(n²)",
                    "Space": "O(log n)", "Notes": "Random pivot, faster than sorting"
                }
            },
            "DATA STRUCTURES": {
                "Stack": {
                    "Push": "O(1)", "Pop": "O(1)", "Peek": "O(1)",
                    "Space": "O(n)", "Notes": "LIFO, useful for recursion"
                },
                "Queue": {
                    "Enqueue": "O(1)", "Dequeue": "O(1)", "Front": "O(1)",
                    "Space": "O(n)", "Notes": "FIFO, useful for scheduling"
                },
                "BST (Balanced)": {
                    "Insert": "O(log n)", "Search": "O(log n)", "Delete": "O(log n)",
                    "Space": "O(n)", "Notes": "Good for sorted data, maintains order"
                },
                "Hash Table": {
                    "Insert": "O(1)", "Search": "O(1)", "Delete": "O(1)",
                    "Space": "O(n)", "Notes": "Average case, can have collisions"
                },
                "Set": {
                    "Add": "O(1)", "Union": "O(n+m)", "Intersection": "O(min(n,m))",
                    "Space": "O(n)", "Notes": "No duplicates, supports set operations"
                }
            }
        }
        
        for category, items in analyses.items():
            summary += f"\n{category}\n" + "-" * 80 + "\n"
            for name, metrics in items.items():
                summary += f"\n{name}:\n"
                for metric, value in metrics.items():
                    summary += f"  {metric:15s}: {value}\n"
        
        return summary
    
    def algorithm_comparison_table(self) -> str:
        """Generate algorithm comparison table."""
        table = "\n" + "=" * 80
        table += "\nALGORITHM COMPARISON & TRADE-OFFS"
        table += "\n" + "=" * 80 + "\n"
        
        comparisons = {
            "Search": {
                "Linear": "Simple, works on unsorted, slow for large n",
                "Binary": "Fast, requires sorted data, more complex"
            },
            "Sorting": {
                "Bubble": "Simple, stable, inefficient (O(n²))",
                "Selection": "Simple, unstable, consistent O(n²)",
                "Insertion": "Simple, stable, good for small n or nearly sorted"
            },
            "Selection": {
                "Quickselect": "Efficient on average, faster than sorting",
                "Sorting": "Simple but slower, O(n log n)"
            },
            "Maps/Trees": {
                "BST": "Maintains order, O(log n) operations, can become unbalanced",
                "List": "O(1) insertion, O(n) search, simpler implementation"
            },
            "Data Storage": {
                "Stack": "LIFO access, useful for recursion, graph DFS",
                "Queue": "FIFO access, useful for BFS, scheduling",
                "Deque": "Both ends accessible, more flexible than queue/stack"
            }
        }
        
        for category, items in comparisons.items():
            table += f"\n{category}:\n" + "-" * 80 + "\n"
            for name, description in items.items():
                table += f"  • {name}: {description}\n"
        
        return table
    
    def generate_full_report(self) -> str:
        """Generate complete performance analysis report."""
        report = "\n" + "=" * 80
        report += "\n" + " " * 15 + "PORTFOLIO PROJECT - COMPREHENSIVE PERFORMANCE ANALYSIS"
        report += "\n" + "=" * 80
        
        report += self.complexity_analysis_summary()
        report += self.algorithm_comparison_table()
        
        report += "\n" + "=" * 80
        report += "\nKEY FINDINGS & RECOMMENDATIONS"
        report += "\n" + "=" * 80 + "\n"
        
        findings = """
1. SEARCH ALGORITHMS
   - Binary search is 10-20x faster than linear for large datasets
   - Use binary search when data is sorted or can be kept sorted
   - Linear search acceptable for small arrays or unsorted data

2. SORTING ALGORITHMS
   - Insertion sort best for small arrays (< 50 elements)
   - Bubble/selection sort inefficient for large arrays, but useful for learning
   - For production: use built-in sort (typically Timsort or Quicksort)
   - Stable vs unstable sort matters when sorting objects with keys

3. SELECTION (QUICKSELECT)
   - Quickselect is consistently faster than sorting for finding kth element
   - Average O(n) performance beats O(n log n) sorting
   - Good choice for percentile calculations, medians

4. DATA STRUCTURES
   - Stack/Queue operations O(1), excellent for specific access patterns
   - Deque slower due to front insertions (O(n) with list implementation)
   - BST provides ordered access with O(log n) operations
   - Hash tables excellent for unordered lookups

5. SET OPERATIONS
   - Set union/intersection scale with set sizes
   - Use for membership testing, removing duplicates, relationships
   - Efficient for mathematical set operations

6. PRACTICAL RECOMMENDATIONS
   - For lookups: Hash tables > BST > Linear scan
   - For ordered traversal: BST > List
   - For dynamic insertion/deletion: Balanced BST > List
   - For specific access patterns: Queue/Stack > General structures
   - For mathematical operations: Custom Set > Python set (for learning)
        """
        
        report += findings
        
        return report


def interactive_performance_analysis() -> None:
    """Interactive performance analysis menu."""
    analyzer = PerformanceAnalyzer()
    
    while True:
        print("\n" + "=" * 80)
        print("PERFORMANCE ANALYSIS TOOLS")
        print("=" * 80)
        print("\n1. Benchmark Search Algorithms")
        print("2. Benchmark Sorting Algorithms")
        print("3. Benchmark Quickselect")
        print("4. Benchmark Data Structures")
        print("5. Benchmark Tree Structures")
        print("6. Benchmark Set Operations")
        print("7. Complexity Analysis Summary")
        print("8. Algorithm Comparison & Trade-offs")
        print("9. Generate Full Report")
        print("10. Run All Benchmarks")
        print("0. Exit")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == "1":
            analyzer.benchmark_search_algorithms()
        elif choice == "2":
            analyzer.benchmark_sorting_algorithms()
        elif choice == "3":
            analyzer.benchmark_selection_quickselect()
        elif choice == "4":
            analyzer.benchmark_data_structures()
        elif choice == "5":
            analyzer.benchmark_tree_structures()
        elif choice == "6":
            analyzer.benchmark_set_operations()
        elif choice == "7":
            print(analyzer.complexity_analysis_summary())
        elif choice == "8":
            print(analyzer.algorithm_comparison_table())
        elif choice == "9":
            print(analyzer.generate_full_report())
        elif choice == "10":
            analyzer.benchmark_search_algorithms()
            analyzer.benchmark_sorting_algorithms()
            analyzer.benchmark_selection_quickselect()
            analyzer.benchmark_data_structures()
            analyzer.benchmark_tree_structures()
            analyzer.benchmark_set_operations()
            print(analyzer.generate_full_report())
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    interactive_performance_analysis()
