#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, calc.add(a, b)))
    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, calc.sub(a, b)))
    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, calc.mul(a, b)))
    elif operator == '/':
        print("{} {} {} = {}".format(a, operator, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
