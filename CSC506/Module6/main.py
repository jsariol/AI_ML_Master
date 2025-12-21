import random
import time
from typing import List

from bst_map import BSTMap
from list_map import ListMap


def demo_bst_map_integers() -> None:
    print("\n=== Demo: BSTMap with integer keys (50 items) ===")
    bst_map = BSTMap()

    keys = random.sample(range(1, 1000), 50)
    for k in keys:
        bst_map.set(k, f"value_{k}")

    print("Min item:", bst_map.min_item())
    print("Max item:", bst_map.max_item())
    print("Is balanced?:", bst_map.is_balanced())

    print("\nIn-order (first 10):", list(bst_map.items_inorder())[:10])
    print("Pre-order (first 10):", list(bst_map.items_preorder())[:10])
    print("Post-order (first 10):", list(bst_map.items_postorder())[:10])

    target = keys[10]
    print(f"\nSearch key {target} =>", bst_map.get(target))

    deleted_key = keys[20]
    print(f"Delete key {deleted_key} =>", bst_map.delete(deleted_key))
    print("Contains deleted key?:", bst_map.contains(deleted_key))

    print("\nASCII tree (after insertions/deletion):")
    print(bst_map.ascii_tree())


def demo_bst_map_strings() -> None:
    print("\n=== Demo: BSTMap with string keys (50 items) ===")
    bst_map = BSTMap()

    keys = [f"key_{i:03d}" for i in range(50)]
    random.shuffle(keys)

    for k in keys:
        bst_map.set(k, f"value_for_{k}")

    print("Min item:", bst_map.min_item())
    print("Max item:", bst_map.max_item())
    print("Is balanced?:", bst_map.is_balanced())

    print("\nIn-order (first 10):", list(bst_map.items_inorder())[:10])


def performance_comparison_search(iterations: int = 20000) -> None:
    print("\n=== Performance: BSTMap vs ListMap (search) ===")
    bst_map = BSTMap()
    list_map = ListMap()

    # Build same dataset
    keys = random.sample(range(1, 200000), 5000)
    for k in keys:
        bst_map.set(k, k)
        list_map.set(k, k)

    # Search targets: mix of hits and misses
    targets: List[int] = []
    for _ in range(iterations):
        if random.random() < 0.8:
            targets.append(random.choice(keys))  # hit
        else:
            targets.append(random.randint(200001, 300000))  # miss

    # Time BSTMap contains
    start = time.perf_counter()
    hit_count_bst = 0
    for t in targets:
        if bst_map.contains(t):
            hit_count_bst += 1
    end = time.perf_counter()
    bst_time = end - start

    # Time ListMap contains
    start = time.perf_counter()
    hit_count_list = 0
    for t in targets:
        if list_map.contains(t):
            hit_count_list += 1
    end = time.perf_counter()
    list_time = end - start

    print(f"BSTMap hits:  {hit_count_bst} | time: {bst_time:.6f}s")
    print(f"ListMap hits: {hit_count_list} | time: {list_time:.6f}s")
    if bst_time > 0:
        print(f"Speedup (List / BST): {list_time / bst_time:.2f}x")


def main() -> None:
    random.seed(42)
    demo_bst_map_integers()
    demo_bst_map_strings()
    performance_comparison_search(iterations=20000)


if __name__ == "__main__":
    main()
