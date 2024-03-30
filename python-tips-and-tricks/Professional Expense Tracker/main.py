import sqlite3
import datetime

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

while True:
    print("select an option: ")
    print("1. enter a new expense")
    print("2. view expenses summary")

    choice = int(input())

    if choice == 1:
        date = input("enter the date of the expense (YYYY-MM-DD): ")
        description = input("enter the description of the expense: ")
        cur.execute("SELECT DISTINCT category FROM expenses")
        categories = cur.fetchall()
        print("select a category by number: ")
        for idx, category in enumerate(categories):
            print(f"{idx + 1}. {category[0]}")
        print(f"{len(categories) + 1}. Create a new category")

        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("enter the new category name: ")
        else:
            category = categories[category_choice - 1][0]

        price = input("enter the price of the expense: ")
        cur.execute("INSERT INTO expenses (Date, description, category, price) VALUES (?,?,?,?)", (date, description, category, price))
        conn.commit()

    elif choice == 2:
        print("select an option: ")
        print("1. enter a new expenses")
        print("2. view monthly expenses by categoty")

        view_choice = int(input())
        if view_choice == 1:
            cur.execute("SELECT * FROM expenses")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)
        elif view_choice == 2:
            month = input("enter the month (mm): ")
            year = input("enter the year (yyyy): ")
            cur.execute("""SELECT category, SUM(price) FROM expenses
                        WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ?
                        GROUP BY category""", (month, year))

            expenses = cur.fetchall()
            for expense in expenses:
                print(f"categoty: {expense[0]}, total: {expense[1]}")
        else:
            exit()
    else:
        exit()

    repeat = input("would you like to do something else (y/n)?\n")
    if repeat.lower() != "y":
        break

conn.close()

