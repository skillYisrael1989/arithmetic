"""A beginner calculator. Run: python3 app.py 12 / 4"""
import argparse
import math


def calculate(left, operator, right):
    if not all(math.isfinite(value) for value in (left, right)):
        raise ValueError("Enter finite numbers")
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ValueError("Cannot divide by zero")
        return left / right
    raise ValueError("Unknown operator")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("left", type=float)
    parser.add_argument("operator", choices=["+", "-", "*", "/"])
    parser.add_argument("right", type=float)
    args = parser.parse_args()
    try:
        print(calculate(args.left, args.operator, args.right))
    except ValueError as error:
        parser.error(str(error))
