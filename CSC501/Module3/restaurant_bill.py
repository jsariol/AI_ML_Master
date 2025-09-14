food_charge = float(input("Enter the cost of the meal: $"))
tip = food_charge * 0.18
sales_tax = food_charge * 0.07
total_price = food_charge + tip + sales_tax

print("\n    --- Receipt ---")
print("Meal cost:      $", format(food_charge, ".2f"))
print("Tip (18%):      $", format(tip, ".2f"))
print("Sales tax (7%): $", format(sales_tax, ".2f"))
print("Total:          $", format(total_price, ".2f"))
