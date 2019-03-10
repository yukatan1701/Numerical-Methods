import matplotlib.pyplot as plt

x = [0, 50, 100, 120, 200]
y_py = [0, 416, 468, 384, 440]
y_my = [0, 416, 976, 1400, 5136]
plt.plot(x, y_my)
plt.plot(x, y_py)
plt.xlabel("Matrix size")
plt.ylabel("Time, ms")
plt.axis([0, 200, 0, 5200])
plt.show()
