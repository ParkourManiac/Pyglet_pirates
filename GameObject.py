from Vec2 import Vec2

class GameObject:
    def __init__(self, position = Vec2(0, 0), rotation = 0, scale = Vec2(1, 1)):
        self.position = position
        self.rotation = rotation
        self.scale = scale