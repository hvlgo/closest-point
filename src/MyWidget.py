from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import closest_point as cp


class MyWidget(QWidget):

    points = []
    closest = []
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.points.append((e.pos().x(), e.pos().y()))
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        pen = QPen()
        pen.setWidth(8)
        pen.setColor(Qt.GlobalColor.black)
        qp.setPen(pen)
        for item in self.points:
            qp.drawPoint(item[0], item[1])
        pen.setColor(Qt.GlobalColor.red)
        qp.setPen(pen)
        for item in self.closest:
            qp.drawPoint(item[0], item[1])
        if self.closest != []:
            qp.drawLine(self.closest[0][0], self.closest[0][1], self.closest[1][0], self.closest[1][1])
        qp.end()

    def calculate(self):
        self.closest.clear()
        if len(self.points) == 0 or len(self.points) == 1:
            return
        cp.points = self.points[:]
        answer = cp.divide_closest_point()
        self.closest.append(answer[1])
        self.closest.append(answer[2])
        self.update()


    def clear(self):
        self.points.clear()
        self.closest.clear()
        self.update()