class WideAngle:
    type = "Angle"

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # (x1, y1) и (x2, y2) задают отрезок; (x3, y3) задают сторону, в которую направлены прямые
        self.mainSegment = (x1, y1, x2, y2)
