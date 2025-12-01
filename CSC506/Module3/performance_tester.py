import time
from typing import Callable, Dict, List, Any

import matplotlib.pyplot as plt

from sorting_algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
)
from data_generator import generate_dataset


SortFunc = Callable[[List[int]], List[int]]


def run_performance_tests() -> List[Dict[str, Any]]:
    
    algorithms: Dict[str, SortFunc] = {
        "bubble": bubble_sort,
        "selection": selection_sort,
        "insertion": insertion_sort,
        "merge": merge_sort,
    }

    dataset_types = ["random", "sorted", "reverse", "partial"]
    sizes = [1_000, 5_000, 10_000, 50_000]

    results: List[Dict[str, Any]] = []

    print("=== Sorting Algorithm Performance Tests ===\n")

    for size in sizes:
        print(f"Dataset size: {size}")
        for dtype in dataset_types:
            
            base_data = generate_dataset(size, dtype)

            for algo_name, algo_func in algorithms.items():
                
                data_copy = base_data[:]

                start = time.perf_counter()
                _ = algo_func(data_copy)
                end = time.perf_counter()

                elapsed = end - start

                results.append(
                    {
                        "algorithm": algo_name,
                        "dataset_type": dtype,
                        "size": size,
                        "time_seconds": elapsed,
                    }
                )

                print(
                    f"  {algo_name:<9} on {dtype:<7}: "
                    f"{elapsed:.6f} seconds"
                )
        print()

    return results


def print_results_table(results: List[Dict[str, Any]]) -> None:
    
    print("\n=== Results Table ===")
    print(
        f"{'Algorithm':<10} {'Dataset':<8} "
        f"{'Size':<8} {'Time (s)':<10}"
    )
    print("-" * 45)

    for row in results:
        print(
            f"{row['algorithm']:<10} "
            f"{row['dataset_type']:<8} "
            f"{row['size']:<8} "
            f"{row['time_seconds']:<10.6f}"
        )


def plot_results_for_size(
    results: List[Dict[str, Any]],
    size: int,
) -> None:
    
    filtered = [r for r in results if r["size"] == size]

    if not filtered:
        print(f"No results for size {size}")
        return

    # Group by dataset type
    dataset_types = sorted({r["dataset_type"] for r in filtered})
    algorithms = sorted({r["algorithm"] for r in filtered})

    for dtype in dataset_types:
        subset = [
            r for r in filtered if r["dataset_type"] == dtype
        ]
        subset.sort(key=lambda r: r["algorithm"])

        labels = [r["algorithm"] for r in subset]
        times = [r["time_seconds"] for r in subset]

        plt.figure()
        plt.bar(labels, times)
        plt.title(f"Size={size}, Dataset={dtype}")
        plt.xlabel("Algorithm")
        plt.ylabel("Time (seconds)")
        plt.tight_layout()
        plt.show()


def main() -> None:
    
    results = run_performance_tests()
    print_results_table(results)

    
    plot_results_for_size(results, 1_000)
    plot_results_for_size(results, 5_000)
    plot_results_for_size(results, 10_000)
    plot_results_for_size(results, 50_000)


if __name__ == "__main__":
    main()
