import random
from typing import List


def generate_dataset(size: int, kind: str) -> List[int]:
    """
    Generate a dataset of a given size and type.

    Args:
        size: Number of elements in the dataset.
        kind: One of:
            - "random": fully random values
            - "sorted": already sorted in non-decreasing order
            - "reverse": sorted in reverse (worst-case for some algorithms)
            - "partial": partially sorted (e.g., first half sorted)

    Returns:
        A list of integers representing the dataset.
    """
    if kind == "random":
        data = [random.randint(0, size * 10) for _ in range(size)]
    elif kind == "sorted":
        data = sorted(random.randint(0, size * 10) for _ in range(size))
    elif kind == "reverse":
        data = sorted(
            (random.randint(0, size * 10) for _ in range(size)),
            reverse=True,
        )
    elif kind == "partial":
        # First half sorted, second half random
        half = size // 2
        first_half = sorted(random.randint(0, size * 10) for _ in range(half))
        second_half = [random.randint(0, size * 10) for _ in range(size - half)]
        data = first_half + second_half
    else:
        raise ValueError(f"Unknown dataset type: {kind}")

    return data
