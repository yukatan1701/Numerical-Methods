import numpy as np

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

z = 0.0
plot = open('plot.txt', 'w')
while z < (test_x[-1]):
	plot.write(str(z) + ' ' + str(P(z)) + '\n')
	z += 0.1
plot.close()

for z in test_x:
	test_y.append(P(z))

out = open('test.ans', 'w')
for ans in test_y:
	out.write(str(ans) + '\n')	
out.close()
