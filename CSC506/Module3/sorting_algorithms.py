from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    
    n = len(arr)
    # Work on a copy to avoid mutating the caller's data
    a = arr[:]

    for i in range(n):
        # After each pass, the largest element "bubbles up" to the end
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        # Optimization: if no swaps were made, the list is already sorted
        if not swapped:
            break
    return a


def selection_sort(arr: List[int]) -> List[int]:

    n = len(arr)
    a = arr[:]

    for i in range(n):
        min_index = i
        # Find the index of the minimum element in the remaining subarray
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        a[i], a[min_index] = a[min_index], a[i]
    return a


def insertion_sort(arr: List[int]) -> List[int]:
    
    a = arr[:]

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        # Shift elements of the sorted segment to the right
        # to make room for the key
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
    return a


def merge_sort(arr: List[int]) -> List[int]:
    
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """
    Helper function to merge two sorted lists into one sorted list.
    """
    merged: List[int] = []
    i = 0
    j = 0

    # Merge while both lists have elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged
