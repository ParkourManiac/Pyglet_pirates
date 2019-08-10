import pyglet
from Vec2 import Vec2
from GameObject import GameObject

class Ship:
    def __init__(self, hp = 10, game_object = GameObject(), image = 0):
        self.hp = hp
        self.velocity = Vec2()
        self.go = game_object
        if(image == 0):
            self.ship = pyglet.resource.image('Ship.png')
        else:
            self.ship = image
        pass

    def move(self):
        self.go.position += self.velocity.rotated(self.go.rotation)
        pass

    def shoot(self, projectile):
        pass

    def steer(self, degree):
        self.go.rotation += degree
        pass

    def draw(self):
        self.ship.blit(self.go.position.x, self.go.position.y)
