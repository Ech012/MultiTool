from sympy import solve, Eq
import sympy as sp
import random 


def calc(excersise):
    print(eval(excersise))


def equation(eq: str):
    for i in range(len(eq)):
        if eq[i] == '=':
            result = eq[i+1:]
            qe = eq[:i]
            break
    s = sp.parsing.sympy_parser.parse_expr(qe)
    s1 = sp.parsing.sympy_parser.parse_expr(result)
    eq = Eq(s, s1)
    sol = solve(eq)
    print(f"The solution is {sol}")


def random_number(num1, num2):
    print(f"Your random number is {random.randint(num1, num2)}")