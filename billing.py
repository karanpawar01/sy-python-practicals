print("*=======billing details=========*")

rice_qty=float(input("enter the qty of rice:"))
rice_price_per_kg=50
rice_total=rice_qty*rice_price_per_kg

sugar_qty=float(input("enter the quantity of sugar:"))
sugar_price_per_kg=100
sugar_total=sugar_qty*sugar_price_per_kg

oil_qty=float(input("enter the quantity of oil :"))
oil_price_per_kg=150
oil_total=oil_qty*oil_price_per_kg

print("=====total amount=====")

print("rice",rice_total)
print("sugar",sugar_total)
print("oil",oil_total)

total_bill=rice_total+sugar_total+oil_total

print("total bill",total_bill)
discount=0
if total_bill>=1000:
    discount=total_bill*0.1
  print("discount",discount) 
elif total_bill>=500:
    discount=total_bill*0.5
    print("discount",discount) 
else:
    print("no discount",discount)
    
    final_bill=total_bill-discount
    print("final_bill",total_bill)