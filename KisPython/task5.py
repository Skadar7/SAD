from math import ceil


def main(z, x):
    my_sum = 0
    n = len(z)-1
    for i in range(1, len(z) + 1):
        my_sum += 5 * pow(((pow(x[n + 1 - ceil(i / 2)], 3)) / 15)
                          - z[n + 1 - i], 2)
    return 69 * my_sum


if __name__ == "__main__":
    print(main([0.31, -0.78, 0.33, 0.51, 0.04, 0.46],
               [-0.04, -0.96, -0.14, 0.2, -0.25, -0.21]))
