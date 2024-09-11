"""Assignment 1"""

def calculate(num1, num2, operator):
    if operator not in "+-*/%":
        return "Invalid Operator"
    else:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1-num2
        elif operator == "*":
            return num1*num2
        elif operator == "/":
            return num1/num2
        elif operator == "%":
            return num1%num2

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
op = input("Enter operator from +, -, *, /, %: ")
print(calculate(n1, n2, op))
