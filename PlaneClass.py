from CircleClass import Circle
from WideAngleClass import WideAngle


class Plane:
    def __init__(self, center_x, center_y, scale=1):
        self.scale = round(scale)
        self.circles = list()
        self.angles = list()
        self.center = (center_x, center_y)
        self.circles.append(Circle(70, 40, 100, -40))
        self.angles.append(WideAngle(1, 1, 20, 20, 10, 10))

    def clear(self):
        self.circles.clear()
        self.angles.clear()

    def add(self, obj):
        if obj.type == "Circle":
            pass
        elif obj.type == "Angle":
            pass
        else:
            pass
