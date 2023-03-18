def add(x, y):
    with open('Temp.json', 'w') as f:
        f.write(x + y)
    return x + y


def multiply(x, y):
    return x * y
