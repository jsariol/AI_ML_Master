"""
Set Operations
==============

Comprehensive Set class implementation supporting all fundamental set operations:
- Union
- Intersection
- Difference
- Symmetric Difference

Also includes static methods for batch operations and performance optimized implementations.
"""

from typing import Iterable, Set as PySet, List, Optional


class Set:
    """
    A custom Set implementation supporting all standard set operations.
    
    This class demonstrates understanding of set theory and efficient implementations
    of set operations. It tracks all operations for performance analysis.
    
    Attributes:
        elements: Internal storage of set elements
        operation_count: Total number of operations performed
    """
    
    def __init__(self, iterable: Optional[Iterable] = None):
        """
        Initialize a Set from an iterable.
        
        Args:
            iterable: Optional iterable to initialize the set with
        """
        self.elements: PySet = set()
        self.operation_count = 0
        
        if iterable is not None:
            for item in iterable:
                self.elements.add(item)
    
    def add(self, item) -> None:
        """Add an element to the set."""
        self.elements.add(item)
        self.operation_count += 1
    
    def remove(self, item) -> None:
        """Remove an element from the set. Raises KeyError if not found."""
        self.elements.remove(item)
        self.operation_count += 1
    
    def discard(self, item) -> None:
        """Remove an element if it exists (no error if not found)."""
        self.elements.discard(item)
        self.operation_count += 1
    
    def contains(self, item) -> bool:
        """Check if an element is in the set."""
        self.operation_count += 1
        return item in self.elements
    
    def is_empty(self) -> bool:
        """Check if the set is empty."""
        return len(self.elements) == 0
    
    def size(self) -> int:
        """Return the number of elements in the set."""
        return len(self.elements)
    
    def clear(self) -> None:
        """Remove all elements from the set."""
        self.elements.clear()
        self.operation_count += 1
    
    def copy(self) -> 'Set':
        """Return a shallow copy of the set."""
        new_set = Set()
        new_set.elements = self.elements.copy()
        return new_set
    
    def to_list(self) -> List:
        """Convert set to list."""
        return list(self.elements)
    
    # ========== SET OPERATIONS ==========
    
    def union(self, other: 'Set') -> 'Set':
        """
        Return a new set with all elements from both sets.
        
        Union: A ∪ B = {x | x ∈ A or x ∈ B}
        
        Time Complexity: O(n + m) where n, m are sizes of sets
        """
        if not isinstance(other, Set):
            raise TypeError("Operand must be a Set")
        
        result = Set()
        result.elements = self.elements.union(other.elements)
        result.operation_count = self.operation_count + other.operation_count + 1
        return result
    
    def intersection(self, other: 'Set') -> 'Set':
        """
        Return a new set with elements common to both sets.
        
        Intersection: A ∩ B = {x | x ∈ A and x ∈ B}
        
        Time Complexity: O(min(n, m)) where n, m are sizes of sets
        """
        if not isinstance(other, Set):
            raise TypeError("Operand must be a Set")
        
        result = Set()
        result.elements = self.elements.intersection(other.elements)
        result.operation_count = self.operation_count + other.operation_count + 1
        return result
    
    def difference(self, other: 'Set') -> 'Set':
        """
        Return a new set with elements in this set but not in other.
        
        Difference: A - B = {x | x ∈ A and x ∉ B}
        
        Time Complexity: O(n) where n is size of this set
        """
        if not isinstance(other, Set):
            raise TypeError("Operand must be a Set")
        
        result = Set()
        result.elements = self.elements.difference(other.elements)
        result.operation_count = self.operation_count + other.operation_count + 1
        return result
    
    def symmetric_difference(self, other: 'Set') -> 'Set':
        """
        Return a new set with elements in either set but not both.
        
        Symmetric Difference: A Δ B = {x | (x ∈ A and x ∉ B) or (x ∈ B and x ∉ A)}
                            = (A - B) ∪ (B - A)
        
        Time Complexity: O(n + m) where n, m are sizes of sets
        """
        if not isinstance(other, Set):
            raise TypeError("Operand must be a Set")
        
        result = Set()
        result.elements = self.elements.symmetric_difference(other.elements)
        result.operation_count = self.operation_count + other.operation_count + 1
        return result
    
    # ========== SUBSET/SUPERSET OPERATIONS ==========
    
    def is_subset(self, other: 'Set') -> bool:
        """
        Check if this set is a subset of other.
        
        A ⊆ B means every element of A is in B
        """
        if not isinstance(other, Set):
            raise TypeError("Operand must be a Set")
        
        return self.elements.issubset(other.elements)
    
    def is_superset(self, other: 'Set') -> bool:
        """
        Check if this set is a superset of other.
        
        A ⊇ B means this set contains all elements of B
        """
        if not isinstance(other, Set):
            raise TypeError("Operand must be a Set")
        
        return self.elements.issuperset(other.elements)
    
    def is_disjoint(self, other: 'Set') -> bool:
        """
        Check if this set has no elements in common with other.
        
        A and B are disjoint if A ∩ B = ∅
        """
        if not isinstance(other, Set):
            raise TypeError("Operand must be a Set")
        
        return self.elements.isdisjoint(other.elements)
    
    # ========== STATIC METHODS FOR BATCH OPERATIONS ==========
    
    @staticmethod
    def union_all(sets: List['Set']) -> 'Set':
        """
        Return the union of multiple sets.
        
        Time Complexity: O(n₁ + n₂ + ... + nₖ)
        """
        if not sets:
            return Set()
        
        result = sets[0].copy()
        for s in sets[1:]:
            result = result.union(s)
        
        return result
    
    @staticmethod
    def intersection_all(sets: List['Set']) -> 'Set':
        """
        Return the intersection of multiple sets.
        
        Time Complexity: O(n₁ + n₂ + ... + nₖ)
        """
        if not sets:
            return Set()
        
        result = sets[0].copy()
        for s in sets[1:]:
            result = result.intersection(s)
        
        return result
    
    # ========== UTILITY METHODS ==========
    
    def __repr__(self) -> str:
        """String representation of the set."""
        return f"Set({sorted(self.elements) if all(isinstance(x, (int, float, str)) for x in self.elements) else self.elements})"
    
    def __str__(self) -> str:
        """String representation of the set."""
        elements_str = ', '.join(str(x) for x in sorted(self.elements) if isinstance(x, (int, float, str)))
        return "{" + elements_str + "}"
    
    def __len__(self) -> int:
        """Return the number of elements in the set."""
        return len(self.elements)
    
    def __iter__(self):
        """Iterate over set elements."""
        return iter(self.elements)
    
    def __eq__(self, other) -> bool:
        """Check if two sets are equal."""
        if not isinstance(other, Set):
            return False
        return self.elements == other.elements
    
    def __and__(self, other) -> 'Set':
        """Support & operator for intersection."""
        return self.intersection(other)
    
    def __or__(self, other) -> 'Set':
        """Support | operator for union."""
        return self.union(other)
    
    def __sub__(self, other) -> 'Set':
        """Support - operator for difference."""
        return self.difference(other)
    
    def __xor__(self, other) -> 'Set':
        """Support ^ operator for symmetric difference."""
        return self.symmetric_difference(other)


def interactive_set_demo() -> None:
    """Interactive console demo for Set operations."""
    print("\n" + "=" * 80)
    print("SET OPERATIONS INTERACTIVE DEMO")
    print("=" * 80)
    
    set_a = Set()
    set_b = Set()
    
    while True:
        print("\nOptions:")
        print("1. Create/modify Set A")
        print("2. Create/modify Set B")
        print("3. Union (A ∪ B)")
        print("4. Intersection (A ∩ B)")
        print("5. Difference (A - B)")
        print("6. Symmetric Difference (A Δ B)")
        print("7. Check subset/superset/disjoint")
        print("8. Show current sets")
        print("9. Clear all sets")
        print("10. Exit")
        
        choice = input("\nEnter choice (1-10): ").strip()
        
        if choice == "1":
            try:
                input_str = input("Enter elements separated by spaces: ").strip()
                set_a = Set(input_str.split())
                print(f"Set A created: {set_a}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                input_str = input("Enter elements separated by spaces: ").strip()
                set_b = Set(input_str.split())
                print(f"Set B created: {set_b}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            result = set_a.union(set_b)
            print(f"\nA ∪ B = {result}")
            print(f"Elements: {sorted(result.to_list())}")
        
        elif choice == "4":
            result = set_a.intersection(set_b)
            print(f"\nA ∩ B = {result}")
            print(f"Elements: {sorted(result.to_list())}")
        
        elif choice == "5":
            result = set_a.difference(set_b)
            print(f"\nA - B = {result}")
            print(f"Elements: {sorted(result.to_list())}")
        
        elif choice == "6":
            result = set_a.symmetric_difference(set_b)
            print(f"\nA Δ B = {result}")
            print(f"Elements: {sorted(result.to_list())}")
        
        elif choice == "7":
            print(f"\nA ⊆ B (A is subset of B): {set_a.is_subset(set_b)}")
            print(f"A ⊇ B (A is superset of B): {set_a.is_superset(set_b)}")
            print(f"A ∩ B = ∅ (disjoint): {set_a.is_disjoint(set_b)}")
        
        elif choice == "8":
            print(f"\nSet A: {set_a}")
            print(f"Set B: {set_b}")
        
        elif choice == "9":
            set_a.clear()
            set_b.clear()
            print("\nAll sets cleared")
        
        elif choice == "10":
            break
        
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    interactive_set_demo()
