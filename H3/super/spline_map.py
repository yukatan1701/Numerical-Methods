from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QPen, QPolygon
import sys
import numpy as np

density = 100

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
	#print("Inside spline: ", x, y)
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
	#print("Args: ", A, B, C, D)
	return A, B, C, D

def P(z, x, A, B, C, D):
	i = z // density
	diff = z - x[i]
	#print(A[i], B[i], C[i], D[i])
	return A[i] * diff ** 3 + B[i] * diff ** 2 + C[i] * diff + D[i]	

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.InitWindow()
		
	def InitWindow(self):
		wid = QWidget(self)
		self.setCentralWidget(wid)
		layout = QVBoxLayout()
		label = QLabel()
		button = QPushButton('Reset')
		button.clicked.connect(self.on_button_clicked)
		layout.addWidget(label)
		layout.addWidget(button)
		self.points = QPolygon()
		wid.setLayout(layout)
		self.title = "Splines"
		self.top = 0
		self.left = 0
		self.width = n
		self.height = n
	
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		
	def mousePressEvent(self, event):
		x = event.pos().x()
		y = event.pos().y()
		self.points << event.pos()
		self.update()
		
	def generateParam(self):
		size = self.points.count()
		x, y = np.zeros(size), np.zeros(size)
		i = 0
		for point in self.points:
			x[i] = point.x()
			y[i] = point.y()
			i += 1
		t = np.array([i * density for i in range(size)])
		self.Ay, self.By, self.Cy, self.Dy = generateSpline(t, y)
		self.Ax, self.Bx, self.Cx, self.Dx = generateSpline(t, x)
		return x, y, t
	
	def V(self, T, t):
		tx = P(t, T, self.Ax, self.Bx, self.Cx, self.Dx)
		ty = P(t, T, self.Ay, self.By, self.Cy, self.Dy)
		return QPoint(tx, ty)
		
	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine, Qt.RoundCap))
		painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
		count = self.points.count()
		painter.setRenderHint(QPainter.Antialiasing)
		if count > 1:
			X, Y, T = self.generateParam()
			begin = int(T[0])
			end = int(T[count-1])
			pts = []
			for t in range(begin, end):
				p = self.V(T, t)
				if len(pts) > 0:
					painter.drawLine(pts[-1], p)
				else:
					painter.drawPoint(p)
				pts.append(p)
		painter.setPen(QPen(Qt.darkBlue, 2, Qt.SolidLine, Qt.RoundCap))
		for i in range(count):
			painter.drawEllipse(self.points.point(i), 3, 3)
			if i > 0:
				painter.drawEllipse(self.points.point(i), 3, 3)
	def on_button_clicked(self):
		self.points.clear()
		self.update()

n = 500
if __name__ == '__main__':
	if len(sys.argv) > 2:
		if sys.argv[1] == '-d':
			density = int(sys.argv[2])
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
