import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen, QPolygon
from PyQt5.QtWidgets import QApplication, QMainWindow

import CircleClass
from PlaneClass import Plane
import WideAngleClass
from WideAngleClass import create_equation, check_pos
from math import sqrt


class GeometryWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("window.ui", self)
        self.center = (400, 300)
        self.max_x, self.max_y, self.min_x, self.min_y = 799, 449, 199, 1
        self.plane = Plane(500, 225)

    def paintEvent(self, event):
        min_x, max_y = 200, 450
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QPen(Qt.black, 3))
        self.drawGrid(qp)
        # my_angle = WideAngleClass.WideAngle(1, 1, 1, 20, 10, 10)
        # my_circle = CircleClass.Circle(70, 40, 100, -20)
        my_angle = WideAngleClass.WideAngle(1, 1, 20, 20, 10, 10)
        my_circle = CircleClass.Circle(-20, -20, 20, 20)
        self.draw_angle(qp, my_angle)
        self.draw_circle(qp, my_circle)
        self.draw_cross(qp, my_circle, my_angle)
        self.drawFrame(qp)
        self.drawBoards(qp)
        qp.end()

    def draw_angle(self, qp, a):
        center_x, center_y = self.center[0], self.center[1]
        # a = WideAngleClass.WideAngle(1, 1, 20, 20, 10, 10)
        qp.setPen(QPen(Qt.green, 2))
        qp.drawLine(a.mainSegment[0] + center_x, a.mainSegment[1] + center_y,
                    a.mainSegment[2] + center_x,
                    a.mainSegment[3] + center_y)
        qp.drawLine(a.firstSegment[0] + center_x, a.firstSegment[1] + center_y,
                    round(a.firstSegment[2]) + center_x,
                    round(a.firstSegment[3]) + center_y)
        qp.drawLine(a.secondSegment[0] + center_x, a.secondSegment[1] + center_y,
                    round(a.secondSegment[2]) + center_x,
                    round(a.secondSegment[3]) + center_y)

    def draw_circle(self, qp, a):
        center_x, center_y = self.center[0], self.center[1]
        qp.setPen(QPen(Qt.green, 2))
        # a = CircleClass.Circle(-20, -20, 20, 20)
        x, y = round(center_x + a.center[0] - a.radius), round(center_y + a.center[1] - a.radius)
        qp.setPen(QPen(Qt.green, 2))
        qp.drawEllipse(x, y, round(a.radius) * 2, round(a.radius) * 2)

    def draw_cross(self, qp, circle, angle):
        qp.setPen(QPen(Qt.red, 1))
        center_x, center_y = self.center[0], self.center[1]
        c_x, c_y = circle.center[0], circle.center[1]
        r = round(circle.radius)
        x1, y1, x2, y2 = angle.mainSegment[0], angle.mainSegment[1], angle.mainSegment[2], \
                         angle.mainSegment[3]
        x4, y4, x5, y5 = angle.firstSegment[2], angle.firstSegment[3], angle.secondSegment[2], \
                         angle.secondSegment[3]
        m_k, m_b = create_equation(x1, y1, x2, y2)
        k1, b1 = create_equation(x1, y1, x4, y4)
        k2, b2 = create_equation(x2, y2, x5, y5)
        points = list()
        for x in range(c_x - r, c_x + r + 1):
            dy = round(sqrt(abs(circle.radius ** 2 - (x - c_x) ** 2)))
            for y in [c_y + dy, c_y - dy]:
                if check_pos(x1, y1, x2, y2, x, y) == angle.pos and check_pos(
                        x1, y1, x4, y4, x, y) != check_pos(x2, y2, x5, y5, x, y):
                    points.append(QPoint(x + center_x, y + center_y))
            y, yo = c_y + dy, c_y - dy
            if min(x1, x2) <= x <= max(x1, x2):
                Y = round(m_k * x + m_b)
                if yo <= Y <= y:
                    points.append(QPoint(x + center_x, Y + center_y))
            if min(x1, x4) <= x <= max(x1, x4):
                Y = round(k1 * x + b1)
                if yo <= Y <= y:
                    points.append(QPoint(x + center_x, Y + center_y))
            if min(x2, x5) <= x <= max(x2, x5):
                Y = round(k2 * x + b2)
                if yo <= Y <= y:
                    points.append(QPoint(x + center_x, Y + center_y))
        qp.drawPolygon(QPolygon(points))

    def drawFrame(self, painter):
        # рисует рамку
        painter.setPen(QPen(Qt.black, 3))
        frame = [QPoint(self.max_x, self.max_y), QPoint(self.max_x, self.min_y),
                 QPoint(self.min_x, self.min_y),
                 QPoint(self.min_x, self.max_y)]
        painter.drawPolygon(QPolygon(frame))

    def drawBoards(self, painter):
        # рисует белое поле вне координатной плоскости, чтобы убрать выходящие за границы элементы
        painter.setBrush(Qt.white)
        points = [QPoint(0, 0), QPoint(self.min_x - 2, 0), QPoint(self.min_x - 2, self.max_y + 2)]
        points += [QPoint(self.width(), self.max_y + 2), QPoint(self.width(), self.height())]
        points += [QPoint(0, self.height())]
        painter.drawPolygon(QPolygon(points))

    def drawGrid(self, painter):
        # рисует сетку координат
        c_x, c_y = self.plane.center
        s = self.plane.scale
        painter.setPen(QPen(Qt.black, 2))
        painter.drawLine(self.min_x, c_y, self.max_x, c_y)
        painter.drawLine(c_x, self.min_y, c_x, self.max_y)
        # рисует стрелочки
        xArrow = [QPoint(self.max_x - 10, c_y - 5), QPoint(self.max_x - 1, c_y),
                  QPoint(self.max_x - 10, c_y + 5)]
        yArrow = [QPoint(c_x - 5, self.min_y + 10), QPoint(c_x, self.min_y + 1),
                  QPoint(c_x + 5, self.min_y + 10)]
        painter.drawPolygon(QPolygon(xArrow))
        painter.drawPolygon(QPolygon(yArrow))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GeometryWidget()
    ex.show()
    sys.exit(app.exec_())
