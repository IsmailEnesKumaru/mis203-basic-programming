item1 = input("First item name: ")
quantity1 = int(input("Quantity: "))
price1 = int(input("Unit Price: "))
item2 = input("Second item name: ")
quantity2 = int(input("Quantity: "))           #We must convert input before aritmethic because input takes numbers as a string.
price2 = int(input("Unit Price: "))

delivery=int(input("Delivery Fee: "))
taxp = int(input("Tax Percentage: "))

line1 = quantity1*price1
line2 = quantity2*price2
subtotal = line1 + line2
tax = subtotal * (taxp/100)
total = subtotal + tax + delivery

print(f"{item1}: {quantity1} x {price1:.2f} = {line1:.2f}")
print(f"{item2}: {quantity2} x {price2:.2f} = {line2:.2f}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Delivery Fee: {delivery:.2f}")
print(f"Total: {total:.2f}")

