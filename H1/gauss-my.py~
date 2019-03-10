import numpy as np
import random
import scipy.linalg as sla

def generate_matrix(n):
	a = np.random.rand(n, n)
	for i in range(n):
		for j in range(n):
			a[i][j] = int(a[i][j] * 10)
	f = [random.randint(0, 10) for _ in range(n)]
	for i in range(n):
		a[i][i] = sum([abs(val) for val in a[i]]) + abs(a[i][i])
	return a, f

n = int(input())
a, f = generate_matrix(n)
for i in range(n):
	print(a[i])
print(f)
print(sla.solve(a, f))

for k in range(n):
	for j in range(k + 1, n):
		a[k][j] = a[k][j] / a[k][k]
	f[k] = f[k] / a[k][k]
	for i in range(k + 1, n):
		for j in range(k + 1, n):
			a[i][j] = a[i][j] - a[i][k] * a[k][j]
		f[i] = f[i] - a[i][k] * f[k]
		a[i][k] = 0
x = np.array([float(0)] * n)
for i in range(n - 1, -1, -1):
	x[i] = f[i]
	for j in range(i + 1, n):
		x[i] = x[i] - a[i][j] * x[j]
print(x)
