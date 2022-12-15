while True:
    choice = input("Please On your Calculator? (on): ")
    if choice in 'on':
        num1 = float(input("Enter First Number: "))
        op = str(input("Enter Your Operator: "))
        num2 = float(input("Enter Second Number: "))
        if op == '+':
            print("The Summation is= ", num1 + num2)
        elif op == '-':
            print("The Subtraction is= ", num1 - num2)
        elif op == '*':
            print("The Multiplication is= ", num1 * num2)
        elif op == '/':
            print("The Divider is= ", num1 / num2)
        else:
            print("Invalid Operator")

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == 'no':
            break
    else:
        print("Invalid")
