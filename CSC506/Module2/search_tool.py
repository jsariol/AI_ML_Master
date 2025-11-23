import time
import random
from typing import List, Callable, Optional

from linear_search import linear_search
from binary_search import binary_search


def generate_array(size: int, sorted_array: bool = False) -> List[int]:
    
    arr = [random.randint(0, size * 10) for _ in range(size)]
    if sorted_array:
        arr.sort()
    return arr


def time_search(
    search_func: Callable[[List[int], int], Optional[int]],
    arr: List[int],
    target: int
) -> float:
    
    start = time.perf_counter()
    _ = search_func(arr, target)
    end = time.perf_counter()
    return end - start


def run_performance_tests() -> None:
    
    sizes = [100, 1_000, 10_000]
    print("\n=== Performance Testing Results ===")

    for size in sizes:
        # Linear search on unsorted array
        arr_unsorted = generate_array(size, sorted_array=False)
        target = random.choice(arr_unsorted)
        t_linear = time_search(linear_search, arr_unsorted, target)

        # Binary search on sorted array
        arr_sorted = sorted(arr_unsorted)
        t_binary = time_search(binary_search, arr_sorted, target)

        print(f"\nArray size: {size}")
        print(f"  Linear search time:  {t_linear:.8f} seconds")
        print(f"  Binary search time:  {t_binary:.8f} seconds")


def interactive_mode() -> None:
    
    print("=== Algorithm Comparison Tool ===")
    print("This tool compares linear search and binary search.")
    print("Available array sizes: 100, 1000, 10000")

    # Choose array size
    size_str = input("Enter array size (100 / 1000 / 10000): ").strip()
    if size_str not in {"100", "1000", "10000"}:
        print("Invalid size. Defaulting to 100.")
        size = 100
    else:
        size = int(size_str)

    # Choose algorithm
    print("\nChoose search algorithm:")
    print("1. Linear search (works on unsorted arrays)")
    print("2. Binary search (requires sorted arrays)")

    algo_choice = input("Enter 1 or 2: ").strip()

    if algo_choice == "1":
        use_binary = False
    elif algo_choice == "2":
        use_binary = True
    else:
        print("Invalid choice. Defaulting to linear search.")
        use_binary = False

    # Generate appropriate array
    if use_binary:
        arr = generate_array(size, sorted_array=True)
        algorithm_name = "Binary Search"
        search_function = binary_search
    else:
        arr = generate_array(size, sorted_array=False)
        algorithm_name = "Linear Search"
        search_function = linear_search

    print(f"\nGenerated an array of size {size} for {algorithm_name}.")
    # Ask user for a target value
    try:
        target_input = input("Enter an integer value to search for: ").strip()
        target = int(target_input)
    except ValueError:
        print("Invalid input. Using a random target from the array.")
        target = random.choice(arr)

    # Run search and measure time
    elapsed = time_search(search_function, arr, target)
    result_index = search_function(arr, target)

    # Show results
    print(f"\nAlgorithm: {algorithm_name}")
    if result_index is not None:
        print(f"Result: value {target} FOUND at index {result_index}")
    else:
        print(f"Result: value {target} NOT FOUND")
    print(f"Execution time: {elapsed:.8f} seconds")

   
def main() -> None:
    
    
    run_performance_tests()

    
    interactive_mode()


if __name__ == "__main__":
    main()
