import numpy as np

X = ['x1', 'x2', 'x3', 'x4', 'x5']

def create_simpl_table(A, r, s, r_elem, Cb):
    new_A = A.copy()
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == r:
                continue
            if j == s:
                continue
            if i == 3 and j == 3:
                continue

            new_A[i][j] = ((A[i][j] * r_elem) - (A[i][s] * A[r][j])) / r_elem

    new_A[r][s] = r_elem ** -1
    for i in range(len(A[0])):
        if i != s:
            new_A[r][i] /= r_elem

    for j in range(len(A)):
        if j != r:
            new_A[j][s] = -(A[j][s] / r_elem)

    return new_A


def f_step(A, B, F, Cb, x1, x2, Cj):
    global X
    Q = np.array([[0]])
    Q = np.insert(Q, 0, Cb @ B, axis=0)
    Q = np.delete(Q, 1, axis=0)

    bas = F.min()
    bas_ind = np.where(F[0] == bas)
    tmp = 1
    if bas_ind[0][0] == 0:
        tmp = 0
    Cb[bas_ind[0][0] + tmp] = -bas

    min_q = 1000
    min_q_ind = 0
    for i in range(len(A)):
        if A[i][bas_ind] > 0:
            temp_m = B[i]/A[i][bas_ind]
            if temp_m < min_q:
                min_q = temp_m
                min_q_ind = i


    Cj[min_q_ind] = X[bas_ind[0][0]]
    for i in range(len(Cj)):
        if Cj[i] == 'x1':
            Cb[i] = 10
        if Cj[i] == 'x3':
            Cb[i] = 30

    r_elem = A[min_q_ind][bas_ind[0][0]]

    B = np.concatenate([B, Q])
    A = np.concatenate([A, F])
    A = np.concatenate([A, B], axis=1)

    new_A = create_simpl_table(A, min_q_ind, bas_ind[0][0], r_elem, Cb)
    if new_A[3][0] < 0 or new_A[3][1] < 0:
        r_A = new_A[:, :2][:-1]
        r_B = new_A[:, 2:][:3]
        r_F = new_A[:, :2][3:]
        x1 = new_A[:, :1][:-1]
        x2 = new_A[:, 1:2][:-1]
        return f_step(r_A, r_B, r_F, Cb, x1, x2, Cj)
    else:
        r_B = new_A[:, 2][:-1]
        new_A[3][2] = Cb @ r_B
        #res = ((new_A[n][m] * r_elem) - (new_A[n - 1][m] * new_A[n][m - 1])) / r_elem
        return (Cb, Cj)


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



