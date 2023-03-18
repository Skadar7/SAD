import numpy as np
from math import ceil

X = ['x1', 'x2', 'x3', 'x4', 'x5']

def create_simpl_table(A, r, s, r_elem, Cb):
    #print(r, s)
    #print(r_elem)
    new_A = A.copy()
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == r:
                continue
            if j == s:
                continue
            if i == 3 and j == 3:
                continue
            #print("( " + str(A[i][j]) + " * " + str(r_elem) + " - " + str(A[i][s]) +
            #      " * " + str(A[r][j]) + ") /" + str(r_elem))
            new_A[i][j] = ((A[i][j] * r_elem) - (A[i][s] * A[r][j])) / r_elem
    #print(new_A)
    #print("====STOP====")
    new_A[r][s] = r_elem ** -1
    for i in range(len(A[0])):
        if i != s:
            new_A[r][i] /= r_elem

    for j in range(len(A)):
        if j != r:
            new_A[j][s] = -(A[j][s] / r_elem)

    #new_A[2][2] = Cb @ new_A[:, 2:][:-1]
    print(new_A)
    print("==================================")
    return new_A


def f_step(A, B, F, Cb, x1, x2, Cj):
    global X
    Q = np.array([[0]])
    Q = np.insert(Q, 0, Cb @ B, axis=0)
    Q = np.delete(Q, 1, axis=0)
    #print(Q)

    bas = F.min()
    #print(bas)
    bas_ind = np.where(F[0] == bas)
    #print(bas_ind[0][0])
    tmp = 1
    if bas_ind[0][0] == 0:
        tmp = 0
    Cb[bas_ind[0][0] + tmp] = -bas
    #print(Cb)

    min_q = 1000
    min_q_ind = 0
    for i in range(len(A)):
        if A[i][bas_ind] > 0:
            temp_m = B[i]/A[i][bas_ind]
            if temp_m < min_q:
                min_q = temp_m
                min_q_ind = i

    #print(min_q_ind)

    Cj[min_q_ind] = X[bas_ind[0][0]]
    for i in range(len(Cj)):
        if Cj[i] == 'x1':
            Cb[i] = 10
        if Cj[i] == 'x3':
            Cb[i] = 30

    r_elem = A[min_q_ind][bas_ind[0][0]]
    #print(r_elem)

    B = np.concatenate([B, Q])
    #print(B)
    #print("====CHECK=====")
    #print(A)
    #print(F)
    A = np.concatenate([A, F])
    #print(A)
    A = np.concatenate([A, B], axis=1)
    #print(A)

    new_A = create_simpl_table(A, min_q_ind, bas_ind[0][0], r_elem, Cb)
    if new_A[3][0] < 0 or new_A[3][1] < 0:
        print(new_A)
        r_A = new_A[:, :2][:-1]
        #print(r_A)
        r_B = new_A[:, 2:][:3]
        #print(r_B)
        r_F = new_A[:, :2][3:]
        #print(r_F)
        x1 = new_A[:, :1][:-1]
        #print(x1)
        x2 = new_A[:, 1:2][:-1]
        #print(x2)
        f_step(r_A, r_B, r_F, Cb, x1, x2, Cj)
        return
    else:
        print("==================================\n"
              "Результат:\n")
        r_B = new_A[:, 2][:-1]
        #print(r_B)
        #print(Cb)
        new_A[3][2] = Cb.dot(r_B)
        print(new_A)
        print("Q = " + str(round(Cb @ r_B, 1)))
        print(Cj[0] + " = " + str(new_A[0][2]))
        print(Cj[2] + " = " + str(new_A[2][2]))
        #res = ((new_A[n][m] * r_elem) - (new_A[n - 1][m] * new_A[n][m - 1])) / r_elem
        return


if __name__ == '__main__':
    """F = 10x1 + 30x2 --> max
        6x1 + 5x2 <= 50
        2x1 + 3x2 <= 128
        4x1 + 16x2 <= 150
        x1, x2 > 0"""
    F = np.array([[10, 30]], dtype=float)
    x1 = np.array([[6], [2], [4]], dtype=float)
    x2 = np.array([[5], [4], [16]], dtype=float)
    x3, x4, x5 = 0, 0, 0
    Cb = np.array([0, 0, 0], dtype=float)
    Cj = ['x3', 'x4', 'x5']
    B = np.array([[50], [128], [150]], dtype=float)

    delta1 = float(Cb @ x1 - F[0][0])
    delta2 = float(Cb @ x2 - F[0][1])
    F[0][0] = delta1
    F[0][1] = delta2
    A = np.concatenate([x1, x2], axis=1)
    f_step(A, B, F, Cb, x1, x2, Cj)
    """print(A, "\n", B, "\n", C)
    min_elem = np.nanmin(A)
    min_col = 0
    for i in range(len(A[0])):
        if A[-1][i] == min_elem:
            min_col = i
            break"""