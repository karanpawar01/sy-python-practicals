status=input("Enter your order status(shipped/delivered/shiping):").lower()

if status == "shipped":
    print("Your orded has been shipped and is on its way...")
elif status == "delivered":
    print("Your ordered has been delivered successfully...")
elif status == "pending":
    print("Your ordered is pending and will be processed soon...")
else:
    print("Invalid status. Please enter shiped , delevered, or Pending")