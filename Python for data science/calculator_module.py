def calculator():
    num1 = int(input("Enter first number:  "))
    num2 = int(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    print("Select operation:")
    match operation:
        case '+' :
            c = num1 + num2
            print(f"addtion of {num1} and {num2} is: ",c)

        case '-':
            c = num1 - num2
            print(f"subtraction of {num1} and {num2} is: ",c)

        case '*':
            c = num1 * num2
            print(f"multiplication of {num1} and {num2} is: ",c)

        case '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                c = num1 / num2
                print(f"division of {num1} and {num2} is: ",c)

calculator()