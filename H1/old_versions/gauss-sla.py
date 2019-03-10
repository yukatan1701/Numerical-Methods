import numpy as np
import scipy.linalg as sla

n = int(input())
a = np.random.rand(n, n)
f = [val for val in range(n)]
for i in range(n):
	a[i][i] = sum([abs(val) for val in a[i]]) + abs(a[i][i])
print(sla.solve(a, f))
