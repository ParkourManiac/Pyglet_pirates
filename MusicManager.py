import pyglet

class MusicManager:
    @staticmethod
    def setup():
        MusicManager.music = {"Viking_Ship": pyglet.resource.media("Viking_Ship.wav"),
                             "Pirate_Dance": pyglet.resource.media("Pirate_Dance.wav"),
                              "Dreams_of_a_Child": pyglet.resource.media("Dreams_of_a_Child.wav"),
                              "The_Dark_Castle": pyglet.resource.media("The_Dark_Castle.wav")
                              } # TODO: Make sure to update manually

    @staticmethod
    def start(music_track):
        if(MusicManager.music[music_track] is not None):
            MusicManager.music[music_track].play()
            

    @staticmethod
    def stop(music_track):
        pass