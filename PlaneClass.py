class Plane:
    def __init__(self):
        self.circles = list()
        self.lines = list()

    def clear(self):
        self.circles.clear()
        self.lines.clear()

    def add(self, obj):
        if obj.type == "Circle":
            pass
        elif obj.type == "Angle":
            pass
        else:
            pass
