# Online Store Discount System

purchase = float(input("Enter total purchase amount (NPR): "))
member = input("Are you a loyalty member? (yes/no): ")

discount = 0

if purchase < 1000:
    discount = 0

elif purchase < 5000:
    discount = 5

elif purchase < 15000:
    discount = 10

else:
    discount = 20

discount_amount = purchase * discount / 100
price_after_discount = purchase - discount_amount

# Extra 5% discount for loyalty members
if member.lower() == "yes":
    extra_discount = price_after_discount * 5 / 100
    final_price = price_after_discount - extra_discount
else:
    final_price = price_after_discount

print("Final payable amount: NPR", final_price)