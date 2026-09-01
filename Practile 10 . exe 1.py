costs = [1250.75, 890.50, 2450.00, 675.25, 3100.80, 1500.40]

costs.sort(reverse=True)

print("Prices from highest to lowest:")
for cost in costs:
    print(f"{cost:.2f}")

print("\nTop 3 priciest entries:")
for cost in costs[:3]:
    print(f"{cost:.2f}")