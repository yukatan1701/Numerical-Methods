import time
import numpy as np
import scipy.linalg as sla
import matplotlib.pyplot as plt

def generate_matrix(n):
	#np.random.seed(n)
	a = np.random.rand(n, n)
	for i in range(n):
		for j in range(n):
			a[i][j] = int(a[i][j] * 10)
	f = [np.random.randint(0, 10) for _ in range(n)]
	for i in range(n):
		a[i][i] = sum([abs(val) for val in a[i]]) + abs(a[i][i])
	return a, f

def gauss(a, f):
	for k in range(n):
		a[k, k + 1:] /= a[k, k]
		f[k] /= a[k][k]
		for i in range(k + 1, n):
			a[i, k + 1:] -= a[i][k] * a[k, k + 1:]
			f[i] -= a[i][k] * f[k]
		a[k + 1:, k] = np.zeros(n - k - 1)
	x = np.array([float(0)] * n)
	for i in range(n - 1, -1, -1):
		x[i] = f[i]
		for j in range(i + 1, n):
			x[i] -= a[i][j] * x[j]
	return x


size = list(range(100, 501, 20))
y_solve, y_gauss = [0], [0]
print("Size\tLibrary time\tGauss time")
for n in size:
	a, f = generate_matrix(n)
	t0 = time.time()
	x1 = sla.solve(a, f)
	t1 = time.time() - t0

	t0 = time.time()
	x2 = gauss(a, f)
	t2 = time.time() - t0
	assert(np.allclose(x2, x1))
	#print("Size: ", n, "| Time: %.3f" % t1, "%.3f" % t2)
	print(n, "\t%.4f" % t1, "\t\t%.4f" % t2, sep = '')
	y_solve.append(t1)
	y_gauss.append(t2)
	
x = [0] + size
plt.plot(x, y_solve, label = "Library")
plt.plot(x, y_gauss, label = "Gauss")
plt.legend(loc = "upper left")
plt.xlabel("Matrix size")
plt.ylabel("Time, s")
plt.axis([0, size[-1], 0, y_gauss[-1]])
plt.savefig('gauss.png', bbox_inches='tight')
plt.show()
