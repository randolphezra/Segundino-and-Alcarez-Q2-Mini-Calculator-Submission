def getValues():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    return n1, n2

operation = int(input("Choose Operation (1 - Addition, 2 - Subtraction, 3 - Multiplication, 4 - Division): "))

if operation < 1 or operation > 4:
    print("Invalid choice.")
else:
    num1, num2 = getValues()

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

#Contribution - Alcarez
#Helped equally

#Contribution - Segundino
#Helped equally

#Grade and Section
#8 - Edelweiss