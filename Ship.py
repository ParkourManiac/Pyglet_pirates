import pyglet
from Vec2 import Vec2
from GameObject import GameObject

class Ship:
    def __init__(self, hp = 10, image = 0):
        self.hp = hp
        self.velocity = Vec2()
        self.go = GameObject()

        if(image == 0):
            self.ship_image = pyglet.resource.image('Ship.png')
        else:
            self.ship_image = image
        pass
        self.ship_image.anchor_x = self.ship_image.width // 2
        self.ship_image.anchor_y = self.ship_image.height // 2
        self.ship = pyglet.sprite.Sprite(self.ship_image)

    def move(self):
        self.go.position += self.velocity.rotated(self.go.rotation)
        pass

    def shoot(self, projectile):
        # canon = pyglet.resource.media('canon.wav', streaming = false) # streaming = false For gunshots and etc
        pass

    def steer(self, degree):
        self.go.rotation += degree
        pass

    def draw(self):
        self.ship.update(self.go.position.x, self.go.position.y, -self.go.rotation)
        self.ship.draw()
        print(self.go.position.x, self.go.position.y)
