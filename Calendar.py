from _tkinter import *
from math import *
num1 = float(input("Enter First Number: "))
op = str(input("Enter Your Operator: "))
num2 = float(input("Enter Second Number: "))


if op == '+':
    print("The Summation is= ",num1+num2)
elif op == '-':
    print("The Subtraction is= ", num1-num2)
elif op == '*':
    print("The Multiplication is= ", num1 * num2)
elif op == '/':
    print("The Divider is= ", num1 / num2)
else:
    print("Please Enter valid input")