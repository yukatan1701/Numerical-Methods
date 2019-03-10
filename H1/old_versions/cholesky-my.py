import numpy as np
import random
import scipy.linalg as sla

def generate_matrix(n):
	a = np.zeros((n, n))
	for i in range(n):
		for j in range(i + 1, n):
			a[i][j] = random.randint(0, 10)
			a[j][i] = a[i][j]
		a[i][i] = sum([abs(val) for val in a[i]])
	f = [random.randint(0, 10) for _ in range(n)]
	return a, f

def get_s(a, n):
	s = np.zeros((n, n))
	for i in range(n):
		sq_sum = 0
		for k in range(i - 1):
			sq_sum = sq_sum + s[k][i] ** 2
		s[i][i] = (a[i][i] - sq_sum) ** 0.5
		for j in range(i + 1, n):
			s_sum = 0
			for k in range(i - 1):
				s_sum = s_sum + s[k][i] * s[k][j]
			s[i][j] = (a[i][j] - s_sum) / s[i][i]
	return s

n = int(input())
a, f = generate_matrix(n)
for i in range(n):
	print(a[i])
print(f)
s = get_s(a, n)
for i in range(n):
	print(s[i])
l = sla.cholesky(a)
print()
for i in range(n):
	print(l[i])
y = sla.solve(np.transpose(s), f)
x = sla.solve(s, y)
print(sla.solve(a, f))
print(x)
