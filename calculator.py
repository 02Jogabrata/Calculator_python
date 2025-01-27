print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", num1 + num2)

        elif choice == '2':
            print(num1, "-", num2, "=", num1 - num2)

        elif choice == '3':
            print(num1, "*", num2, "=", num1 * num2)

        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Invalid input")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        break
