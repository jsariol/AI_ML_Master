#Class deffinition
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    # Method to print item cost
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")


# Main program

print("Item 1")
item1 = ItemToPurchase()
item1.item_name = input("Enter the item name:\n")
item1.item_price = float(input("Enter the item price:\n"))
item1.item_quantity = int(input("Enter the item quantity:\n"))


print("\nItem 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter the item name:\n")
item2.item_price = float(input("Enter the item price:\n"))
item2.item_quantity = int(input("Enter the item quantity:\n"))

#Dr Gang, here I wanted to play with the formatting of the output. I used f-strings to format the output and center it. I also used max_width to ensure that the output is aligned properly.
line1 = f"{item1.item_name} {item1.item_quantity} @ ${item1.item_price:.2f} = ${item1.item_price * item1.item_quantity:.2f}"
line2 = f"{item2.item_name} {item2.item_quantity} @ ${item2.item_price:.2f} = ${item2.item_price * item2.item_quantity:.2f}"
max_width = max(len(line1), len(line2))

print("\n" + "TOTAL COST".center(max_width))
item1.print_item_cost()
item2.print_item_cost()

total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print("\n" + ("Total: $" + f"{total:.2f}").center(max_width))
