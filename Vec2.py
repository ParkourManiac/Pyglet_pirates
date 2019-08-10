import math

class Vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def rotated(self, rotation_amount, use_radians = False):
        if(not use_radians):
            rotation = rotation_amount * 1/360 * 2*math.pi
        else:
            rotation = rotation_amount
        return Vec2(self.x * math.cos(rotation) - self.y * math.sin(rotation), self.x * math.sin(rotation) + self.y * math.cos(rotation))
