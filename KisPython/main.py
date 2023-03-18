from math import acos, ceil


def main(z, x):
    a = (92 * pow((20 * pow(x, 3) + 10 * z), 7)) - (60 * pow(acos(z), 2))
    b = 5 * (pow((ceil(31 * pow(x, 3) + pow(z, 2) + (11 * x))), 7))
    c = pow(pow(z, 2) + (pow((ceil(98 * pow(x, 2) +
                                   pow(z, 3) + 75 * x)), 5)), 0.5)

    return (a / b) + c


if __name__ == '__main__':
    print(main(-0.06, 0.35))
