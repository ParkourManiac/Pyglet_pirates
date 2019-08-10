import pyglet
from pyglet.window import key
from DialogHandler import DialogHandler
from Scene import Scene, IntroScene, TestShipScene
                
# TODO: Continue adding handlers inside the scenes

window = pyglet.window.Window()
pyglet.resource.path = ['res/image', 'res/audio', 'res']
pyglet.resource.reindex()

intro_scene = IntroScene(window)
test_ship_scene = TestShipScene(window)

@window.event
def on_draw():
    if(Scene.current == intro_scene.id): # Intro
        intro_scene.draw(window)
    if(Scene.current == test_ship_scene.id): # TestShip
        test_ship_scene.draw(window)
    pass

@window.event
def on_key_press(symbol, modifiers):
    if(Scene.current == intro_scene.id): # Intro
        intro_scene.key_press(symbol, modifiers)
    elif(Scene.current == test_ship_scene.id): # TestShip
        test_ship_scene.key_press(symbol, modifiers)
    pass

pyglet.app.run()
