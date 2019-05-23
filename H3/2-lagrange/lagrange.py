import numpy as np
import matplotlib.pyplot as plt
import sys

def readData(filename):
	f = open(filename, 'r')
	x = [float(line) for line in f]
	f.close()
	return x
	
def phi(i, z):
	p = 1
	for j in range(n):
		if i == j:
			continue
		p *= (z - x[j]) / (x[i] - x[j])
	return p

def P(z):
	s = 0
	for i in range(n):
		s += y[i] * phi(i, z)
	return s
	
x = np.array(readData('train.dat'))
y = np.array(readData('train.ans'))
test_x = readData('test.dat')
test_y = []
assert(len(x) == len(y))
n = len(x)

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

plt.plot(plot_x, plot_y, label='Lagrange interpolation')
plt.plot(test_x, test_y, 'ro', label='Test points')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = "upper left")
plt.savefig('lagrange.png', bbox_inches='tight')
plt.show()
