item_name = input("Enter food item name:\n")
item_price = float(input("Enter item price:\n"))
item_quantity = int(input("Enter item quantity:\n"))

print("\nRECEIPT")
print(f"{item_quantity} {item_name} @ ${item_price:.2f} = ${item_quantity * item_price:.2f}")
print(f"Total cost: ${item_quantity * item_price:.2f}")

print()  # <-- línea en blanco

item2_name = input("Enter second food item name:\n")
item2_price = float(input("Enter item price:\n"))
item2_quantity = int(input("Enter item quantity:\n"))

print("\nRECEIPT")
print(f"{item_quantity} {item_name} @ ${item_price:.2f} = ${item_quantity * item_price:.2f}")
print(f"{item2_quantity} {item2_name} @ ${item2_price:.2f} = ${item2_quantity * item2_price:.2f}")

total_cost = (item_quantity * item_price) + (item2_quantity * item2_price)
gratuity = total_cost * 0.15
total_with_tip = total_cost + gratuity

print(f"Total cost: ${total_cost:.2f}")

print()  # <-- línea en blanco

print(f"15% gratuity: ${gratuity:.2f}")
print(f"Total with tip: ${total_with_tip:.2f}")