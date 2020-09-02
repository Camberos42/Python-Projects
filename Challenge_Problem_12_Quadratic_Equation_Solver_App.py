import cmath
import math

#Quadratic Equation Solver App.
print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

total_ecs = int(input("How many equations would you like to solve today:"))

for i in range(1,total_ecs+1):
    print(f"Solving equation #{i}")
    print("---------------------------------------------------------------")

    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))

    print(f"The solutions to {a} + {b} + {c} = 0 are:") 
    x1 = (-b + cmath.sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - cmath.sqrt((b**2)-(4*a*c)))/(2*a)
    print("x1 = "+ str(x1))
    print("x2 = "+ str(x2))
