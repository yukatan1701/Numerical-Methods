import numpy as np
import time
import random
import numpy.linalg as lg
import scipy.linalg as sla
import matplotlib.pyplot as plt

def generate_matrix():
    np.random.seed(n)
    random.seed(n)
    a = np.random.rand(n, n)
    for i in range(n):
        for j in range(n):
            a[i][j] = int(a[i][j] * 10)
    f = [random.randint(0, 10) for _ in range(n)]
    for i in range(n):
    	a[i][i] = sum([abs(val) for val in a[i]]) + abs(a[i][i])
    return a, f

def diff(x1, x2):
    return lg.norm(x1 - x2)

def jacobi(a, f, x):
    xnew = np.zeros(n)
    for i in range(n):
        s = 0
        for j in range(i - 1):
            s = s + a[i][j] * x[j]
        for j in range(i + 1, n):
            s = s + a[i][j] * x[j]
        xnew[i] = (f[i] - s) / a[i][i]
    return xnew

def jacobi_solve(a, f):
    eps = 0.000001
    xnew = np.zeros(n)
    while True:
        x = xnew
        xnew = jacobi(a, f, x)
        if diff(x, xnew) <= eps:
            break
    return xnew

size = list(range(10, 101, 10))
y_solve, y_jacobi = [0], [0]
print("Size\tLibrary time\tJacobi time")
for n in size:
	a, f = generate_matrix()
	t0 = time.time()
	x1 = sla.solve(a, f)
	t1 = time.time() - t0

	t0 = time.time()
	x2 = jacobi_solve(a, f)
	t2 = time.time() - t0
	#print("Size: ", n, "| Time: %.3f" % t1, "%.3f" % t2)
	print(n, "\t%.4f" % t1, "\t\t%.4f" % t2, sep = '')
	y_solve.append(t1)
	y_jacobi.append(t2)
	
x = [0] + size
plt.plot(x, y_solve, label = "Library")
plt.plot(x, y_jacobi, label = "Jacobi")
plt.legend(loc = "upper left")
plt.xlabel("Matrix size")
plt.ylabel("Time, s")
plt.axis([0, size[-1], 0, y_jacobi[-1]])
plt.savefig('jacobi.png', bbox_inches='tight')
plt.show()
