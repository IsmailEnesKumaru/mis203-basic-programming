total_price = 0
total_tickets = 0
total_free_tickets = 0

print("Welcome to the Ticket Office Program!\n")


while True:
    name = input("Enter the customer name or q to quit: ")
    name = name.lower()

    if name == 'q':
        break

    name = name.title()

    age = int(input("Enter the customer age: "))

    if age < 0 or age > 120:
        print("Invalid age. Please enter a valid age between 0 and 120.")
        continue

    day = input("Would you like to get a ticket for weekday or weekend? (Enter 'weekday' or 'weekend'): ")
    day = day.lower()

    if day not in ['weekday', 'weekend']:
        print("Invalid input. Please enter 'weekday' or 'weekend'.")
        continue

    student = input("Is the customer a student? (yes/no): ")
    student = student.lower()

    if student not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue

    wticket = 200
    eticket = 250

    if day == 'weekday':
        if age <= 6:
            price = 0
        elif age <= 12:
            price = wticket * 0.6
        elif student == 'yes' and age <= 25:
            price = wticket * 0.7
        elif age > 65:
            price = wticket * 0.5
        else:
            price = wticket

    elif day == 'weekend':
        if age <= 6:
            price = 0
        elif age <= 12:
            price = eticket * 0.6
        elif student == 'yes' and age <= 25:
            price = eticket * 0.7
        elif age > 65:
            price = eticket * 0.5
        else:
            price = eticket

    if student == 'yes' and age <= 25 and age > 12:
        print(f"{name} : {price:.2f} TRY (Student)")
    elif age <= 6:
        print(f"{name} : {price:.2f} TRY (Free)")
    elif age > 65:
        print(f"{name} : {price:.2f} TRY (Senior)")
    elif age <= 12:
        print(f"{name} : {price:.2f} TRY (Child)")
    else:
        print(f"{name} : {price:.2f} TRY (Standard)")

    total_price += price
    total_tickets += 1

    if age <= 6:
        total_free_tickets += 1


if total_tickets == 0:
    print("\nNo tickets were sold.")
else:
    print(f"\nTickets sold: {total_tickets}")
    print(f"Total revenue: {total_price:.2f} TRY")
    print(f"Average price: {total_price / total_tickets:.2f} TRY")
    print(f"Free tickets: {total_free_tickets}")

print("\nExiting the ticket office program. Goodbye!")
