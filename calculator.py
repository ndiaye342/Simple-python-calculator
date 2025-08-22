number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    result = float(number1) + float(number2)
    print(f"{number1} + {number2} = {result}")
elif operator == "-":
    result = float(number1) - float(number2)
    print(f"{number1} - {number2} = {result}")
elif operator == "*":
    result = float(number1) * float(number2)
    print(f"{number1} * {number2} = {result}")
elif operator == "/":
    if number2 == "0":
        print("Error: Division by zero is not allowed.")
    else:
        result = float(number1) / float(number2)
        print(f"{number1} / {number2} = {result}")