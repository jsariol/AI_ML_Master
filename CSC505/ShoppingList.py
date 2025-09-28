"""
Prototype Pages Printer
- Prints the page names, number of pages, and a simple flow for the shopping list app paper prototype.
"""

PAGES = [
    ("S1", "Lists (Home)"),
    ("S2", "List Detail"),
    ("S3", "Add/Edit Item"),
    ("S4", "Search/Filter"),
    ("S5", "Settings"),
]

FLOW = [
    "S1 -> S2",
    "S2 -> S3",
    "S3 -> S2",
    "S2 -> S4",
    "S4 -> S2",
    "S1 -> S5",
    "S5 -> S1",
]

def main():
    print("=== Shopping List App — Paper Prototype ===\n")
    print("Pages:")
    for pid, name in PAGES:
        print(f"  {pid}: {name}")
    print(f"\nTotal pages: {len(PAGES)}\n")

    print("Sequence / Flow:")
    for step in FLOW:
        print(f"  {step}")

    
    graph = {
        "S1": ["S2", "S5"],
        "S2": ["S3", "S4"],
        "S3": ["S2"],
        "S4": ["S2"],
        "S5": ["S1"],
    }
    print("\nAdjacency:")
    for k, v in graph.items():
        print(f"  {k} -> {', '.join(v)}")

if __name__ == "__main__":
    main()
