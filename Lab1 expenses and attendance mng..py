"""Integrated Expense, Attendance, Grading & Billing Manager."""

expenses = []
records = []
students = []
bills = []


def main():
    while True:
        print("\nPress 1 Expense Management")
        print("Press 2 Attendance")
        print("Press 3 Grading")
        print("Press 4 Billing")
        print("Press 5 Reports View")
        print("Press 6 Exit")

        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Enter 1-6.")
            continue

        match user_input:
            case 1:
                expense_management()
            case 2:
                attendance()
            case 3:
                grading()
            case 4:
                billing()
            case 5:
                reportview()
            case 6:
                print("Thank you for using the system. Goodbye!")
                break
            case _:
                print("Invalid choice. Enter 1-6.")


def expense_management():
    desc = input("Description: ")
    cat = input("Category (Food/Travel/Utilities/Stationery/Other): ").title()
    if cat not in ["Food", "Travel", "Utilities", "Stationery", "Other"]:
        print("Choose a category from the list.")
        return
    try:
        amt = float(input("Amount: "))
    except ValueError:
        print("Amount must be a positive number.")
        return
    if amt <= 0:
        print("Amount must be a positive number.")
        return
    expenses.append((desc, cat, amt))
    print("Expense added successfully!")


def attendance():
    name = input("Name: ")
    try:
        total = int(input("Total days: "))
        present = int(input("Days present: "))
    except ValueError:
        print("Enter whole numbers only.")
        return
    if total < 1:
        print("Enter a whole number of at least 1.")
        return
    if present < 0 or present > total:
        print("Days present must be between 0 and", total)
        return
    pct = present / total * 100
    if pct >= 75:
        status = "Eligible"
    eli1f pct >= 60:
        status = "Warning"
    else:
        status = "Shortage"
    records.append((name, pct, status))
    print(f"{name}: {pct:.2f}% -> {status}")


def grading():
    name = input("Student name: ")
    total = 0
    fail = False
    for i in range(1, 6):
        try:
            m = float(input("Subject " + str(i) + " marks: "))
        except ValueError:
            print("Marks must be a number. Try again.")
            return
        if m < 0 or m > 100:
            print("Marks must be between 0 and 100.")
            return
        if m < 35:
            fail = True
        total = total + m
    pct = total / 5
    if pct >= 90:
        grade = "A+"
    elif pct >= 80:
        grade = "A"
    elif pct >= 70:
        grade = "B"
    elif pct >= 60:
        grade = "C"
    elif pct >= 50:
        grade = "D"
    elif pct >= 35:
        grade = "E"
    else:
        grade = "F"
    if fail:
        grade = "F"
    result = "FAIL" if grade == "F" else "PASS"
    students.append((name, pct, grade, result))
    print(f"Total: {total:.2f}/500  Percentage: {pct:.2f}%")
    print("Grade:", grade, " Result:", result)


def billing():
    customer = input("Customer name: ")
    subtotal = 0
    while True:
        item = input("Item name (type done to finish): ")
        if item.lower() == "done":
            break
        try:
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
        except ValueError:
            print("Enter valid numbers.")
            continue
        if price <= 0 or qty < 1:
            print("Price must be greater than 0 and quantity at least 1.")
            continue
        subtotal = subtotal + price * qty

    if subtotal == 0:
        print("No items added.")
        return

    if subtotal >= 10000:
        discount = subtotal * 0.15
    elif subtotal >= 5000:
        discount = subtotal * 0.10
    elif subtotal >= 1000:
        discount = subtotal * 0.05
    else:
        discount = 0
    taxable = subtotal - discount
    tax = taxable * 0.18
    grand = taxable + tax
    bills.append((customer, grand))
    print(f"Subtotal : {subtotal:.2f}")
    print(f"Discount : {discount:.2f}")
    print(f"Taxable  : {taxable:.2f}")
    print(f"Tax 18%  : {tax:.2f}")
    print(f"GRAND TOTAL: {grand:.2f}")


def reportview():
    print("\n--- EXPENSES ---")
    if not expenses:
        print("No records available.")
    for e in expenses:
        print(f"{e[0]:<15}{e[1]:<12}{e[2]:>10.2f}")

    print("\n--- ATTENDANCE ---")
    if not records:
        print("No records available.")
    for r in records:
        print(f"{r[0]:<15}{r[1]:>8.2f}%  {r[2]}")

    print("\n--- GRADING ---")
    if not students:
        print("No records available.")
    for s in students:
        print(f"{s[0]:<15}{s[1]:>8.2f}%  {s[2]}  {s[3]}")

    print("\n--- BILLING ---")
    if not bills:
        print("No records available.")
    for b in bills:
        print(f"{b[0]:<15}{b[1]:>10.2f}")


main()