import pyglet
import glob

class MusicManager:
    @staticmethod
    def setup():
        MusicManager.music = {"Viking_Ship": pyglet.resource.media("Viking_Ship.wav"),
                                "Pirate_Dance": pyglet.resource.media("Pirate_Dance.wav"),
                                "Dreams_of_a_Child": pyglet.resource.media("Dreams_of_a_Child.wav"),
                                "The_Dark_Castle": pyglet.resource.media("The_Dark_Castle.wav")
                              } # TODO: Make sure to update manually
        MusicManager.music_player = pyglet.media.Player()

    # @staticmethod
    # def read_songs(path, file_type):
    #     MusicManager.music = {}
    #     long_paths = glob.glob(path + "*" + file_type)
    #     file_names = []
    #     for long_path in long_paths:
    #         file_names.append(long_path.replace(path, ""))
    #     for file_name in file_names:
    #         name = file_name.replace(file_type, "")
    #         MusicManager.music[name] = pyglet.resource.media(file_name)
    #     print(MusicManager.music)

    @staticmethod
    def start(music_track):
        MusicManager.music_player.play()

    @staticmethod
    def queue(music_track):
        MusicManager.music_player.queue(MusicManager.music[music_track])
            

    @staticmethod
    def stop(music_track):
        MusicManager.music_player.pause()