num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = int(input("Choose Operation (1 - Addition, 2 - Subtraction, 3 - Multiplication, 4 - Division): "))

if operation == 4 and num2 == 0:
    print("Invalid Choice.")
else:
    def add_numbers(num1, num2):
        return num1 + num2

    def subtract_numbers(num1, num2):
        return num1 - num2

    def multiply_numbers(num1, num2):
        return num1 * num2

    def divide_numbers(num1, num2):
        return num1 / num2

    if operation == 1:
        result = add_numbers(num1, num2)
        print("Result:", result)
    elif operation == 2:
        result = subtract_numbers(num1, num2)
        print("Result:", result)
    elif operation == 3:
        result = multiply_numbers(num1, num2)
        print("Result:", result)
    elif operation == 4:
        result = divide_numbers(num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice.")

#Contribution - Alcarez
#Helped equally

#Contribution - Segundino
#Helped equally

#Grade and Section
#8 - Edelweiss