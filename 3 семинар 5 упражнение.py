import numpy as np
N = int(input())
M = int(input())
def new_matrix(N, M):
    matrix = np.zeros((N, M), dtype=int)
    left, right = 0, M - 1
    top, bottom = 0, N - 1
    num = 1
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    return matrix
print(new_matrix(N, M))