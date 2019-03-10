import numpy as np
import numpy.linalg as lg

def generate_matrix(n):
    np.random.seed(n)
    a = np.random.rand(n, n)
    for i in range(n):
        for j in range(n):
            a[i][j] = int(a[i][j] * 10)
    f = [np.random.randint(0, 10) for _ in range(n)]
    for i in range(n):
    	a[i][i] = sum([abs(val) for val in a[i]]) + abs(a[i][i])
    return a, f

def diff(x1, x2):
    return lg.norm(x1 - x2)

def seidel(a, f, x, n):
    xnew = np.zeros(n)
    for i in range(n):
        s = 0
        for j in range(i - 1):
            s = s + a[i][j] * xnew[j]
        for j in range(i + 1, n):
            s = s + a[i][j] * x[j]
        xnew[i] = (f[i] - s) / a[i][i]
    return xnew

def solve(a, f, n):
    eps = 0.000001
    xnew = np.zeros(n)
    while True:
        x = xnew
        xnew = seidel(a, f, x, n)
        if diff(x, xnew) <= eps:
            break
    return xnew

n = int(input())
a, f = generate_matrix(n)
for i in range(n):
    print(a[i])
print(f)
print(solve(a, f, n))
