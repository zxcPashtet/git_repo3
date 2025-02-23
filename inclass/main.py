import sys
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRectF
from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from inclass.Ui import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
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