from math import log


def main(n, b, z):
    my_sum = 0
    for j in range(1, b+1):
        for i in range(1, n+1):
            my_sum += 44 * pow(log(pow(i, 3) / 32), 6) -\
                      18 * pow((79 + 61 * j + z ** 2), 2) - 99
    return my_sum

if __name__ == "__main__":
    print(main(6, 7, 0.05))