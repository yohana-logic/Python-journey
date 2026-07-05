expenses = []

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expenses.append({
            "amount": amount,
            "category": category
        })

        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. Amount: ${expense['amount']} | "
                    f"Category: {expense['category']}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")