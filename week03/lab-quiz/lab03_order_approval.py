order = float(input("Enter order amount (TRY): "))
stock = int(input("Enter available stock: "))
quantity = int(input("Enter requested quantity: "))
member = input("Is the customer a member? (yes/no): ").lower()

if quantity <= 0:
    print("Order rejected: Quantity must be greater than 0.")

elif quantity > stock:
    print("Order rejected: Insufficient stock.")

else:
    print("Order approved: Quantity is valid and stock is available.")

    final_price = order

    if member == "yes" and order >= 500:
        final_price = order * 0.90
        print("Member discount applied: 10%")

    print("Final price:", final_price, "TRY")
