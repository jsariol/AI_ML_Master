# List example
fruits = ["apple", "banana", "cherry"] # fruits list is ['apple', 'banana', 'cherry']

# Insert an element at a specific position
fruits.insert(1, "orange")  # fruits list is now ['apple', 'orange', 'banana', 'cherry']

# Append an element at the end
fruits.append("grape")  # fruits list is now ['apple', 'orange', 'banana', 'cherry', 'grape']

# Update an element
fruits[2] = "blueberry"  # fruits list is now ['apple', 'orange', 'blueberry', 'cherry', 'grape']

# Remove an element by value
fruits.remove("cherry")  # fruits list is now ['apple', 'orange', 'blueberry', 'grape']

# Remove an element by index
del fruits[0]  # fruits list is now ['orange', 'blueberry', 'grape']


# Dictionary example
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Insert a new key-value pair
student["GPA"] = 3.8  
# {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'GPA': 3.8}

# Update an existing key
student["age"] = 22  
# {'name': 'Alice', 'age': 22, 'major': 'Computer Science', 'GPA': 3.8}

# Remove an element
del student["major"]  
# {'name': 'Alice', 'age': 22, 'GPA': 3.8}
