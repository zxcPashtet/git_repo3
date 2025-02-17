import sys
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRectF
from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 745, 617)
        self.setWindowTitle('Рисование')
        self.pushButton = QPushButton('Создать', self)
        self.pushButton.move(230, 490)
        self.pushButton.resize(271, 71)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randint(0, 700)
        y = randint(0, 450)
        r = randint(0, 100)
        rectangle = QRectF(x, y, r, r)
        qp.drawEllipse(rectangle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())