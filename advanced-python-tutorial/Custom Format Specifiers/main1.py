import math


class Coordinate2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x = {self.x}, y = {self.y}"

    def __format__(self, format_spec):
        if format_spec == "polar":
            r = math.sqrt(self.x**2 + self.y**2)
            theta = math.atan2(self.y, self.x)
            return f"r = {r:.2f}, theta = {theta:.2f}"
        return f"x = {self.x}, y = {self.y}"


coord2d = Coordinate2D(20, 15)
print(coord2d)
print(f"{coord2d:polar}")
print(format(coord2d, "polar"))
