from asteval import Interpreter 

def calculator():
    ae = Interpreter()
    response = input("Select an operation, 1 = addition, 2 = subtraction, 3 = multiplication, 4 = division, 5 = exponents, 6 = special equation: ")
    if response == "1":
        yes_noadd = input("You have chosen addition, if you want this type y, if you want to change type n: ").lower()
        if yes_noadd == "y":
            num1_add = float(input("Type your first number you want to add: "))
            num2_add = float(input("Type your second number you want to add: "))
            sum = num1_add + num2_add
            print("The sum of", num1_add, "and", num2_add, "is", sum)
        else:
            print("Reset calculator to continue.")
    if response == "2":
        yes_noadd = input("You have chosen subtraction, if you want this type y, if you want to change type n: ").lower()
        if yes_noadd == "y":
            num1_sub = float(input("Type the number you want to subtract from: "))
            num2_sub = float(input("Type the number you want to subtract from the base number: "))
            dif = num1_sub - num2_sub
            print("The difference of", num1_sub, "and", num2_sub, "is", dif)
        else:
            print("Reset calculator to continue.")
    if response == "3":
        yes_noadd = input("You have chosen multiplication, if you want this type y, if you want to change type n: ").lower()
        if yes_noadd == "y":
            num1_mult = float(input("Type the number the first number you want to multiply: "))
            num2_mult = float(input("Type the number the second number you want to multiply: "))
            pro = num1_mult * num2_mult
            print("The product of", num1_mult, "and", num2_mult, "is", pro)
        else:
            print("Reset calculator to continue.")
    if response == "4":
        yes_noadd = input("You have chosen division, if you want this type y, if you want to change type n: ").lower()
        if yes_noadd == "y":
            num1_div = float(input("Type the number you want to divide: "))
            num2_div = float(input("Type the number you want the base number to be divided by: "))
            quo = num1_div / num2_div
            print("The quotient of", num1_div, "and", num2_div, "is", quo)
        else:
            print("Reset calculator to continue.")
    if response == "5":
        yes_noadd = input("You have chosen exponents, if you want this type y, if you want to change type n: ").lower()
        if yes_noadd == "y":
            num1_exp = float(input("Type the number you want to start with: "))
            num2_exp = float(input("Type the number you want the base number to be the power to: "))
            exp_result = num1_exp ** num2_exp
            print("The quotient of", num1_exp, "and", num2_exp, "is", exp_result)
        else:
            print("Reset calculator to continue.")
    if response == "6":
        yes_noadd = input("You have chosen a special equation, if you want this type y, if you want to change type n: ").lower()
        if yes_noadd == "y":
            special = input("Type the equation you want solved: ")
            result = ae(special)
            print("The result of", special, "=", result)
        else:
            print("Reset calculator to continue.")
calculator()