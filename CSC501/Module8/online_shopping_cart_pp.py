#Milestone 1

#Class deffinition
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    # Method to print item cost. I wanted to format the output to have 2 decimal places so it reflects a price in a more realistic way. It also manages a 
    # scenario where the item price has a decimal value like $4.50 or $19.99
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

#Here I wanted to play with the formatting of the output. I used f-strings to format the output and center it. I also used max_width to ensure that the output is aligned properly.
line1 = f"{item1.item_name} {item1.item_quantity} @ ${item1.item_price:.2f} = ${item1.item_price * item1.item_quantity:.2f}"
line2 = f"{item2.item_name} {item2.item_quantity} @ ${item2.item_price:.2f} = ${item2.item_price * item2.item_quantity:.2f}"
max_width = max(len(line1), len(line2))

print("\n" + "TOTAL COST".center(max_width))
item1.print_item_cost()
item2.print_item_cost()

total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(("Total: $" + f"{total:.2f}").center(max_width)+ "\n")



#Milestone 2

#ShoppingCart Class deffinition
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

#Add item to cart method.
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

#Remove item from cart method.
    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

#Modify item in cart method.
    def modify_item(self, item_to_modify):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

#Get number of items in cart method.
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

#Get cost of cart method.
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

#Print total method.
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                total_price = item.item_price * item.item_quantity
                print(f"{item.item_name} {item.item_quantity} @ ${int(item.item_price)} = ${int(total_price)}")
            print(f"Total: ${int(self.get_cost_of_cart())}")

#Print descriptions method.
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

#Print menu method.
def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    command = ""

    while command != "q":
        print(menu)
        command = input("Choose an option:\n").lower()

        if command == "a":
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase()
            new_item.item_name = item_name
            new_item.item_description = item_description
            new_item.item_price = item_price
            new_item.item_quantity = item_quantity
            cart.add_item(new_item)

        elif command == "r":
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

        elif command == "c":
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            modified_item = ItemToPurchase()
            modified_item.item_name = item_name
            modified_item.item_quantity = new_quantity
            cart.modify_item(modified_item)

        elif command == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif command == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif command == "q":
            # Quit — do nothing, loop will end
            pass
        else:
            # Invalid option, re-display menu
            continue

def main():
    print("Enter customer's name:")
    customer_name = input()
    if not customer_name.strip():
        customer_name = "none"
    print("Enter today's date:")
    current_date = input()
    if not current_date.strip():
        current_date = "January 1, 2020"

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()
