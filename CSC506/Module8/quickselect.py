"""
Quickselect Algorithm
=====================

Efficient algorithm to find the kth smallest (or largest) element in an unsorted list.
Uses divide-and-conquer with random pivot selection for O(n) average-case performance.
"""

from typing import List, Optional, Tuple
import random


class QuickSelectVisualizer:
    """
    Quickselect implementation with detailed step-by-step visualization.
    
    Attributes:
        comparisons: Total number of comparisons made
        partitions: Total number of partition operations
        steps: List of steps for visualization
    """
    
    def __init__(self):
        self.comparisons = 0
        self.partitions = 0
        self.steps = []
    
    def _partition(self, arr: List[int], left: int, right: int, pivot_index: int) -> int:
        """
        Partition the array around a pivot element.
        
        Moves all elements smaller than pivot to the left,
        larger elements to the right.
        """
        pivot_value = arr[pivot_index]
        
        # Move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        store_index = left
        for i in range(left, right):
            self.comparisons += 1
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1
        
        # Move pivot to final position
        arr[right], arr[store_index] = arr[store_index], arr[right]
        self.partitions += 1
        
        return store_index
    
    def quickselect(self, arr: List[int], k: int) -> Tuple[int, dict]:
        """
        Find the kth smallest element (1-indexed, k >= 1).
        
        Args:
            arr: Unsorted list of integers
            k: Position of element to find (1-indexed)
            
        Returns:
            Tuple of (kth_smallest_element, statistics_dict)
        """
        if not arr:
            raise ValueError("Cannot select from empty list")
        
        if k < 1 or k > len(arr):
            raise ValueError(f"k must be between 1 and {len(arr)}")
        
        self.comparisons = 0
        self.partitions = 0
        self.steps = []
        
        a = arr[:]
        result = self._quickselect_recursive(a, 0, len(a) - 1, k - 1)
        
        stats = {
            'comparisons': self.comparisons,
            'partitions': self.partitions,
            'kth_smallest': result,
            'k': k,
            'array_size': len(arr)
        }
        
        return result, stats
    
    def _quickselect_recursive(self, arr: List[int], left: int, right: int, k_index: int) -> int:
        """
        Recursive quickselect helper.
        
        Args:
            arr: Array being searched
            left: Left boundary
            right: Right boundary
            k_index: Index of element to find (0-indexed)
        """
        if left == right:
            return arr[left]
        
        # Random pivot selection
        pivot_index = random.randint(left, right)
        pivot_index = self._partition(arr, left, right, pivot_index)
        
        self.steps.append({
            'operation': 'partition',
            'pivot_index': pivot_index,
            'array_state': arr[:],
            'search_range': (left, right),
            'k_index': k_index
        })
        
        if k_index == pivot_index:
            return arr[k_index]
        elif k_index < pivot_index:
            return self._quickselect_recursive(arr, left, pivot_index - 1, k_index)
        else:
            return self._quickselect_recursive(arr, pivot_index + 1, right, k_index)
    
    def find_kth_smallest_with_sorted(self, arr: List[int], k: int) -> Tuple[int, dict]:
        """
        Find kth smallest by sorting (for comparison purposes).
        
        Args:
            arr: Unsorted list
            k: Position to find
            
        Returns:
            Tuple of (kth_smallest, stats)
        """
        if k < 1 or k > len(arr):
            raise ValueError(f"k must be between 1 and {len(arr)}")
        
        sorted_arr = sorted(arr)
        return sorted_arr[k - 1], {
            'method': 'sorted',
            'k': k,
            'result': sorted_arr[k - 1]
        }
    
    def print_comparison(self, arr: List[int], k: int) -> None:
        """Compare quickselect vs sorting approaches."""
        print("\n" + "=" * 80)
        print("QUICKSELECT - COMPARISON WITH SORTING")
        print("=" * 80)
        print(f"Array: {arr}")
        print(f"Finding {k}{'st' if k == 1 else 'nd' if k == 2 else 'rd' if k == 3 else 'th'} smallest element\n")
        
        # Quickselect
        self.comparisons = 0
        self.partitions = 0
        self.steps = []
        result_qs, stats_qs = self.quickselect(arr, k)
        
        print(f"QUICKSELECT RESULT")
        print(f"  Element: {result_qs}")
        print(f"  Comparisons: {stats_qs['comparisons']}")
        print(f"  Partitions: {stats_qs['partitions']}")
        
        # Sorting approach
        result_sorted, stats_sorted = self.find_kth_smallest_with_sorted(arr, k)
        
        print(f"\nSORTING APPROACH")
        print(f"  Element: {result_sorted}")
        print(f"  Method: Sort then access index {k-1}")
        
        print(f"\nVERIFICATION")
        print(f"  Both methods agree: {result_qs == result_sorted}")
        print("=" * 80 + "\n")


def quickselect_simple(arr: List[int], k: int) -> int:
    """Simple quickselect without tracking."""
    def select(left: int, right: int, k_index: int) -> int:
        if left == right:
            return arr[left]
        
        pivot_index = random.randint(left, right)
        pivot_value = arr[pivot_index]
        
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1
        
        arr[right], arr[store_index] = arr[store_index], arr[right]
        
        if k_index == store_index:
            return arr[k_index]
        elif k_index < store_index:
            return select(left, store_index - 1, k_index)
        else:
            return select(store_index + 1, right, k_index)
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}")
    
    a = arr[:]
    return select(0, len(a) - 1, k - 1)


def interactive_quickselect_demo() -> None:
    """Interactive console demo for quickselect."""
    print("\n" + "=" * 80)
    print("QUICKSELECT INTERACTIVE DEMO")
    print("=" * 80)
    
    while True:
        print("\nOptions:")
        print("1. Find kth smallest in custom array")
        print("2. Find kth smallest in random array")
        print("3. Compare with sorting approach")
        print("4. Performance test")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == "1":
            try:
                input_str = input("Enter integers separated by spaces: ").strip()
                arr = list(map(int, input_str.split()))
                k = int(input(f"Enter k (1-{len(arr)}): "))
                
                result = quickselect_simple(arr, k)
                print(f"\nThe {k}{'st' if k == 1 else 'nd' if k == 2 else 'rd' if k == 3 else 'th'} smallest element is: {result}")
                print(f"Verification (sorted): {sorted(arr)[k-1]}")
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            size = int(input("Array size (default 20): ") or "20")
            arr = [random.randint(0, 100) for _ in range(size)]
            k = int(input(f"Enter k (1-{size}): "))
            
            print(f"Generated array: {arr}\n")
            
            visualizer = QuickSelectVisualizer()
            visualizer.print_comparison(arr, k)
        
        elif choice == "3":
            input_str = input("Enter integers separated by spaces: ").strip()
            arr = list(map(int, input_str.split()))
            k = int(input(f"Enter k (1-{len(arr)}): "))
            
            visualizer = QuickSelectVisualizer()
            visualizer.print_comparison(arr, k)
        
        elif choice == "4":
            print("\nPerformance Test: Quickselect vs Sorting")
            print("-" * 50)
            
            import time
            sizes = [100, 1000, 10000]
            
            for size in sizes:
                arr = [random.randint(0, size * 10) for _ in range(size)]
                k = size // 2
                
                # Quickselect
                visualizer = QuickSelectVisualizer()
                start = time.perf_counter()
                result_qs, _ = visualizer.quickselect(arr[:], k)
                time_qs = time.perf_counter() - start
                
                # Sorting
                start = time.perf_counter()
                result_sort = sorted(arr)[k - 1]
                time_sort = time.perf_counter() - start
                
                print(f"\nArray size: {size}, k={k}")
                print(f"  Quickselect: {time_qs:.8f}s (result: {result_qs})")
                print(f"  Sorting:     {time_sort:.8f}s (result: {result_sort})")
                print(f"  Speedup: {time_sort / time_qs:.2f}x")
        
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    interactive_quickselect_demo()
