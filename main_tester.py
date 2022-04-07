import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow

import CircleClass
import WideAngleClass
from WideAngleClass import create_equation, check_pos


class GeometryWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("window.ui", self)
        self.center = (400, 300)

    def paintEvent(self, event):
        min_x, max_y = 200, 450
        qp = QPainter()
        qp.begin(self)
        frame_pen = QPen(Qt.black, 3)
        qp.setPen(frame_pen)
        qp.drawLine(min_x, 1, self.width() - 1, 1)
        qp.drawLine(self.width() - 1, 1, self.width() - 1, max_y)
        qp.drawLine(self.width() - 1, max_y, min_x, max_y)
        qp.drawLine(min_x, max_y, min_x, 1)
        my_angle = WideAngleClass.WideAngle(1, 1, 20, 20, 10, 10)
        my_circle = CircleClass.Circle(-20, -20, 20, 20)
        self.draw_angle(qp, my_angle)
        self.draw_circle(qp, my_circle)
        self.draw_cross(qp, my_circle, my_angle)
        qp.end()

    def draw_angle(self, qp, a):
        center_x, center_y = self.center[0], self.center[1]
        # a = WideAngleClass.WideAngle(1, 1, 20, 20, 10, 10)
        qp.setPen(QPen(Qt.green, 2))
        qp.drawLine(a.mainSegment[0] + center_x, a.mainSegment[1] + center_y, a.mainSegment[2] + center_x,
                    a.mainSegment[3] + center_y)
        qp.drawLine(a.firstSegment[0] + center_x, a.firstSegment[1] + center_y, round(a.firstSegment[2]) + center_x,
                    round(a.firstSegment[3]) + center_y)
        qp.drawLine(a.secondSegment[0] + center_x, a.secondSegment[1] + center_y, round(a.secondSegment[2]) + center_x,
                    round(a.secondSegment[3]) + center_y)

    def draw_circle(self, qp, a):
        center_x, center_y = self.center[0], self.center[1]
        # a = CircleClass.Circle(-20, -20, 20, 20)
        x, y = round(center_x + a.center[0] - a.radius), round(center_y + a.center[1] - a.radius)
        qp.setPen(QPen(Qt.green, 2))
        qp.drawEllipse(x, y, round(a.radius) * 2, round(a.radius) * 2)

    def draw_cross(self, qp, circle, angle):
        center_x, center_y = self.center[0], self.center[1]
        c_x, c_y = circle.center[0], circle.center[1]
        r = round(circle.radius)
        m_k, m_b = create_equation(angle.mainSegment[0], angle.mainSegment[1], angle.mainSegment[2],
                                   angle.mainSegment[3])
        k1, b1 = create_equation(angle.firstSegment[0], angle.firstSegment[1], angle.firstSegment[2],
                                 angle.firstSegment[3])
        k2, b2 = create_equation(angle.secondSegment[0], angle.secondSegment[1], angle.secondSegment[2],
                                 angle.secondSegment[3])
        points = list()
        for t in range(2):
            for j in range(c_x - r, c_x + r + 1):
                x = j
                if t == 1:
                    x = 2 * c_x - j
                y = (-1) ** (t + 1) * (r ** 2 - x ** 2) + c_y

            if angle.horizontal:
                pass
            elif angle.vertical:
                pass
            else:
                if check_pos(angle.mainSegment[0], angle.mainSegment[1], angle.mainSegment[2],
                             angle.mainSegment[3], x, y) == angle.pos:
                    pass
                else:
                    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GeometryWidget()
    ex.show()
    sys.exit(app.exec_())
