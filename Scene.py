import pyglet
from pyglet.window import key
from DialogHandler import DialogHandler
from Ship import Ship
from Vec2 import Vec2
from Input import Input

class SceneManager:
    @staticmethod
    def setup(current_window, key_values, scene_name):
        SceneManager.window = current_window
        SceneManager.keys = key_values
        SceneManager.scene_name = scene_name
        SceneManager.scene_object = None
        SceneManager.scenes = {"IntroScene": IntroScene, "TestShipScene": TestShipScene} # TODO: Make sure to update manually

    @staticmethod
    def start():
        if(SceneManager.scene_object is None):
            SceneManager.scene_object = SceneManager.instantiate_scene(SceneManager.scene_name)
            
        SceneManager.scene_object.start()

    @staticmethod
    def end():
        SceneManager.scene_object.end()

    @staticmethod
    def change_scene_and_start(new_scene):
        SceneManager.end()
        SceneManager.scene_name = new_scene
        SceneManager.scene_object = SceneManager.instantiate_scene(SceneManager.scene_name)
        SceneManager.scene_object.start() # Migth want to make a separate function that doesn't start the scene???

    @staticmethod
    def instantiate_scene(scene_name):
        new_scene = SceneManager.scenes[scene_name]()
        print("Instantiated scene: ", scene_name)
        print("Obj ref: ", new_scene)
        return new_scene
        

        

class Scene:
    #current_index = 0
    handlers_configured = False

    def __init__(self):
        self.id = 404
        self.first_run = True
        self.image = pyglet.resource.image('kitten_chasing_small.png')
        
        
    def start(self):
        # self.first_run = False
        # # Sets the handler for input
        # if(not Scene.handlers_configured):
        #     self.setup_handlers()
        self.setup_handlers()

    def end(self):
        self.setup_handlers(True)

    def update(self):
        pass

    def draw(self):
        pass

    # def change_scene(self, scene): #scene_index = 0):
    #     self.setup_handlers(True)
    #     #Scene.current_index = scene_index
    #     # TODO: Construct a new scene
    #     SceneManager.change_scene(scene)

    def key_press(self, symbol, modifiers):
        if(symbol == key.A):
            print('A')
        elif(symbol == key.D):
            print('D')
        elif(symbol == key.ENTER):
            SceneManager.change_scene_and_start("IntroScene")

    def key_release(self, symbol, modifiers):
        if(symbol == key.A):
            print('a')
        elif(symbol == key.D):
            print('d')

    def setup_handlers(self, remove = False): # TODO: Somethings wrong. The handlers are not removed
        if(not remove):
            SceneManager.window.push_handlers(on_key_press=self.key_press, on_key_release= self.key_release, on_draw=self.draw) 
            Scene.handlers_configured = True
        else:
            SceneManager.window.remove_handlers(on_key_press=self.key_press, on_key_release= self.key_release, on_draw=self.draw) 
            Scene.handlers_configured = False



class IntroScene(Scene):
    def __init__(self):
        Scene.__init__(self) # Base method
        self.id = 0

        # Dialog
        self.dialog = ['Hello world', 'Welcome!', "This is my very first...", "...python/pyglet application", "Enjoy! :D"]
        self.label = pyglet.text.Label('Hello world', font_name='Times New Roman', font_size=36, x=SceneManager.window.width//2, y=SceneManager.window.height//2, anchor_x='center', anchor_y='center')
        self.dialog = DialogHandler(self.dialog, self.label)

        # Loading resources
        self.music = pyglet.resource.media('Viking_Ship.wav')

    def change_scene(self):
        if(self.id == 0): # Prevents delayed callback event from triggering in the wrong scene
            #Scene.change_scene(self, 1) # Base method
            SceneManager.change_scene_and_start("TestShipScene")
            # TODO: Change so that it takes in an object of the scene to be loaded?????
        
    def start(self):
        Scene.start(self) # Base method

        # TODO: Change callback to SceneManager.change_scene("TestShipScene")
        #self.dialog.callback = self.change_scene
        self.dialog.callback = self.change_scene
        self.dialog.start_dialog()
        self.music.play()

    def end(self):
        self.dialog.remove_dialog_handler()
        Scene.end(self)

    def draw(self):
        Scene.draw(self) # Base method

        SceneManager.window.clear()
        self.dialog.label.draw()
        self.image.blit(0, 0)



class TestShipScene(Scene):
        def __init__(self):
            Scene.__init__(self)
            self.id = 1
            # Ship/Player
            self.player = Ship()

        def start(self):
            Scene.start(self)
            self.player.velocity = Vec2(0,3)
    
        def draw(self):
            Scene.draw(self)
            self.update()
            SceneManager.window.clear()
            self.player.draw()

        def update(self):
            if(SceneManager.keys[key.A]):
                self.player.steer(10)
            if(SceneManager.keys[key.D]):
                self.player.steer(-10)
            self.player.move()


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