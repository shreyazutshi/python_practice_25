print("Hello! This is a basic calculator. Choose an operator among given for mentioned functions:\n"
      " + for Addition\n"
      " - for Subtraction\n"
      " / for Division\n"
      " * for Multiplication\n"
      " ** for Exponent\n"
      " // for floor division\n"
      " % for quotient\n " )
s= int(input("Enter 0 to exit or 1 to start: "))

while s != 0:
    num1 = int(input("Enter a number: "))
    operator = input("Enter an operator: ")
    num2 = int(input("Enter another number: "))

    if operator == "+":
        print(f"Addition of {num1} and {num2} is {num1 + num2}")
    elif operator == "-":
        print(f"Substraction of {num1} and {num2} is {num1 - num2}")
    elif operator == "/":
        if num2 != 0:
             print(f"Division of {num1} and {num2} is {num1 / num2}")
        else:
             print("UH OH, Denominator can't be 0.")
             continue
    elif operator == "*":
        print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
    elif operator == "**":
        print(f"Exponent of {num1} over {num2} is {num1 ** num2}")
    elif operator == "//":
        print(f"Floor division of {num1} and {num2} is {num1 // num2}")
    elif operator == "%":
        print(f"Quotient of {num1} over {num2} is {num1 % num2}")
    else:
        print("Invalid operator. Please choose from the given operators.")
        continue

    s = int(input("\nEnter 0 to exit or 1 to continue: "))
print("Goodbye! Come back soon. :)")
