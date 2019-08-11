import pyglet
from pyglet.window import key
from DialogHandler import DialogHandler
from Scene import SceneManager, Scene, IntroScene, TestShipScene
                
# TODO: Continue adding handlers inside the scenes

window = pyglet.window.Window()
pyglet.resource.path = ['res/image', 'res/audio', 'res']
pyglet.resource.reindex()
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Debug FPS
fps_display = pyglet.window.FPSDisplay(window)

SceneManager.setup(window, keys, "IntroScene")
SceneManager.start()
# intro_scene = IntroScene(window, keys)
# test_ship_scene = TestShipScene(window, keys)

if __name__ == "__main__":
    pyglet.app.run()

    # Ljudet avstängt i volymkontrollen