from json import loads, dumps
from os.path import getsize

def check():
    if getsize(r"E:\storage.json") == 0:
        return {}
    with open(r"E:\storage.json", 'r') as r:
        return loads(r.read())


def f_set(key, val):
    data = check()
    print(data)
    if key in data:
        data[key].append(val)
    else:
        data.setdefault(key, []).append(val)

    print(data)
    with open(r"E:\storage.json", 'w') as w:
        return w.write(dumps(data))

def f_get(key):
    if getsize(r"E:\storage.json") == 0:
        return "Файл пустой"

    with open(r"E:\storage.json", "r") as r:
        data = loads(r.read())
        return data[key]


if __name__ == "__main__":
    while True:
        enter = input()
        if "--key" in enter and "--val" in enter:
            end = enter.index('-', 2)
            key = enter[6:end].strip()
            print(key)
            start = enter.index("-", 2)
            val = enter[start+6:]
            print(val)
            f_set(key, val)
        elif "--key" in enter:
            print(f_get(enter[6:]))
        else:
            print("Закончили работу!")
            break