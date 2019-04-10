def readData(filename):
	f = open(filename, 'r')
	x = [float(line) for line in f]
	f.close()
	return x
	
def f(i, x, y, z):
	if i == len(x):
		return y[-1]
	return (y[i + 1] - y[i]) / (x[i + 1] - x[i]) * (z - x[i]) + y[i]
	
x = readData('train.dat')
y = readData('train.ans')
test_x = readData('test.dat')
test_y = []
assert(len(x) == len(y))
n = len(x) - 1
i = 0
for z in test_x:
	while z > x[i]:
		i += 1
	if i > 0:
		i -= 1
	test_y.append(f(i, x, y, z))

out = open('test.ans', 'w')
for ans in test_y:
	out.write(str(ans) + '\n')	
out.close()
