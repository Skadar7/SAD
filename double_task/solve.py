import numpy as np
import main

if __name__ == '__main__':
    X = ['x1', 'x2', 'x3', 'x4', 'x5']
    """F = 10x1 + 30x2 --> max
        6x1 + 5x2 <= 50
        2x1 + 3x2 <= 128
        4x1 + 16x2 <= 150
        x1, x2 > 0"""
    F = np.array([[10, 30]], dtype=float)
    x1 = np.array([[6], [2], [4]], dtype=float)
    x2 = np.array([[5], [4], [16]], dtype=float)
    x3_5 = [[[0, 0, 1]], [[0, 1, 0]], [[1, 0, 0]]]
    Cb = np.array([0, 0, 0], dtype=float)
    Cj = ['x3', 'x4', 'x5']
    B = np.array([[50], [128], [150]], dtype=float)
    print("Найти минимум целевой функции: {}y1 +{}y2 + {}y3".format(B[0][0], B[1][0], B[2][0]))
    delta1 = float(Cb @ x1 - F[0][0])
    delta2 = float(Cb @ x2 - F[0][1])
    F[0][0] = delta1
    F[0][1] = delta2

    A = np.concatenate([x1, x2], axis=1)
    Cb, Cj = main.f_step(A, B, F, Cb, x1, x2, Cj)
    #print(Cb, Cj)
    A = np.array([[6, 5],
                  [2, 3],
                  [4, 16]]).T
    print("При ограничениях")
    print("{}y1 + {}y2 + {}y3 >= 10".format(A[0][0], A[0][1], A[0][2]))
    print("{}y1 + {}y2 + {}y3 >= 30".format(A[1][0], A[1][1], A[1][2]))
    new_vect = []
    for i in range(len(Cj)):
        if X.index(Cj[i]) < 2:
            new_vect.append(np.array(A[X.index(Cj[i]):X.index(Cj[i])+1]))
        else:
            new_vect.append(np.array(x3_5[X.index(Cj[i]) - 2]))

    D = np.concatenate([new_vect[0].T, new_vect[1].T, new_vect[2].T], axis=1)
    print("Матрица базисных векторов")
    print(D)
    print("==============")
    D_inv = np.linalg.inv(D)
    print("Обратная матрица")
    print(D_inv)
    y = Cb @ D_inv
    print("Значение двойственных переменных")
    print("y = ", y)
    B = np.array([50, 128, 150], dtype=float)
    print("Gmin = ", round(np.dot(B, y), 1))
    #solve(A, B, F, Cb, x1, x2, Cj)
