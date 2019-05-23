import numpy as np
import matplotlib.pyplot as plt
import sys

def readData(filename):
	f = open(filename, 'r')
	x = [float(line) for line in f]
	f.close()
	return x
	
def sweep(n, a, b, c, f):
	alpha = np.zeros(n + 1)
	beta = np.zeros(n + 1)
	for i in range(n):
		d = a[i] * alpha[i] + b[i]
		alpha[i + 1] = -c[i] / d
		beta[i + 1] = (f[i] - a[i] * beta[i]) / d
	x = np.zeros(n)
	x[n - 1] = beta[n]
	for i in range(n - 2, -1, -1):
		x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
	return x	
	
def generateSpline(x, y):
	n = x.shape[0] - 1
	h = (x[n] - x[0]) / n
	
	a = np.array([0] + [1] * (n - 1) + [0])
	b = np.array([1] + [4] * (n - 1) + [1])
	c = np.array([0] + [1] * (n - 1) + [0])
	f = np.zeros(n + 1)
	for i in range(1, n):
		f[i] = 3 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2
	B = sweep(n + 1, a, b, c, f)
	
	A = np.zeros(n + 1)
	C = np.zeros(n + 1)
	D = np.zeros(n + 1)
	for i in range(n):
		A[i] = (B[i + 1] - B[i]) / (3 * h)
		C[i] = (y[i + 1] - y[i]) / h - (B[i + 1] + 2 * B[i]) * h / 3
		D[i] = y[i]
	return A, B, C, D

def P(z):
	i = int(z)
	diff = z - x[i]
	return A[i] * diff ** 3 + B[i] * diff ** 2 + C[i] * diff + D[i]	
		
x = np.array(readData('train.dat'))
y = np.array(readData('train.ans'))
test_x = readData('test.dat')
test_y = []
assert(len(x) == len(y))
n = len(x)

A, B, C, D = generateSpline(x, y)

for z in test_x:
	test_y.append(P(z))

out = open('test.ans', 'w')
for ans in test_y:
	out.write(str(ans) + '\n')	
out.close()

if len(sys.argv) == 1 or sys.argv[1] != '-p':
	quit()

plot_x, plot_y = [], []
z = 0.0
while z < (test_x[-1]):
	plot_x.append(z)
	plot_y.append(P(z)) 
	z += 0.1
	
plt.plot(plot_x, plot_y, label='Spline interpolation')
plt.plot(test_x, test_y, 'ro', label='Test points')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = "upper left")
plt.savefig('spline.png', bbox_inches='tight')
plt.show()
