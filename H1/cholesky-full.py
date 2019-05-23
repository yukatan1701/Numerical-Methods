import matplotlib.pyplot as plt
import time
import numpy as np
import scipy.linalg as lg

def generate_matrix(n):
	a = np.zeros((n, n))
	for i in range(n):
		for j in range(i + 1, n):
			a[i, j] = np.random.randint(0, 10)
			a[j, i] = a[i][j]
		a[i, i] = sum([abs(val) for val in a[i]])
	f = np.random.randint(low = 0, high = 10, size = (n, ))
	return a, f

def get_s(a, n):
	s = np.zeros((n, n))
	for i in range(n):
		sq_sum = 0.0
		for k in range(i):
			sq_sum += s[k, i] ** 2
		s[i, i] = (a[i, i] - sq_sum) ** 0.5
		for j in range(i + 1, n):
			s_sum = 0.0
			for k in range(i):
				s_sum += s[k, i] * s[k, j]
			s[i, j] = (a[i, j] - s_sum) / s[i, i]
	return s

def l_reverse(a, f):
	x = np.array([float(0)] * n)
	for i in range(n):
		x[i] = f[i]
		for j in range(0, i):
			x[i] -= a[i, j] * x[j]
		x[i] /= a[i, i]
	return x

def u_reverse(a, f):
	x = np.array([float(0)] * n)
	for i in range(n - 1, -1, -1):
		x[i] = f[i]
		for j in range(i + 1, n):
			x[i] -= a[i, j] * x[j]
		x[i] /= a[i, i]
	return x

size = list(range(100, 201, 10))
y_solve, y_chol = [0], [0]
print("Size\tLibrary time\tCholesky time")
for n in size:
	a, f = generate_matrix(n)
	
	t0 = time.time()
	c, low = lg.cho_factor(a)
	x1 = lg.cho_solve((c, low), f)
	t1 = time.time() - t0
	
	t0 = time.time()
	s = get_s(a, n)
	y = l_reverse(np.transpose(s), f)
	x2 = u_reverse(s, y)
	t2 = time.time() - t0
	
	assert(np.allclose(x1, x2))
	print(n, "\t%.4f" % t1, "\t\t%.4f" % t2, sep = '')
	y_solve.append(t1)
	y_chol.append(t2)

x = [0] + size
plt.plot(x, y_solve, label = "Library")
plt.plot(x, y_chol, label = "Cholesky")
plt.legend(loc = "upper left")
plt.xlabel("Matrix size")
plt.ylabel("Time, s")
plt.axis([0, size[-1], 0, y_chol[-1]])
plt.savefig('cholesky.png', bbox_inches='tight')
plt.show()
