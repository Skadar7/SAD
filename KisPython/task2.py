from math import ceil, tan, sin


def f(y):
    if y < 60:
        return 84 * pow((y ** 2 / 9) - 1 - y ** 3, 5) \
               + y ** 3 + 59 * y ** 2
    elif 60 <= y < 131:
        return (59 * y) ** 7 + (y ** 6 / 60) \
               + pow(sin(y), 3)
    elif 131 <= y < 172:
        return 1 - y ** 2 - pow(tan(y), 5)
    elif 172 <= y < 222:
        return y ** 4
    else:
        return 5 * (ceil(31 * y ** 3 + y ** 2 + 11 * y)) ** 5


if __name__ == "__main__":
    print(f(58))
