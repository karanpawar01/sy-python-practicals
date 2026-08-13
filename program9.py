print("************ CALCULATOR *********************")

customer_name=input(" Enter customer  name :")

item1 = input(" enter the 1 item :")
price1 = float( input(" Enter price :"))
qty1 = int(input(" Enter Quantity"))
amount1 = price1 * qty1

item2 = input( " Enter the 2 item :")
price2 = float(input(" Enter the price :"))
qyt2 = int(input(" Enter Quantity :"))
amount2 = price2 * qyt2

item3 = input( " Enter 3 item :")
price3 = float(input(" Enter price :2"))
qyt3 = int(input(" Enter Quantity :"))
amount3 = price3 *  qyt3
total_bill = amount1 + amount2 + amount3

if(total_bill >= 5000):
     discount = total_bill * 0.30
elif( total_bill >= 3000):
     discount = total_bill * 0.20

elif( total_bill >= 1000):
     discount = total_bill * 0.10
else:
     discount = 0

final_amount = total_bill - discount


print("\n========= CUSTOMER BILL============")
print(customer_name," your bill  :")
print(" total bill    :",total_bill)
print(" discount   :",discount)
print(" final amount :", final_amount)

print("******************* THANK YOU VISIT AGAIN **********")