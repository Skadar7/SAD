from functools import reduce
from math import fsum
from pprint import pprint


def geom_mean(arr):
    return [round(pow(reduce(lambda x, y: x * y, k), 1/5), 2) for k in arr]

def geom_mean_norm(arr):
    return fsum(arr)


def W(a, b):
    return [round(i / a, 2) for i in b]


def sum_col(arr):
    res = []
    for i in range(len(arr[0])):
        res.append(0)
        for j in range(len(arr)):
            res[i] += round(arr[j][i], 2)

    return res


def synthesis_of_alternatives(cnt, x, y):
    res = 0
    for i, j in enumerate(x):
        res += j * y[i][cnt]
    return res


if __name__ == "__main__":
    GLOBAL_I = 1
    MINI_I = 1

    vuz_name = ['ВДНХ', 'Солнцево', 'Марьино', 'Раменки', 'Ростокино']
    vuz_arr = [[1, 3, 2, 1/4, 1/4], [1/3, 1, 1/4, 1/5, 1/3], [1/2, 4, 1, 1/5, 1/4],
               [4, 5, 5, 1, 1], [4, 3, 4, 1, 1]]

    arr1 = [[1, 1/5, 5, 1/5, 1], [5, 1, 6, 1/3, 5], [1/5, 1/6, 1, 1/7, 1/5],
            [5, 3, 7, 1, 5], [1, 1/5, 5, 1/5, 1]] # Цена (-)

    arr2 = [[1, 1/7, 4, 1, 1/8], [7, 1, 9, 8, 1], [1/4, 1/9, 1, 1/3, 1/9],
            [1, 1/8, 3, 1, 1/9], [8, 1, 9, 9, 1]] # Удаленность (-)

    arr3 = [[1, 6, 5, 4, 5], [1/7, 1, 1/3, 1/7, 1/2], [1/6, 3, 1, 1/6, 2],
            [1/5, 7, 6, 1, 6], [1/6, 2, 1/2, 1/6, 1]] # Б. места (+)

    arr4 = [[1, 6, 4, 5, 4], [1/6, 1, 1/5, 1/4, 1/5], [1/4, 5, 1, 4, 2],
            [1/5, 4, 1/4, 1, 1/3], [1/4, 5, 1/2, 3, 1]] # Отзывы (+)

    arr5 = [[1, 4, 5, 1/3, 5], [1/4, 1, 4, 1/5, 3], [1/5, 1/4, 1, 1/6, 1/2],
            [3, 5, 6, 1, 6], [1/5, 1/3, 2, 1/6, 1]] # Проходной балл (-)

    arr = [vuz_arr, arr1, arr2, arr3, arr4, arr5]
    geom_mean_res = []

    """Для определения относительной ценности каждого элемента
     находим геометрическое среднее """
    for _ in arr:
        geom_mean_res.append(geom_mean(_))

    for k, i in enumerate(geom_mean_res):
        print("Таблица {}".format(k))
        for l, j in enumerate(i):
            print("Строка {}\nV{} = {}".format(l+1, l+1, j))
        print("\n")
    #pprint(geom_mean_res) #Vi
    print("\n===========================================\n")
    geom_mean_norm_res = []

    # Проводим нормализацию полученных чисел
    for _ in geom_mean_res:
        geom_mean_norm_res.append(geom_mean_norm(_))

    for i, j in enumerate(geom_mean_norm_res):
        print("Нормализация для таблицы {} = {}".format(i+1, j))
    #print(geom_mean_norm_res)#sumVi

    weight = []
    # Найдем важность приоритетов
    for i, _ in enumerate(geom_mean_res):
        weight.append(W(geom_mean_norm_res[i], _))

    print("\n===========================================\n")

    for k, i in enumerate(weight):
        print("Таблица {}".format(k))
        for l, j in enumerate(i):
            print("Строка {}\nW{} = {}".format(l + 1, l + 1, j))
        print("\n")
    #print(weight)#W3k1Y

    S = []
    # Cумма каждого столбца матрицы суждений
    for _ in arr[:]:
        S.append(sum_col(_))

    for k, i in enumerate(S):
        print("Таблица {}".format(k + 1))
        for l, j in enumerate(i):
            print("Столбец {}\nS{} = {}".format(l + 1, l + 1, j))
        print("\n")

    #полученный результат умножается на компоненту нормализованного вектора приоритетов
    P = []
    I = 0
    for i, j in zip(S, weight[:]):
        P.append([])
        for x, y in zip(i, j):
            P[I].append(x * y)
        I += 1

    for k, i in enumerate(P):
        print("Таблица {}".format(k + 1))
        for l, j in enumerate(i):
            print("Столбец {}\nP{} = {}".format(l + 1, l + 1, j))
        print("\n")

    lambda_max = []
    for _ in P:
        lambda_max.append(round(geom_mean_norm(_), 2))

    print("Лямбда\n",lambda_max)

    #Отклонение от согласованности выражается индексом согласованности
    IS = []
    for i in lambda_max:
        IS.append(round((i - 5)/(5 - 1), 3))

    print("Индекс согласованности\n", IS)

    #отношением согласованности ОС
    OS = []
    for i in IS:
        OS.append(round(i / 1.12, 3))

    print("Отношение согласованоости\n", OS)

    synthes = []
    for i, j in enumerate(weight):
        if i == 5:
            break
        synthes.append(synthesis_of_alternatives(i, weight[0], weight))

    win = dict()
    for i, j in zip(vuz_name, synthes):
        win[i] = j

    win = sorted(win.items(), key=lambda x: x[1], reverse=True)
    print("\n===================\n")
    for i, j in enumerate(win):
        print("{} место {} = {}".format(i+1, j[0], round(j[1], 3)))
