import time
import random
from typing import List, Dict, Callable, Any

import matplotlib.pyplot as plt

from data_structures import Stack, Queue, LinkedList
from complexity_analyzer import predict_complexity


# Type alias for a single benchmark result row
BenchmarkRow = Dict[str, Any]


def benchmark_stack(input_sizes: List[int], trials_per_op: int = 1000) -> List[BenchmarkRow]:
    
    results: List[BenchmarkRow] = []

    for n in input_sizes:
        # Prepare initial data
        initial_data = list(range(n))

        # --- INSERT (push) ---
        stack = Stack(initial_data)
        start = time.perf_counter()
        for i in range(trials_per_op):
            stack.push(-i)  # push dummy values
            stack.pop()     
        end = time.perf_counter()
        avg_insert_time = (end - start) / trials_per_op

        predicted_insert = predict_complexity("stack", "insert") or {}
        results.append({
            "structure": "stack",
            "operation": "insert",
            "n": n,
            "avg_time_seconds": avg_insert_time,
            "predicted_time": predicted_insert.get("time"),
            "predicted_space": predicted_insert.get("space"),
        })

        # --- DELETE (pop) ---
        stack = Stack(initial_data)
        start = time.perf_counter()
        for _ in range(trials_per_op):
            stack.push(0)   # ensure not empty
            stack.pop()
        end = time.perf_counter()
        avg_delete_time = (end - start) / trials_per_op

        predicted_delete = predict_complexity("stack", "delete") or {}
        results.append({
            "structure": "stack",
            "operation": "delete",
            "n": n,
            "avg_time_seconds": avg_delete_time,
            "predicted_time": predicted_delete.get("time"),
            "predicted_space": predicted_delete.get("space"),
        })

        # --- SEARCH (linear scan) ---
        stack = Stack(initial_data)
        # Choose random targets, sometimes present, sometimes not
        search_values = [random.randint(0, n * 2) for _ in range(trials_per_op)]

        start = time.perf_counter()
        for value in search_values:            
            _ = value in stack._data
        end = time.perf_counter()
        avg_search_time = (end - start) / trials_per_op

        predicted_search = predict_complexity("stack", "search") or {}
        results.append({
            "structure": "stack",
            "operation": "search",
            "n": n,
            "avg_time_seconds": avg_search_time,
            "predicted_time": predicted_search.get("time"),
            "predicted_space": predicted_search.get("space"),
        })

    return results


def benchmark_queue(input_sizes: List[int], trials_per_op: int = 1000) -> List[BenchmarkRow]:
    
    results: List[BenchmarkRow] = []

    for n in input_sizes:
        initial_data = list(range(n))

        # --- INSERT (enqueue) ---
        queue = Queue(initial_data)
        start = time.perf_counter()
        for i in range(trials_per_op):
            queue.enqueue(-i)
            queue.dequeue()
        end = time.perf_counter()
        avg_insert_time = (end - start) / trials_per_op

        predicted_insert = predict_complexity("queue", "insert") or {}
        results.append({
            "structure": "queue",
            "operation": "insert",
            "n": n,
            "avg_time_seconds": avg_insert_time,
            "predicted_time": predicted_insert.get("time"),
            "predicted_space": predicted_insert.get("space"),
        })

        # --- DELETE (dequeue) ---
        queue = Queue(initial_data)
        start = time.perf_counter()
        for _ in range(trials_per_op):
            queue.enqueue(0)
            queue.dequeue()
        end = time.perf_counter()
        avg_delete_time = (end - start) / trials_per_op

        predicted_delete = predict_complexity("queue", "delete") or {}
        results.append({
            "structure": "queue",
            "operation": "delete",
            "n": n,
            "avg_time_seconds": avg_delete_time,
            "predicted_time": predicted_delete.get("time"),
            "predicted_space": predicted_delete.get("space"),
        })

        # --- SEARCH ---
        queue = Queue(initial_data)
        search_values = [random.randint(0, n * 2) for _ in range(trials_per_op)]

        start = time.perf_counter()
        for value in search_values:
            _ = value in queue._data
        end = time.perf_counter()
        avg_search_time = (end - start) / trials_per_op

        predicted_search = predict_complexity("queue", "search") or {}
        results.append({
            "structure": "queue",
            "operation": "search",
            "n": n,
            "avg_time_seconds": avg_search_time,
            "predicted_time": predicted_search.get("time"),
            "predicted_space": predicted_search.get("space"),
        })

    return results


def benchmark_linked_list(input_sizes: List[int], trials_per_op: int = 1000) -> List[BenchmarkRow]:
    
    results: List[BenchmarkRow] = []

    for n in input_sizes:
        initial_data = list(range(n))

        # --- INSERT (append) ---
        ll = LinkedList(initial_data)
        start = time.perf_counter()
        for i in range(trials_per_op):
            ll.append(-i)
            ll.delete(-i)     
        end = time.perf_counter()
        avg_insert_time = (end - start) / trials_per_op

        predicted_insert = predict_complexity("linked_list", "insert") or {}
        results.append({
            "structure": "linked_list",
            "operation": "insert",
            "n": n,
            "avg_time_seconds": avg_insert_time,
            "predicted_time": predicted_insert.get("time"),
            "predicted_space": predicted_insert.get("space"),
        })

        # --- DELETE (delete by value) ---
        ll = LinkedList(initial_data)
        start = time.perf_counter()
        for _ in range(trials_per_op):            
            if ll.head is not None:
                value = ll.head.value
                ll.delete(value)
                ll.append(value)
        end = time.perf_counter()
        avg_delete_time = (end - start) / trials_per_op

        predicted_delete = predict_complexity("linked_list", "delete") or {}
        results.append({
            "structure": "linked_list",
            "operation": "delete",
            "n": n,
            "avg_time_seconds": avg_delete_time,
            "predicted_time": predicted_delete.get("time"),
            "predicted_space": predicted_delete.get("space"),
        })

        # --- SEARCH ---
        ll = LinkedList(initial_data)
        search_values = [random.randint(0, n * 2) for _ in range(trials_per_op)]

        start = time.perf_counter()
        for value in search_values:
            _ = ll.search(value)
        end = time.perf_counter()
        avg_search_time = (end - start) / trials_per_op

        predicted_search = predict_complexity("linked_list", "search") or {}
        results.append({
            "structure": "linked_list",
            "operation": "search",
            "n": n,
            "avg_time_seconds": avg_search_time,
            "predicted_time": predicted_search.get("time"),
            "predicted_space": predicted_search.get("space"),
        })

    return results


def plot_operation(results: List[BenchmarkRow], structure: str, operation: str) -> None:
    
    # Filter rows for this structure and operation
    filtered = [
        row for row in results
        if row["structure"] == structure and row["operation"] == operation
    ]

    if not filtered:
        print(f"No data to plot for {structure}.{operation}")
        return

    # Sort by n to get a clean line
    filtered.sort(key=lambda r: r["n"])

    ns = [row["n"] for row in filtered]
    times = [row["avg_time_seconds"] for row in filtered]

    plt.figure()
    plt.plot(ns, times, marker="o")
    plt.xlabel("Input size (n)")
    plt.ylabel("Average time per operation (seconds)")
    plt.title(f"{structure} - {operation} performance")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def run_all_benchmarks() -> List[BenchmarkRow]:
    
    input_sizes = [1_000, 5_000, 10_000, 20_000]

    results: List[BenchmarkRow] = []
    results.extend(benchmark_stack(input_sizes))
    results.extend(benchmark_queue(input_sizes))
    results.extend(benchmark_linked_list(input_sizes))

    return results


if __name__ == "__main__":
    
    all_results = run_all_benchmarks()

    
    plot_operation(all_results, "stack", "insert")
    plot_operation(all_results, "stack", "search")
    plot_operation(all_results, "queue", "insert")
    plot_operation(all_results, "linked_list", "search")
