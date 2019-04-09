import numpy as np
import random
import scipy.linalg as sla

def generate_matrix(n):
	a = np.zeros((n, n))
	for i in range(1, n - 1):
		for j in range(i - 1, i + 2):
			a[i][j] = random.randint(1, 10)
		a[i][i] = abs(a[i][i]) + abs(a[i][i - 1]) + abs(a[i][i + 1])
	a[0][0] = random.randint(1, 10)
	a[0][1] = random.randint(1, 10)
	a[n - 1][n - 2] = random.randint(1, 10)
	a[n - 1][n - 1] = random.randint(1, 10)
	f = [random.randint(1, 10) for _ in range(n)]
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

n = int(input())
mx, f = generate_matrix(n)
a, b, c = get_abc(mx, n)
#for i in range(n):
#	print(mx[i])
#print(f)
#print(a, b, c)
x = sweep(a, b, c, f, n)
#print(SolveBanded(mx, f))
print(x)
