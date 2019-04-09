import matplotlib.pyplot as plt

x = [0, 2000, 4000, 16000, 32000]
y_my = [0, 404, 452, 612, 852]
y_py = [0, 380, 460, 580, 788]
plt.plot(x, y_my)
plt.plot(x, y_py)
plt.xlabel("Matrix size")
plt.ylabel("Time, ms")
plt.axis([0, 32000, 0, 800])
plt.show()