import pyglet
from pyglet.window import key
import glob
from DialogHandler import DialogHandler
from Scene import SceneManager, Scene, IntroScene, TestShipScene

# TODO: Move music into the MusicManager and start the music from the intro scene using the MusicManager

window = pyglet.window.Window()
pyglet.resource.path = ['res/image', 'res/audio', 'res']
pyglet.resource.reindex()
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Debug FPS
fps_display = pyglet.window.FPSDisplay(window)
fps_display.label.font_size = 10
fps_display.anchor_x = 'left'
fps_display.anchor_x = 'top'
def fps():
    fps_display.draw()
window.push_handlers(on_draw=fps)

SceneManager.setup(window, keys, "IntroScene")
SceneManager.music_manager.read_songs('res\\audio\\', '.wav') # TODO: Change glob to pyglet function!!!
SceneManager.start()
"Test/test".strip("Test/")
if __name__ == "__main__":
    pyglet.app.run()

    # Ljudet avstängt i volymkontrollen