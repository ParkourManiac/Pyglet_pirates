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
def fps(): 
    fps_display.draw()
window.push_handlers(on_draw=fps) 

SceneManager.setup(window, keys, "IntroScene")
SceneManager.start()

if __name__ == "__main__":
    pyglet.app.run()

    # Ljudet avstängt i volymkontrollen