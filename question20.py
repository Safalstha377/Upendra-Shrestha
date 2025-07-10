#20.Write a menu-driven program to perform arithmetic operations (+, -, *, /) based on user choice using conditional statements.

 
print("╔══════════════════════════════════════╗")
print("║       ARITHMETIC MENU OPERATION      ║")
print("╠══════════════════════════════════════╣")
print("║ 1. Addition (+)                      ║")
print("║ 2. Subtraction (-)                   ║")
print("║ 3. Multiplication (*)                ║")
print("║ 4. Division (/)                      ║")
print("║ 5. Exit                              ║")
print("╚══════════════════════════════════════╝")

for n in range(1000):  
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the program. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")

        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")

        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")

        elif choice == '4':
            if num2 == 0:
                print(f"Result:{num1} / {num2} = {result}")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")

    else:
        print("Invalid choice! Please select a valid option (1-5).")

    print()