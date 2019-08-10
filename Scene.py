import pyglet
from pyglet.window import key
from DialogHandler import DialogHandler
from Ship import Ship
from Vec2 import Vec2

class Scene:
    current = 0
    handlers_configured = False

    def __init__(self, window):
        self.id = 404
        self.first_run = True
        self.image = pyglet.resource.image('kitten_chasing_small.png')
        pass

    def start(self, window):
        self.first_run = False
        pass

    def draw(self, window):
        if(self.first_run):
            self.start(window)

    def key_press(self, symbol, modifiers):
        if(symbol == key.A):
            print('A')
            pass
        elif(symbol == key.D):
            print('D')
            pass

class IntroScene(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self.id = 0

        # Dialog
        self.dialog = ['Hello world', 'Welcome!', "This is my very first...", "...python/pyglet application", "Enjoy! :D"]
        self.label = pyglet.text.Label('Hello world', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
        self.dialog = DialogHandler(self.dialog, self.label)

        # Image
        self.image = pyglet.resource.image('kitten_chasing_small.png')
        self.music = pyglet.resource.media('Viking_Ship.wav')
        # canon = pyglet.resource.media('canon.wav', streaming = false) # streaming = false For gunshots and etc

    def change_scene(self):
        Scene.current = 1
        
    def start(self, window):
        Scene.start(self, window)
        
        #if(not Scene.handlers_configured):
        #    self.setup_handlers(window)

        self.dialog.callback = self.change_scene
        self.dialog.start_dialog()
        self.music.play()

    def draw(self, window):
        Scene.draw(self, window)

        window.clear()
        self.dialog.label.draw()
        self.image.blit(0, 0)
        
        pass

    def key_press(self, symbol, modifiers):
        if(symbol == key.A):
            print('A')
            pass
        elif(symbol == key.D):
            print('D')
            pass
        elif(symbol == key.ENTER):
            pyglet.app.exit()
        pass

    def setup_handlers(self, window, remove = False):
        if(not remove):
            window.push_handlers(on_key_press=self.key_press, on_draw=self.draw) 
            Scene.handlers_configured = True
        else:
            window.remove_handlers(on_key_press=self.key_press, on_draw=self.draw) 
            Scene.handlers_configured = False


class TestShipScene():

        def __init__(self, window):
            Scene.__init__(self, window)
            self.id = 1
            # Ship/Player
            self.player = Ship()

        def start(self, window):
            Scene.start(self, window)
            self.player.velocity = Vec2(0,3)
    
        def draw(self, window):
            Scene.draw(self, window)
    
            window.clear()
            self.player.move()
            self.player.draw()
            pass
    
        def key_press(self, symbol, modifiers):
            if(symbol == key.A):
                self.player.steer(10)
                print('A')
            elif(symbol == key.D):
                self.player.steer(-10)
                print('D')
                pass
            elif(symbol == key.ENTER):
                pyglet.app.exit()

        def key_release(self):
            pass

        def setup_handlers(self, window, remove = False):
            if(not remove):
                window.push_handlers(on_key_press=self.key_press, on_draw=self.draw) 
                Scene.handlers_configured = True
            else:
                window.remove_handlers(on_key_press=self.key_press, on_draw=self.draw) 
                Scene.handlers_configured = False





# def start_game():
#     def on_key_press(symbol, modifiers):
#         print 'Key pressed in game'
#         return True

#     def on_mouse_press(x, y, button, modifiers):
#         print 'Mouse button pressed in game'
#         return True

#     window.push_handlers(on_key_press, on_mouse_press)

# def end_game():
#     window.pop_handlers()