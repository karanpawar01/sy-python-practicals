transactions = []

for i in range(5):
    amount = float(input(f"Enter transaction {i + 1}: "))
    transactions.append(amount)

largest = max(transactions)
average = sum(transactions) / len(transactions)

print(f"Largest transaction: {largest:.2f}")
print(f"Average spend: {average:.2f}")

