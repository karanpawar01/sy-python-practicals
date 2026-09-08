purchase_amount = float(input("Enter total purchase amount: "))
discount_percent = float(input("Enter discount percentage: "))


discount_amount = purchase_amount * discount_percent / 100
final_amount = purchase_amount - discount_amount


print("\n" + "=" * 45)
print("             BILLING SUMMARY")
print("=" * 45)
print(f"{'Purchase Amount':<25} ₹{purchase_amount:>10.2f}")
print(f"{'Discount Percentage':<25} {discount_percent:>10.2f}%")
print(f"{'Discount Amount':<25} ₹{discount_amount:>10.2f}")
print("-" * 45)
print(f"{'Final Payable Amount':<25} ₹{final_amount:>10.2f}")
print("=" * 45)
