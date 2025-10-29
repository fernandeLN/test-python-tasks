"""
In this exercise, you'll extend the functionality of the company account and warehouse operations program from the previous lesson.
You'll implement saving and loading of
account balance ,
warehouse inventory, and
operation history to/from a text file.

1. You can store balance, inventory and history in separate files or in one file.

2. At the start of the program, if the file(s) exists, load the data from the file and use it to initialize the program state.
  - If the file does not exist or if there are any errors during file reading (e.g., the file is corrupted or not readable),
  handle these cases gracefully.
  - Make sure to save all the data to correct files when the program is being shutdown.

Hints:

- Use built-in Python functions for file I/O and converting data to Python objects (i.e. literal_eval).
- Remember to handle any file I/O errors that may occur.
- Think about the format in which you'll save the data to the file. The format should be easy to read back into the program.
- Always close the files after you're done with them to free up system resources.

"""

from ast import literal_eval

# store data in separate files "balance.txt - inventory.txt - history.txt"
print("Welcome to the accounting/warehouse system.\n")
# We need to load the data from the files if they exist, and if not, start from standard values
# We can write try/except for each file "balance.txt - inventory.txt - history.txt" or define a function to avoid repetition

def data_loading(filename,default_value):
    try:
        with open(filename,'r') as f:
            data = literal_eval(f.read())
            if not data :
                return default_value
            return data
    except (FileNotFoundError, ValueError, SyntaxError):
        return default_value

def data_saving(filename,data):
    with open(filename,'w') as f:
        f.write(str(data))
# balance.txt
balance = data_loading("balance.txt",0)

# inventory.txt
warehouse = data_loading("inventory.txt", {})

# history.txt
operations = data_loading("history.txt", [])


while True:
    print("These are the available commands: \nbalance -- sale -- purchase -- account -- list -- warehouse -- review -- end")
    # if fi
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
                data_saving("balance.txt", balance) # just for auto-saving without waiting for the end command for saving, can be removed if we want to save just at the "end command"
                operations.append(("balance", amount))
                data_saving("history.txt", operations) # just for auto-saving without waiting for the end command
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
                    data_saving("inventory.txt", warehouse) # just for auto-saving
                    balance += total_price
                    data_saving("balance.txt", balance) # just for auto-saving
                    print(f"Sold {quantity_input} x {name} for a total of {total_price}\n")
                    operations.append(("sale", name, price, quantity_input))
                    data_saving("history.txt", operations) # just for auto-saving
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
                    data_saving("balance.txt", balance) # just for auto-saving
                    if name in warehouse:
                        warehouse[name]["quantity"] += quantity_input
                        warehouse[name]["price"] = price
                    else:
                        warehouse[name] = {"quantity": quantity_input, "price": price}
                    data_saving("inventory.txt", warehouse) # just for auto-saving
                    print(f" {quantity_input} x {name} was purchased for a total of {total_price}\n")
                    operations.append(("purchase", name, price, quantity_input))
                    data_saving("history.txt", operations) # just for auto-saving
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
            data_saving("history.txt", operations) # just for auto-saving

        elif command.lower() == "account":
            operations.append("account")
            data_saving("history.txt", operations) # just for auto-saving
            print(f"Your current account balance is {balance}")

        elif command.lower() == "warehouse":
            name = input("Enter the name of the product to display status: ")
            operations.append(("warehouse", name))
            data_saving("history.txt", operations) # just for auto-saving
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
            data_saving("balance.txt", balance)
            data_saving("inventory.txt", warehouse)
            data_saving("history.txt", operations)
            print("Closing the program. See you next time!")
            break