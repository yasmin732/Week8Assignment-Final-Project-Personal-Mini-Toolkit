print("=================================")
print(" Welcome to My Personal Toolkit!")
print("=================================")

while True:
    print("\n===== PERSONAL MINI-TOOLKIT =====")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Choose a tool (1-4): ")

    if choice == "1":
        # Simple calculator that performs basic arithmetic operations
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("You cannot divide by zero.")
                continue
        else:
            print(f"Sorry, '{operator}' is not a valid operation.")
            continue

        print(f"The result is {result}.")

    elif choice == "2":
        # To-do list that lets the user add, view, and remove tasks
        todo_list = []

        while True:
            action = input("To-do: add / show / remove / done: ")

            if action == "add":
                task = input("Enter a task: ")
                todo_list.append(task)
                print(f"Added '{task}' to your to-do list.")

            elif action == "show":
                print("Your to-do list:")

                if len(todo_list) == 0:
                    print("Your list is empty.")
                else:
                    for task in todo_list:
                        print(f"- {task}")

            elif action == "remove":
                task = input("Enter a task to remove: ")

                if task in todo_list:
                    todo_list.remove(task)
                    print(f"Removed '{task}' from your to-do list.")
                else:
                    print(f"'{task}' is not on your to-do list.")

            elif action == "done":
                print("Returning to the main menu.")
                break

            else:
                print(f"Sorry, '{action}' is not a valid option.")

    elif choice == "3":
        # Number guessing game that gives feedback until the correct number is guessed
        secret_number = 7

        print("I'm thinking of a number between 1 and 10.")

        while True:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                print(f"Correct! You guessed the number {secret_number}.")
                break
            elif guess < secret_number:
                print(f"{guess} is too low. Try again.")
            else:
                print(f"{guess} is too high. Try again.")

    elif choice == "4":
        print("Thank you for using my Personal Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please choose 1-4.")