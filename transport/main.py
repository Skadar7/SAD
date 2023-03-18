import numpy as np


def get_key(f, value):
    for k, v in f.items():
        if v == value:
            return k

def create_new_table(f, K, cnt, new_f, start_key):
    if cnt % 2 == 0:
        new_k = K[0] + str(int(K[1]) - 1)
        if K[1] != '0' and new_k in f:
            new_f[new_k] = f[new_k][1]
        else:
            new_k = K[0] + str(int(K[1]) + 1)
            new_f[new_k] = f[new_k][1]
    else:
        new_k = str(int(K[0]) - 1) + K[1]
        if K[0] != '0' and new_k in f:
            new_f[new_k] = f[new_k][1]
        else:
            new_k = str(int(K[0]) + 1) + K[1]
            new_f[new_k] = f[new_k][1]

    if new_k == start_key:
        min_elem = min(new_f.values())
        new_f[list(new_f.keys())[-1]] = 0
        for i in range(len(new_f)):
            if i % 2 == 0:
                new_f[list(new_f.keys())[i]] -= min_elem
            else:
                new_f[list(new_f.keys())[i]] += min_elem

        for k, v in new_f.items():
            if k in f:
                f[k] = list(f[k])
                f[k][1] = v
                f[k] = tuple(f[k])

        del_keys = []
        for k, v in f.items():
            if f[k][1] == 0:
                del_keys.append(k)

        for k in del_keys:
            if k in f:
                del f[k]

        return f
    else:
        return create_new_table(f, new_k, cnt+1, new_f, start_key)



def uv_calculation(f, u, v):
    for k in f.keys():
        if u['u{}'.format(k[0])] != -10 \
                and v['v{}'.format(k[1])] == -10:
            v['v{}'.format(k[1])] = f[k][0] - u['u{}'.format(k[0])]
        if v['v{}'.format(k[1])] != -10 \
                and u['u{}'.format(k[0])] == -10:
            u['u{}'.format(k[0])] = f[k][0] - v['v{}'.format(k[1])]
    return u, v


def potentials(A, f, u, v):
    delta = {}
    for k in f.keys():
        u['u{}'.format(k[0])] = -10
        v['v{}'.format(k[1])] = -10

    u = dict(sorted(u.items(), key=lambda x: x[0]))
    v = dict(sorted(v.items(), key=lambda x: x[0]))
    u[list(u.keys())[0]] = 0
    v[list(v.keys())[0]] = f[list(f.keys())[0]][0]

    u, v = uv_calculation(f, u, v)
    print("Значение потенциалов: ", u, v)
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == 3:
                break
            if j == 4:
                continue

            if '{}{}'.format(i, j) in f:
                continue
            else:
                delta['{}{}'.format(i, j)] = A[i][j] - \
                                             (u['u{}'.format(i)] + v['v{}'.format(j)])

    print("Значение относительных оценок:", delta)
    min_elem = min(delta.values())
    print("Минимальная размерность: ", min_elem)
    if min(delta.values()) < 0:
        lmd = (get_key(delta, min_elem), min_elem)
        f[lmd[0][0] + lmd[0][1]] = (A[int(lmd[0][0])][int(lmd[0][1])], 100)
        f = create_new_table(f, lmd[0][0] + lmd[0][1], 0, {}, lmd[0][0] + lmd[0][1])
        return potentials(A, f, {}, {})
    else:
        return f


def minimum_cost(A, minimum, f):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == 3:
                return minimum_cost(A, minimum+1, f)
            if j == 4:
                continue

            if A[i][j] == minimum:
                if A[i][4] != 0 and A[3][j] != 0:
                    if A[i][4] - A[3][j] == 0:
                        f['{}{}'.format(i, j)] = (A[i][j], A[3][j])
                        A[i][4] = 0
                        A[3][j] = 0
                    elif A[i][4] - A[3][j] > 0:
                        f['{}{}'.format(i, j)] = (A[i][j], A[3][j])
                        A[i][4] -= A[3][j]
                        A[3][j] = 0
                    else:
                        f['{}{}'.format(i, j)] = (A[i][j], A[i][4])
                        A[3][j] -= A[i][4]
                        A[i][4] = 0

            if A[0][4] == 0 and A[1][4] == 0 and A[2][4] == 0:
                print(f)
                return f


def northwest_corner(A, i, j, f):
    if A[2][4] == 0:
        return f

    if A[i][4] - A[3][j] >= 0:
        f['{}{}'.format(i, j)] = (A[i][j], A[3][j])
        A[i][4] -= A[3][j]
        return northwest_corner(A, i, j+1, f)
    else:
        tmp = A[i][4]
        f['{}{}'.format(i, j)] = (A[i][j], tmp)
        A[i][4] = 0
        i += 1
        if A[i][4] - (A[3][j] - tmp) >= 0:
            A[i][4] -= (A[3][j] - tmp)
            f['{}{}'.format(i, j)] = (A[i][j], A[3][j] - tmp)
            return northwest_corner(A, i, j+1, f)


if __name__ == '__main__':
    transportation_table = np.array([[1, 4, 5, 5, 60],
                                     [1, 3, 9, 3, 70],
                                     [3, 3, 2, 4, 20],
                                     [40, 30, 30, 50, 150]])

    f = {}
    """f = northwest_corner(transportation_table, 0, 0, {})
    res = 0
    for k in f.keys():
        res += f[k][0] * f[k][1]
    print(f)
    print("Общая стоимсоть перевозок методом северного угла = " + str(res))"""
    #####################################################
    """f = minimum_cost(transportation_table, 1, f)
    res = 0
    for k in f.keys():
        res += f[k][0] * f[k][1]

    print("Общая стоимсоть перевозок методом минимальной стоимости = " + str(res))"""
    
    f = northwest_corner(transportation_table, 0, 0, {})
    f = potentials(transportation_table, f, {}, {})
    print(f)
    res = 0
    for k in f.keys():
        res += f[k][0] * f[k][1]

    print("Общая стоимсоть перевозок методом потенциалов = " + str(res))