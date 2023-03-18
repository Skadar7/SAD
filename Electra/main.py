from math import inf
from pprint import pprint
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

COLOR = [-1 for _ in range(10)]
PN = []

def detect_cycle(arr, start):
    global COLOR
    COLOR[start] = 0
    for i in range(10):
        if arr[start][i] != 0:
            if COLOR[i] != 0:
                return detect_cycle(arr, i)
            else:
                print(COLOR)
                print("\n+++++++++++++++++++++++++++++++++++++\n")
                COLOR = [-1 for _ in range(10)]
                return False
    return True


def calc_crit(arr):
    price = [(1, 5), (5.1, 8), (8.1, 13)]
    price_score = [15, 10, 5]
    remote = [(1, 20), (20.1, 40), (40.1, 60), (60.1, 106)]
    r_score = [5, 10, 15, 20]
    b_pl = [(0.1, 1), (1.1, 2.1), (2.2, 4)]
    b_pl_score = [15, 10, 5]
    rev = [(1.1, 3.1), (3.2, 5.1), (5.2, 6.1), (6.2, 7.0)]
    rev_score = [5, 10, 15, 20]
    ball = [(1, 2.1), (2.2, 4.1), (4.2, 6.1), (6.2, 7)]
    ball_score = [5, 10, 15, 20]

    res_tbl = [["Эсенево"], ["Медведкого"], ["Солнцево"], ["Марьино"], ["Новопеределкино"],
               ["Ростокино"], ["ВДНХ"], ["Раменки"], ["Савёловская"], ["Мичуринский проспект"]]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if j == 0:
                continue
            if j == 1:
                for x, y in zip(price, price_score):
                    if x[0] <= arr[i][j] <= x[1]:
                        res_tbl[i].append(y)
            if j == 2:
                for x, y in zip(remote, r_score):
                    if x[0] <= arr[i][j] <= x[1]:
                        res_tbl[i].append(y)
            if j == 3:
                for x, y in zip(b_pl, b_pl_score):
                    if x[0] <= arr[i][j] <= x[1]:
                        res_tbl[i].append(y)
            if j == 4:
                for x, y in zip(rev, rev_score):
                    if x[0] <= arr[i][j] <= x[1]:
                        res_tbl[i].append(y)
            if j == 5:
                for x, y in zip(ball, ball_score):
                    if x[0] <= arr[i][j] <= x[1]:
                        res_tbl[i].append(y)

    print(res_tbl)
    return res(res_tbl)


def res(arr):
    global PN
    gr = nx.DiGraph()
    weights = [5, 3, 1, 2, 4]
    asp = [0, 1, 0, 1, 1]
    graph_arr = [[], [], [], [], [], [], [], [], [], []]
    vuz_place = {"Эсенево": 0, "Медведкого": 0, "Солнцево": 0, "Марьино": 0, "Новопеределкино": 0,
                 "Ростокино": 0, "ВДНХ": 0, "Раменки": 0, "Савёловская": 0, "Мичуринский проспект": 0}
    for i in range(10):
        for j in range(10):
            graph_arr[i].append(0)

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if i == j:
                continue
            P = 0
            N = 0
            P_str = 'P{0}{1} = '.format(i, j)
            N_str = 'N{0}{1} = '.format(i, j)
            D_str1 = 'D{0}{1} = P{0}{1}/N{0}{1} = '.format(i, j)
            D_str2 = 'D{0}{1} = 1/D{1}{0} = '.format(j, i)
            for k in range(len(arr[0])):
                if k == 0:
                    gr.add_node(arr[i][0])
                    continue
                if asp[k - 1] == 1:
                    if arr[i][k] > arr[j][k]:
                        P += weights[k - 1]
                        P_str += '{} + '.format(weights[k - 1])
                        N_str += '0 + '
                    elif arr[i][k] < arr[j][k]:
                        N += weights[k - 1]
                        N_str += '{} + '.format(weights[k - 1])
                        P_str += '0 + '
                    else:
                        N_str += '0 + '
                        P_str += '0 + '
                else:
                    if arr[i][k] < arr[j][k]:
                        P += weights[k - 1]
                        P_str += '{} + '.format(weights[k - 1])
                        N_str += '0 + '
                    elif arr[i][k] > arr[j][k]:
                        N += weights[k - 1]
                        N_str += '{} + '.format(weights[k - 1])
                        P_str += '0 + '
                    else:
                        N_str += '0 + '
                        P_str += '0 + '

            print(P_str[:-2] + '= {}'.format(P))
            print(N_str[:-2] + '= {}'.format(N))
            if P != 0 and N != 0:
                D1 = round(P / N, 1)
                D2 = round(1 / D1, 1)
                if D1 > 1:
                    graph_arr[i][j] = D1
                    if D1 not in PN:
                        PN.append(D1)
                else:
                    graph_arr[j][i] = D2
                    if D2 not in PN:
                        PN.append(D2)
                print(D_str1 + '{0}/{1} = {2}'.format(P, N, D1))
                print(D_str2 + '1/{0} = {1}'.format(D1, D2))
            elif N == 0:
                graph_arr[j][i] = inf
                print(D_str1 + '{0}/{1} = {2}'.format(P, N, 0))
                print(D_str2 + '1/{0} = {1}'.format(0, inf))
            else:
                graph_arr[i][j] = inf
                print(D_str1 + '{0}/{1} = {2}'.format(P, N, inf))
                print(D_str2 + '1/{0} = {1}'.format(inf, 0))

            print('\n===================================\n')

    PN = sorted(PN)

    while True:
        print(PN)
        pprint(graph_arr)
        if PN[0] > 10:
            break
        else:
            for i in range(len(graph_arr)):
                for j in range(len(graph_arr[0])):
                    if graph_arr[i][j] == PN[0]:
                        graph_arr[i][j] = 0
            PN.remove(PN[0])

    #print(PN)
    #print(sorted(PN))
    for i in range(len(graph_arr)):
        for j in range(len(graph_arr[0])):
            if graph_arr[i][j] > 0:
                vuz_place[arr[i][0]] += 1
                gr.add_edge(arr[i][0], arr[j][0])
            if graph_arr[j][i] > 0:
                vuz_place[arr[i][0]] -= 1


    sorted_vuz = sorted(vuz_place.items(), key=lambda x: x[1], reverse=True)
    p = 1
    for i in sorted_vuz:
        print("{} место - {} = {}".format(p, i[0], i[1]))
        p += 1

    pprint(graph_arr)
    plt.figure(figsize=(10, 10))
    nx.draw(gr, node_size=500, with_labels=True)
    plt.show()


if __name__ == "__main__":
    arr = [["Эсенево", 8, 105, 4, 7.0, 6.1], ["Медведкого", 8.7, 55, 1.2, 6.9, 6.2],
           ["Солнцево", 7.1, 43, 1.6, 5.2, 4.4], ["Марьино", 5.2, 26, 2.0, 3.2, 3.1],
           ["Новопеределкино", 8.7, 57, 2.2, 6.9, 6.3], ["Ростокино", 10.6, 53, 1.0, 6.8, 6.6],
           ["ВДНХ", 3.1, 55, 1.2, 6.9, 6.2], ["Раменки", 3.2, 28, 3.7, 2.2, 2.1],
           ["Савёловская", 11.6, 67, 0.8, 6.9, 6.9], ["Мичуринский проспект", 12.1, 60, 0.7, 7.0, 7.0]]

    calc_crit(arr)