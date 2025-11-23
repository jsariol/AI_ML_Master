from typing import List, Any, Optional


def linear_search(arr: List[Any], target: Any) -> Optional[int]:    
    
    for index, value in enumerate(arr):
        if value == target:
            return index
    return None
