"""
Bubble Sort with Step-by-Step Visualization

"""

from typing import List, Tuple, Optional


class BubbleSortVisualizer:
    """
    A bubble sort implementation that tracks and visualizes every step.
    
    Attributes:
        comparisons: Total number of element comparisons made
        swaps: Total number of swaps performed
        steps: List of tuples (array_state, positions_being_compared, was_swapped)
    """
    
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.steps = []
        
    def sort_with_visualization(self, arr: List[int]) -> Tuple[List[int], dict]:
        """
        Sort an array using bubble sort and capture visualization data.
        
        Args:
            arr: List of integers to sort
            
        Returns:
            Tuple of (sorted_array, statistics_dict)
        """
        self.comparisons = 0
        self.swaps = 0
        self.steps = []
        
        n = len(arr)
        a = arr[:]
        
        # Initial state
        self.steps.append({
            'iteration': 0,
            'pass': 0,
            'array': a[:],
            'compared_indices': None,
            'was_swapped': False,
            'description': 'Initial array'
        })
        
        for pass_num in range(n):
            swapped = False
            
            for j in range(0, n - 1 - pass_num):
                # Perform comparison
                self.comparisons += 1
                
                if a[j] > a[j + 1]:
                    # Perform swap
                    a[j], a[j + 1] = a[j + 1], a[j]
                    self.swaps += 1
                    swapped = True
                    
                    # Record step with swap
                    self.steps.append({
                        'iteration': len(self.steps),
                        'pass': pass_num + 1,
                        'comparison_index': j,
                        'array': a[:],
                        'compared_indices': (j, j + 1),
                        'was_swapped': True,
                        'values_swapped': (a[j + 1], a[j]),
                        'description': f'Pass {pass_num + 1}: Swapped {a[j + 1]} and {a[j]}'
                    })
                else:
                    # Record step without swap
                    self.steps.append({
                        'iteration': len(self.steps),
                        'pass': pass_num + 1,
                        'comparison_index': j,
                        'array': a[:],
                        'compared_indices': (j, j + 1),
                        'was_swapped': False,
                        'values_compared': (a[j], a[j + 1]),
                        'description': f'Pass {pass_num + 1}: {a[j]} < {a[j + 1]} (no swap)'
                    })
            
            # Optimization: if no swaps in this pass, array is sorted
            if not swapped:
                break
        
        stats = {
            'comparisons': self.comparisons,
            'swaps': self.swaps,
            'total_steps': len(self.steps),
            'passes_executed': pass_num + 1,
            'is_sorted': a == sorted(a)
        }
        
        return a, stats
    
    def get_step(self, step_index: int) -> Optional[dict]:
        """Get details of a specific step."""
        if 0 <= step_index < len(self.steps):
            return self.steps[step_index]
        return None
    
    def print_visualization(self, arr: List[int], max_steps: Optional[int] = None) -> None:
        """
        Print detailed step-by-step visualization of bubble sort.
        
        Args:
            arr: Array to sort
            max_steps: Maximum steps to display (None for all)
        """
        sorted_arr, stats = self.sort_with_visualization(arr)
        
        print("\n" + "=" * 80)
        print("BUBBLE SORT - STEP-BY-STEP VISUALIZATION")
        print("=" * 80)
        print(f"Initial array: {arr}")
        print(f"Target array:  {sorted_arr}\n")
        
        steps_to_show = self.steps
        if max_steps and max_steps < len(self.steps):
            steps_to_show = self.steps[:max_steps + 1]
        
        for step in steps_to_show:
            print(f"Step {step['iteration']} (Pass {step['pass']}): {step['description']}")
            print(f"  Array: {step['array']}")
            
            if step['compared_indices']:
                indices = step['compared_indices']
                arr_visual = list(step['array'])
                visual = ""
                for i, val in enumerate(arr_visual):
                    if i in indices:
                        visual += f"[{val}] "
                    else:
                        visual += f" {val}  "
                print(f"  Indices: {visual}")
            print()
        
        if max_steps and max_steps < len(self.steps):
            print(f"... ({len(self.steps) - max_steps - 1} more steps)\n")
        
        print("=" * 80)
        print("STATISTICS")
        print("=" * 80)
        print(f"Total comparisons: {stats['comparisons']}")
        print(f"Total swaps:       {stats['swaps']}")
        print(f"Total steps:       {stats['total_steps']}")
        print(f"Passes executed:   {stats['passes_executed']}")
        print(f"Is sorted:         {stats['is_sorted']}")
        print("=" * 80 + "\n")


def bubble_sort_simple(arr: List[int]) -> List[int]:
    """Simple bubble sort without visualization."""
    n = len(arr)
    a = arr[:]
    
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    
    return a


def interactive_bubble_sort_demo() -> None:
    """Interactive console demo for bubble sort visualization."""
    print("\n" + "=" * 80)
    print("BUBBLE SORT INTERACTIVE DEMO")
    print("=" * 80)
    
    while True:
        print("\nOptions:")
        print("1. Sort custom array")
        print("2. Sort random array")
        print("3. Sort pre-defined example")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            try:
                input_str = input("Enter integers separated by spaces: ").strip()
                arr = list(map(int, input_str.split()))
                
                visualizer = BubbleSortVisualizer()
                show_all = input("Show all steps? (y/n, default n): ").strip().lower() != 'y'
                max_steps = None if not show_all else int(input("Max steps to show (or press Enter for all): ") or 0) or None
                
                if max_steps:
                    visualizer.print_visualization(arr, max_steps)
                else:
                    visualizer.print_visualization(arr)
                    
            except ValueError:
                print("Invalid input. Please enter space-separated integers.")
        
        elif choice == "2":
            import random
            size = int(input("Array size (default 10): ") or "10")
            arr = [random.randint(0, 100) for _ in range(size)]
            print(f"Generated array: {arr}")
            
            visualizer = BubbleSortVisualizer()
            show_all = input("Show all steps? (y/n, default n): ").strip().lower() == 'y'
            
            if show_all:
                visualizer.print_visualization(arr)
            else:
                sorted_arr, stats = visualizer.sort_with_visualization(arr)
                print(f"\nSorted array: {sorted_arr}")
                print(f"Comparisons: {stats['comparisons']}, Swaps: {stats['swaps']}")
        
        elif choice == "3":
            examples = [
                [5, 2, 8, 1, 9],
                [64, 34, 25, 12, 22, 11],
                [1, 2, 3, 4, 5],  # Already sorted
                [5, 4, 3, 2, 1],  # Reverse sorted
            ]
            
            for i, ex in enumerate(examples, 1):
                print(f"{i}. {ex}")
            
            ex_choice = input("Choose example (1-4): ").strip()
            if ex_choice in ['1', '2', '3', '4']:
                arr = examples[int(ex_choice) - 1]
                visualizer = BubbleSortVisualizer()
                visualizer.print_visualization(arr)
        
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    interactive_bubble_sort_demo()
