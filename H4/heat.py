from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

def on_button_clicked():
	alert = QMessageBox()
	alert.setText("Hello!")
	alert.exec_()

def getPos(event):
	x = event.pos().x()
	y = event.pos().y()
	print(x, y)

def u0(x, y):
	return np.exp(-(x * x + y * y) / 4)

def u(x, y, t):
	return 1 / np.sqrt(t + 1) * np.exp(-(x * x + y * y) / (4 * (t + 1)))

mu = 1.0
T = 2.0
L, R = -10, 10
n = 50
m = 50
h = (R - L) / n
tau = T / m
x = np.linspace(L, R, n + 1)
t = np.linspace(0.0, T, m + 1)
y = np.zeros((m + 1, n + 1, n + 1))


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
label = QLabel()
button = QPushButton('Push')

pixmap = QPixmap(n, n)
pixmap.fill(Qt.white)
painter = QPainter()
painter.begin(pixmap)

label.setPixmap(pixmap)
label.mousePressEvent = getPos
button.clicked.connect(on_button_clicked)
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()
