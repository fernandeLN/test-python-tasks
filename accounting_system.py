"""
In this exercise, you are tasked to write a Python program that simulates operations on a company's account and a warehouse.
The program should handle various commands for performing operations like adding/subtracting balance, recording sales and purchases,
 displaying account balance, showing warehouse status, and reviewing recorded operations.

Instructions:

1. Write a program that displays available commands upon launch. The commands are:
  - balance
  - sale
  - purchase
  - account
  - list
  - warehouse
  - review
  - end

2. Handle each command uniquely:
  - 'balance': The program should prompt for an amount to add or subtract from the account.
  - 'sale': The program should prompt for the name of the product, its price, and quantity.
  Perform necessary calculations and update the account and warehouse accordingly.
  - 'purchase': The program should prompt for the name of the product, its price, and quantity.
  Perform necessary calculations and update the account and warehouse accordingly.
  Ensure that the account balance is not negative after a purchase operation.
  - 'account': Display the current account balance.
  - 'list': Display the total inventory in the warehouse along with product prices and quantities.
  - 'warehouse': Prompt for a product name and display its status in the warehouse.
  - 'review': Prompt for two indices 'from' and 'to', and display all recorded operations within that range.
  If ‘from’ and ‘to’ are empty, display all recorder operations. Handle cases where 'from' and 'to' values are out of range.
  - 'end': Terminate the program.

3. After executing any command, the program should again display the list of commands and prompt for the next command.

Hints:

- Use a loop to continuously prompt for commands until the 'end' command is entered.
- Keep track of the account balance and warehouse inventory.
- Remember to handle edge cases, like invalid command inputs, negative amounts during a 'purchase' operation, or out-of-range indices
during a 'review' operation.
- The balance, sale, and purchase commands are remembered by the program.
- Handle user inputs that are not as expected. The program should not crash in these cases, but instead, it should display an appropriate error message.
"""
print("Welcome to the accounting/warehouse system.\n")
balance = 0
operations = []
warehouse = {}

while True:
    print("These are the available commands: \nbalance -- sale -- purchase -- account -- list -- warehouse -- review -- end")
    command = input("From the available commands, enter one: ")
    list_of_commands = ["balance", "sale", "purchase", "account", "list", "warehouse", "review", "end"]
    if command.lower() not in list_of_commands:
        print("Invalid command. Please enter a valid one from the available commands.\n")
    else:
        if command.lower() == "balance":
            print("You have entered the BALANCE command.")
            amount = input("Enter the amount of the transaction - positive numbers for earnings and negative numbers for purchases :")
            try:
                amount = int(amount)
                print("The amount of the transaction is:", amount)
                balance += amount
                operations.append(("balance", amount))
            except ValueError:
                print("Invalid amount. Please enter a number.\n")
                continue

        elif command.lower() == "sale":
            name = input("Enter the name of the product: ")
            try:
                price = float(input("Enter the price of the product: "))
                quantity_input = int(input("Enter the quantity of the product: "))

                if (name in warehouse) and (warehouse[name]["quantity"] < quantity_input):
                    print("Not enough stock\n")
                elif name not in warehouse:
                    print(f" Product {name} not available in the inventory\n")
                else:
                    total_price = price * quantity_input
                    warehouse[name]["quantity"] -= quantity_input
                    balance += total_price
                    print(f"Sold {quantity_input} x {name} for a total of {total_price}\n")
                    operations.append(("sale", name, price, quantity_input))
            except ValueError:
                print("Invalid input. Please enter a number\n")

        elif command.lower() == "purchase":
            name = input("Enter the name of the product to purchase: ")
            try:
                price = float(input("Enter the price of the product: "))
                quantity_input = int(input("Enter the quantity of the product: "))
                total_price = price * quantity_input
                if balance < total_price:
                    print("Not enough funds\n")
                else:
                    balance -= total_price
                    if name in warehouse:
                        warehouse[name]["quantity"] += quantity_input
                        warehouse[name]["price"] = price
                    else:
                        warehouse[name] = {"quantity": quantity_input, "price": price}

                    print(f" {quantity_input} x {name} was purchased for a total of {total_price}\n")
                    operations.append(("purchase", name, price, quantity_input))
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        elif command.lower() == "list":
            if not warehouse:
                print("The warehouse is empty. Purchase new products first\n")
            else:
                print("Inventory")
                for name, info in warehouse.items():
                    print(f"Product: {name}\nQuantity: {info['quantity']}, Unit_Price: {info['price']}\n")
            operations.append("list")

        elif command.lower() == "account":
            operations.append("account")
            print(f"Your current account balance is {balance}")

        elif command.lower() == "warehouse":
            name = input("Enter the name of the product to display status: ")
            operations.append(("warehouse", name))
            if name not in warehouse:
                print(f"{name} was not found in the warehouse.\n")
            else:
                if warehouse[name]["quantity"] > 0:
                    print(f"Product {name} is available.\nQuantity: {warehouse[name]['quantity']} -- Unit_Price: {warehouse[name]['price']}\n")
                else:
                    print(f"Product {name} is out of stock.\n")

        elif command.lower() == "review":
            if not operations:
                print("No operations were performed.\n")
                continue

            first_index = input("Enter the starting index of the operation to review: ")
            last_index = input("Enter the last index of the operation to review: ")
            try:
                start = int(first_index) if first_index else 0
                end = int(last_index) if last_index else (len(operations)-1)

                if start < 0 or end < 0 or end >= len(operations) or start >= len(operations):
                    print("Index out of range.")
                elif start > end:
                    print("Start index cannot be greater than end index. Try again.\n")
                else:
                    for i, op in enumerate(operations[start:end+1], start=start):
                        print(i, op)
            except ValueError:
                print("Invalid input. Please enter numbers\n")

        elif command.lower() == "end":
            print("Closing the program. See you next time!")
            break