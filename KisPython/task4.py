from math import sin, cos


def main(n):
    if n == 0:
        return 0.21
    else:
        return pow(sin(main(n - 1)), 2) + \
               pow(cos(98 * pow(main(n - 1), 2) + pow(main(n - 1), 3) + 1), 3)


if __name__ == "__main__":
    print(main(5))