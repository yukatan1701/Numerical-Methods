from PyQt5.QtCore import Qt, QPoint, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QPen, QPolygon, QColor
import sys
import numpy as np

def f():
	coef = (c * tau / h) ** 2
	new_table = np.zeros((n, n))
	global table, subtable
	for i in range(1, n - 1):
		for j in range(1, n - 1):
			new_table[i][j] = 2 * table[i][j] - subtable[i][j] + coef * \
				(table[i - 1][j] + table[i + 1][j] + \
				table[i][j - 1] + table[i][j + 1] - 4 * table[i][j])
			#if (new_table[i][j] < 1):
			#	new_table[i][j] = 0.0
	subtable = table
	table = new_table

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.InitWindow()
		
	def InitWindow(self):
		wid = QWidget(self)
		self.setCentralWidget(wid)
		layout = QVBoxLayout()
		label = QLabel()
		layout.addWidget(label)
		self.points = QPolygon()
		wid.setLayout(layout)
		self.title = "Splines"
		self.top = 0
		self.left = 0
		self.width = n
		self.height = n
		self.timer = QTimer(self)
		self.timer.setInterval(100)
		self.timer.timeout.connect(self.blink)
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.timer.start()
		
	def blink(self):
		f()
		self.update()
		
	def mousePressEvent(self, event):
		x = event.pos().x()
		y = event.pos().y()
		table[y][x] = 255.0
		
	def paintEvent(self, event):
		painter = QPainter(self)
		for i in range(n):
			for j in range(n):
				if table[i][j] > 0.0 and table[i][j] < 1024.0:
					painter.setPen(QPen(QColor(255 - int(table[i][j]) % 256, 255 - int(table[i][j]) % 256, 255), 1, Qt.SolidLine))
				elif table[i][j] > 1024.0:
					painter.setPen(QPen(QColor(0, 0, 255), 1, Qt.SolidLine))
				else:
					painter.setPen(QPen(QColor(255, 255, 255), 1, Qt.SolidLine))
				painter.drawPoint(j, i)
		
	def on_button_clicked(self):
		self.points.clear()
		self.update()	

n = 100

c = 0.25
tau = 0.5
h = 1.0

table = np.zeros((n, n))
subtable = np.zeros((n, n))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
