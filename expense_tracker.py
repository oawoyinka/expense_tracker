import json

try:
    with open("output.json", "r") as json_file:
        expenses = json.load(json_file)
except FileNotFoundError:
    expenses = []

while True:
    print("Welcome to expense tracker!")
    print("---------------------------")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Spending by category")
    print("5. Delete expense")
    print("6. Exit")
    print("---------------------------")
    choice = input("Pick an option: ")

    if choice == "1":
        amount = input("Enter expense amount: ")
        amount = float(amount)
        category = input("Enter category: ")
        description = input("Enter description: ")
        print("---------------------------")
        print("Expense added successfully!")
    

        new_entry = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(new_entry)

        with open("output.json", "w") as json_file:
            json.dump(expenses, json_file, indent=4)
        break

    elif choice == "6":
        print("Thank you, see you another time!")
        break

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet")
            break
        else:
            for expense in expenses:
                amount = expense["amount"]
                category = expense["category"]
                description = expense["description"]
                print(f"Amount: {amount} | Category: {category} | Description: {description}")
            break

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print(f"Total spending: {total}")
        break
    elif choice == "4":
        if not expenses:
            print("No expenses recorded yet")
            break
        else:
            category_total = {}
            for expense in expenses:
                category = expense["category"]
                amount = expense["amount"]
                if category in category_total:
                    category_total[category] += amount
                else:
                    category_total[category] = amount
            for category, total in category_total.items():
                print(f"{category}: {total}")
            break
    elif choice == "5":
        if not expenses:
            print("No expenses recorded yet")

    else:
        print("Invalid option, choose between 1-6.")
        break