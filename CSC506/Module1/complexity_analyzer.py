from typing import Dict, Optional

ComplexityInfo = Dict[str, str]

# Central map of predicted complexities.
COMPLEXITY_MAP: Dict[str, Dict[str, ComplexityInfo]] = {
    "stack": {        
        "push": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Add item to the top of the stack.",
        },
        "pop": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Remove item from the top of the stack.",
        },
        "peek": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Read the top item without removing it.",
        },
        "search": {
            "time": "O(n)",
            "space": "O(1)",
            "notes": "Linear scan through all elements.",
        },        
        "insert": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Modeled as push to the top.",
        },
        "delete": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Modeled as pop from the top.",
        },
    },
    "queue": {        
        "enqueue": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Add item to the back of the queue.",
        },
        "dequeue": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Remove item from the front of the queue.",
        },
        "peek": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Read the front item without removing it.",
        },
        "search": {
            "time": "O(n)",
            "space": "O(1)",
            "notes": "Linear scan through all elements.",
        },
        "insert": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Modeled as enqueue at the back.",
        },
        "delete": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Modeled as dequeue from the front.",
        },
    },
    "linked_list": {        
        "insert_at_head": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Insert new node at the beginning of the list.",
        },
        "append": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Insert new node at the end (tail) of the list.",
        },
        "search": {
            "time": "O(n)",
            "space": "O(1)",
            "notes": "Traverse nodes from head until value is found.",
        },
        "delete": {
            "time": "O(n)",
            "space": "O(1)",
            "notes": "Need to find the node and update links.",
        },        
        "insert": {
            "time": "O(1)",
            "space": "O(1)",
            "notes": "Modeled as insert_at_head or append.",
        },
    },
}


def normalize_structure_name(structure_name: str) -> str:

    name = structure_name.strip().lower()
    if name in COMPREHENSION_ALIASES:
        return COMPREHENSION_ALIASES[name]
    return name



COMPREHENSION_ALIASES: Dict[str, str] = {
    "stack": "stack",
    "queue": "queue",
    "linked list": "linked_list",
    "linkedlist": "linked_list",
    "list": "linked_list",  
}


def predict_complexity(structure_name: str, operation: str) -> Optional[ComplexityInfo]:
    
    struct_key = normalize_structure_name(structure_name)
    op_key = operation.strip().lower()

    structure_info = COMPLEXITY_MAP.get(struct_key)
    if structure_info is None:
        return None

    return structure_info.get(op_key)


def format_complexity(structure_name: str, operation: str) -> str:
    
    info = predict_complexity(structure_name, operation)
    if info is None:
        return (
            f"No complexity information available for "
            f"structure='{structure_name}', operation='{operation}'."
        )

    struct_key = normalize_structure_name(structure_name)
    op_key = operation.strip().lower()

    time = info.get("time", "N/A")
    space = info.get("space", "N/A")
    notes = info.get("notes", "")

    return (
        f"Predicted complexity for {struct_key}.{op_key}:\n"
        f"  Time:  {time}\n"
        f"  Space: {space}\n"
        f"  Notes: {notes}"
    )
