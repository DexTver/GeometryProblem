import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint
from window import Ui_GeometryProblem

from PlaneClass import Plane, extractNumbers
from WideAngleClass import WideAngle
from CircleClass import Circle


class GeometryWidget(QMainWindow, Ui_GeometryProblem):
    def __init__(self):
        super().__init__()
        # uic.loadUi("window.ui", self)
        self.setupUi(self)
        self.max_x, self.max_y, self.min_x, self.min_y = 799, 449, 199, 1
        self.plane = Plane(500, 225)
        self.LeftBut.clicked.connect(lambda: self.rotatePlane("left"))
        self.RightBut.clicked.connect(lambda: self.rotatePlane("right"))
        self.DownBut.clicked.connect(lambda: self.rotatePlane("down"))
        self.UpBut.clicked.connect(lambda: self.rotatePlane("up"))
        self.ScaleSlider.valueChanged[int].connect(self.scalePlane)
        self.DrawBut.clicked.connect(self.update)
        self.LoadFileBut.clicked.connect(self.loadFromFile)
        self.ClearBut.clicked.connect(self.clearPlane)
        self.AddAngleBut.clicked.connect(self.addAdngle)
        self.AddCircleBut.clicked.connect(self.addCicle)

    def addCicle(self):
        firstCoords = self.CenterCoordCircle.toPlainText()
        secondCoords = self.SecondCoordCircle.toPlainText()
        if firstCoords == "" or secondCoords == "":
            # считывание с мышки
            return None
        else:
            firstCoords = extractNumbers(firstCoords)
            secondCoords = extractNumbers(secondCoords)
        circle = Circle(firstCoords[0], firstCoords[1], secondCoords[0], secondCoords[1])
        self.plane.add(circle)
        self.CenterCoordCircle.setPlainText("")
        self.SecondCoordCircle.setPlainText("")
        self.update()

    def addAdngle(self):
        firstCoords = self.FirstCoordAngle.toPlainText()
        secondCoords = self.SecondCoordAngle.toPlainText()
        thirdCoords = self.ThirdCoordAngle.toPlainText()
        if firstCoords == "" or secondCoords == "" or thirdCoords == "":
            # считывание с мышки
            return None
        else:
            firstCoords = extractNumbers(firstCoords)
            secondCoords = extractNumbers(secondCoords)
            thirdCoords = extractNumbers(thirdCoords)
        angle = WideAngle(firstCoords[0], firstCoords[1], secondCoords[0], secondCoords[1],
                          thirdCoords[0], thirdCoords[1])
        self.plane.add(angle)
        self.FirstCoordAngle.setPlainText("")
        self.SecondCoordAngle.setPlainText("")
        self.ThirdCoordAngle.setPlainText("")
        self.update()

    def clearPlane(self):
        self.plane.clear()
        self.update()

    def loadFromFile(self):
        fname = QFileDialog.getOpenFileName(self, "Выбрать файл с точками", "",
                                            "Текстовый файл (*.txt)")[0]
        print(fname)
        self.plane.addFromFile(fname)
        self.update()

    def scalePlane(self, value):
        self.plane.scale = max(value // 5, 1)
        self.update()

    def rotatePlane(self, command):
        const = 20
        if command == "left":
            self.plane.center = (
                self.plane.center[0] + const * self.plane.scale, self.plane.center[1])
        elif command == "right":
            self.plane.center = (
                self.plane.center[0] - const * self.plane.scale, self.plane.center[1])
        elif command == "up":
            self.plane.center = (
                self.plane.center[0], self.plane.center[1] + const * self.plane.scale)
        elif command == "down":
            self.plane.center = (
                self.plane.center[0], self.plane.center[1] - const * self.plane.scale)
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawShapes(painter)  # рисует все фигуры
        self.drawFrame(painter)  # рисует рамку координатной плоскости
        self.drawBoards(painter)  # закрашивает поле вне координатной плоскости
        painter.end()

    def drawShapes(self, painter):
        self.drawGrid(painter)  # рисует сетку координат
        painter.setPen(QPen(Qt.black, 1))
        for a in self.plane.circles:
            self.drawCircle(painter, a)  # рисует все окружности
        for a in self.plane.angles:
            self.drawAngle(painter, a)  # рисует все "широкие" углы

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
