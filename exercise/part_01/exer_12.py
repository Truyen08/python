## tinh' tong? tien` bill (co' tax + tip)
meal_cost = float(input("Enter meal cost: "))
tax = 0.05 * meal_cost
tip = 0.18 * meal_cost
total = meal_cost + tax + tip

print(f"Meal cost: ${meal_cost:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Total: ${total:.2f}")
