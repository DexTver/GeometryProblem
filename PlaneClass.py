from CircleClass import Circle
from WideAngleClass import WideAngle

from collections import deque


class Plane:
    def __init__(self, center_x, center_y, scale=1):
        self.scale = round(scale)
        self.dots = deque()
        self.circles = list()
        self.angles = list()
        self.my_circle = None
        self.my_angle = None
        self.center = (center_x, center_y)
        # self.circles.append(Circle(70, 40, 100, -40))
        # self.angles.append(WideAngle(1, 1, 20, 20, 10, 10))

    def clear(self):
        self.circles.clear()
        self.angles.clear()
        self.my_circle = None
        self.my_angle = None

    def add(self, obj):
        try:
            if obj.type == "Circle":
                self.circles.append(obj)
            elif obj.type == "Angle":
                self.angles.append(obj)
        except:
            self.dots.append(obj)

    def addFromFile(self, fname):
        txt = open(fname, mode="r")
        str = txt.readlines()
        for s in str:
            points = extractNumbers(s)
            if len(points) == 4:
                self.circles.append(Circle(points[0], points[1], points[2], points[3]))
            else:
                self.angles.append(
                    WideAngle(points[0], points[1], points[2], points[3], points[4], points[5]))
        txt.close()

    def calculateCross(self):
        self.my_angle = WideAngle(20, 20, 20, -15, 50, 50)
        self.my_circle = Circle(-10, -10, 30, 30)
        return 100


def extractNumbers(str):
    points = list()
    x = ""
    for i in range(len(str)):
        if str[i].isdigit():
            x += str[i]
        elif x != "":
            points.append(int(x))
            x = ""
    if x != "":
        points.append(int(x))
    return points
