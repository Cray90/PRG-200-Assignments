# ATM Withdrawal Validator

balance = int(input("Enter your account balance (NPR): "))
daily_withdrawn = int(input("Enter amount already withdrawn today (NPR): "))
amount = int(input("Enter withdrawal amount (NPR): "))

if amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")

elif amount > balance:
    print("Insufficient balance.")

elif daily_withdrawn + amount > 50000:
    print("Daily withdrawal limit reached.")

else:
    balance = balance - amount
    print("Withdrawal successful.")
    print("Your current balance after withdrawal: NPR", balance)