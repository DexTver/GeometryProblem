import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint
from window import Ui_GeometryProblem

from PlaneClass import Plane


class GeometryWidget(QMainWindow, Ui_GeometryProblem):
    def __init__(self):
        super().__init__()
        # uic.loadUi("window.ui", self)
        self.setupUi(self)
        self.max_x, self.max_y, self.min_x, self.min_y = 799, 449, 199, 1
        self.plane = Plane(500, 225, 2)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawShapes(painter)

    def drawShapes(self, painter):
        self.drawGrid(painter)  # рисует сетку координат
        painter.setPen(QPen(Qt.black, 1))
        for a in self.plane.circles:
            self.drawCircle(painter, a)  # рисует все окружности
        for a in self.plane.angles:
            self.drawAngle(painter, a)  # рисует все "широкие" углы
        self.drawFrame(painter)  # рисует рамку координатной плоскости
        self.drawBoards(painter)  # закрашивает поле вне координатной плоскости

    def drawGrid(self, painter):
        # рисует сетку координат
        c_x, c_y = self.plane.center
        s = self.plane.scale
        painter.setPen(QPen(Qt.black, 2))
        painter.drawLine(self.min_x, c_y, self.max_x, c_y)
        painter.drawLine(c_x, self.min_y, c_x, self.max_y)
        # рисует стрелочки
        xArrow = [QPoint(self.max_x - 10 * s, c_y - 5 * s), QPoint(self.max_x - 1, c_y),
                  QPoint(self.max_x - 10 * s, c_y + 5 * s)]
        yArrow = [QPoint(c_x - 5 * s, self.min_y + 10 * s), QPoint(c_x, self.min_y + 1),
                  QPoint(c_x + 5 * s, self.min_y + 10 * s)]
        painter.drawPolygon(QPolygon(xArrow))
        painter.drawPolygon(QPolygon(yArrow))

    def drawAngle(self, painter, a):
        # рисует угол
        c_x, c_y = self.plane.center
        s = self.plane.scale
        x1, y1, x2, y2, x4, y4, x5, y5 = a.mainSegment[0] * s, -a.mainSegment[1] * s, a.mainSegment[
            2] * s, -a.mainSegment[3] * s, a.firstSegment[2] * s, -a.firstSegment[3] * s, \
                                         a.secondSegment[2] * s, -a.secondSegment[3] * s
        # Знак Y меняется, т.к. система координат в окне
        # зеркально отражена привычной Декартовой системе.
        painter.drawLine(x1 + c_x, y1 + c_y, x2 + c_x, y2 + c_y)
        painter.drawLine(x1 + c_x, y1 + c_y, x4 + c_x, y4 + c_y)
        painter.drawLine(x2 + c_x, y2 + c_y, x5 + c_x, y5 + c_y)

    def drawCircle(self, painter, a):
        # рисует окружность
        c_x, c_y = self.plane.center
        s = self.plane.scale
        x, y = round(c_x + (a.center[0] - a.radius) * s), round(c_y - (a.center[1] + a.radius) * s)
        painter.drawEllipse(x, y, round(a.radius * s) * 2, round(a.radius * s) * 2)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GeometryWidget()
    ex.show()
    sys.exit(app.exec_())
