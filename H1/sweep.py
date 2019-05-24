import numpy as np
import scipy.linalg as sla
import time
import matplotlib.pyplot as plt

def generate_matrix(n):
	a = np.zeros((n, n))
	for i in range(1, n - 1):
		for j in range(i - 1, i + 2):
			a[i][j] = np.random.randint(1, 10)
		a[i][i] = abs(a[i][i]) + abs(a[i][i - 1]) + abs(a[i][i + 1])
	a[0][0] = np.random.randint(1, 10)
	a[0][1] = np.random.randint(1, 10)
	a[n - 1][n - 2] = np.random.randint(1, 10)
	a[n - 1][n - 1] = np.random.randint(1, 10)
	f = [np.random.randint(1, 10) for _ in range(n)]
	return a, f

def get_abc(mx, n):
	a = np.insert(np.diag(mx, -1), 0, 0)
	b = np.diag(mx)
	c = np.insert(np.diag(mx, 1), len(b)-1, 0)
	return a, b, c

def sweep(a, b, c, f, n):
	alpha = [0.0] * (n + 1)
	beta = [0.0] * (n + 1)
	for i in range(n):
		d = a[i] * alpha[i] + b[i]
		alpha[i + 1] = -c[i] / d
		beta[i + 1] = (f[i] - a[i] * beta[i]) / d
	x = [0.0] * n
	x[n - 1] = beta[n]
	for i in range(n - 2, -1, -1):
		x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
	return x

def SolveBanded(mx, f):
	ud = np.insert(np.diag(mx, 1), 0, 0) # upper diagonal
	d = np.diag(mx) # main diagonal
	ld = np.insert(np.diag(mx, -1), len(d)-1, 0) # lower diagonal
	return sla.solve_banded((1, 1), np.matrix([ud, d, ld]), f)


size = list(range(1000, 30001, 1500))
y_solve, y_sweep = [0], [0]
print("Size\tLibrary time\tSweep time")
for n in size:
	mx, f = generate_matrix(n)
	
	t0 = time.time()
	x2 = SolveBanded(mx, f)
	t1 = time.time() - t0
	
	t0 = time.time()
	a, b, c = get_abc(mx, n)
	x1 = sweep(a, b, c, f, n)
	t2 = time.time() - t0
	
	assert(np.allclose(x1, x2))
	print(n, "\t%.4f" % t1, "\t\t%.4f" % t2, sep = '')
	y_solve.append(t1)
	y_sweep.append(t2)
	
x = [0] + size
plt.plot(x, y_solve, label = "Library")
plt.plot(x, y_sweep, label = "Sweep")
plt.legend(loc = "upper left")
plt.xlabel("Matrix size")
plt.ylabel("Time, s")
y_max = max(max(y_solve), max(y_sweep))
plt.axis([0, size[-1], 0, y_max])
plt.savefig('sweep.png', bbox_inches='tight')
plt.show()
