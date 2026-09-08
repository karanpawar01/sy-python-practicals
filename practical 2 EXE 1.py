# Grocery Bill Program

items = []

for i in range(3):
    print(f"\nEnter details for item {i + 1}:")
    name = input("Item name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per item: "))

    amount = quantity * price
    items.append((name, quantity, price, amount))

# Display bill
print("\n" + "=" * 50)
print("                 GROCERY BILL")
print("=" * 50)
print(f"{'Item':<15}{'Qty':>8}{'Price':>12}{'Amount':>15}")
print("-" * 50)

total = 0

for name, quantity, price, amount in items:
    print(f"{name:<15}{quantity:>8}{price:>12.2f}{amount:>15.2f}")
    total += amount

print("-" * 50)
print(f"{'TOTAL BILL':<35}{total:>15.2f}")
print("=" * 50)
 