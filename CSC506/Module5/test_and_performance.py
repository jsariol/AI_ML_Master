
import random
import string
import time
from typing import List, Tuple

from hash_table import HashTable
from priority_queue import PriorityQueue


def make_random_key(prefix: str, length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    return prefix + "_" + "".join(random.choice(chars) for _ in range(length))


def linear_search(dataset: List[Tuple[str, int]], target_key: str):
    """O(n) search over list of (key, value)."""
    for k, v in dataset:
        if k == target_key:
            return v
    return None


def main():
    random.seed(42)

    # --- Build dataset (200 items) ---
    n_items = 200
    dataset: List[Tuple[str, int]] = []
    for i in range(n_items):
        key = make_random_key("user", 12)
        value = random.randint(1, 10_000)
        dataset.append((key, value))

    # --- Hash table test ---
    ht = HashTable(capacity=211)
    for k, v in dataset:
        ht.insert(k, v)

    
    sample_key = dataset[50][0]
    print("HashTable size:", len(ht))
    print("Search existing key:", sample_key, "->", ht.search(sample_key))
    print("Search missing key:", "user_DOES_NOT_EXIST", "->", ht.search("user_DOES_NOT_EXIST"))

    deleted = ht.delete(sample_key)
    print("Delete existing key:", sample_key, "->", deleted)
    print("Search after delete:", sample_key, "->", ht.search(sample_key))
    ht.insert(sample_key, 99999)
    print("Re-insert key:", sample_key, "->", ht.search(sample_key))

    # --- Priority queue test (min-heap) ---
    pq = PriorityQueue()
    for i, (k, v) in enumerate(dataset[:120]):  # 120 items
        priority = random.randint(1, 100)
        pq.insert(priority, (k, v))

    print("\nPriorityQueue size:", len(pq))
    print("Peek (min):", pq.peek())
    extracted = [pq.extract_min() for _ in range(5)]
    print("Extract 5 mins:", extracted)
    print("PriorityQueue size after extract:", len(pq))

    # Delete an arbitrary value payload
    to_delete_value = dataset[10][0]
    
    found = None
    for item in pq.heap:
        if item.value[0] == to_delete_value:
            found = item.value
            break
    if found:
        print("Delete from PQ by payload:", found, "->", pq.delete(found))
    else:
        print("Payload not found in PQ to delete (expected sometimes).")

    # --- Performance comparison: Hash vs Linear search ---
    # 10,000 searches: half hits, half misses.
    searches = 10_000
    hit_keys = [dataset[random.randint(0, n_items - 1)][0] for _ in range(searches // 2)]
    miss_keys = [make_random_key("miss", 12) for _ in range(searches // 2)]
    query_keys = hit_keys + miss_keys
    random.shuffle(query_keys)

    # Time hash table searches
    t0 = time.perf_counter()
    hit_count_ht = 0
    for key in query_keys:
        if ht.search(key) is not None:
            hit_count_ht += 1
    t1 = time.perf_counter()

    # Time linear searches
    t2 = time.perf_counter()
    hit_count_lin = 0
    for key in query_keys:
        if linear_search(dataset, key) is not None:
            hit_count_lin += 1
    t3 = time.perf_counter()

    print("\n--- Performance Results ---")
    print(f"Total queries: {len(query_keys)} (hits+misses)")
    print(f"Hash hits:   {hit_count_ht}")
    print(f"Linear hits: {hit_count_lin}")
    print(f"Hash search time:   {(t1 - t0):.6f} seconds")
    print(f"Linear search time: {(t3 - t2):.6f} seconds")

    
    print("\nBucket sizes (collision distribution):")
    print(ht.debug_bucket_sizes())


if __name__ == "__main__":
    main()
