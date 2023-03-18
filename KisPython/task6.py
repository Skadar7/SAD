def zero(items, left, right):
    if items[0] == 1984:
        return left
    if items[0] == 1988:
        return right


def three(items, left, middle, right):
    if items[3] == 'XPROC':
        return left
    if items[3] == 'GAP':
        return middle
    if items[3] == 'PUG':
        return right


def two(items, left, middle, right):
    if items[2] == 'INI':
        return left
    if items[2] == 'KRL':
        return middle
    if items[2] == 'D':
        return right


def one(items, left, middle, right):
    if items[1] == 'METAL':
        return left
    if items[1] == 'ABNF':
        return middle
    if items[1] == 'RED':
        return right


def main(items):
    return zero(
        items,
        three(items,
              one(items, 0, 1, 2),
              3,
              two(items, 4, 5, 6)),
        three(items, 7, 8,
              one(items, 9, 10, 11))
    )


if __name__ == "__main__":
    print(main([1988, 'ABNF', 'INI', 'GAP']))