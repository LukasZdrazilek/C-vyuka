import argparse

def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def power(base, exponent):
    return base ** exponent

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type = int, default = 1, help = "Vypocte faktorial cisla")
    parser.add_argument("-m", nargs = 2, type = int, default = [1, 1], help = "Vypocte n-tou mocninu cisla")
    args = parser.parse_args()

    if args.f:
        result = factorial(args.f)
        print(f"Faktorial cisla {args.f} = {result}")
    elif args.m:
        base, exponent = args.m
        result = power(base, exponent)
        print(f"{exponent} mocnina cisla {base} = {result}")
    else:
        parser.print_help()
