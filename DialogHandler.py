import pyglet

class DialogHandler:
    def __init__(self, dialog, label):
        self.dialog_array = dialog
        self.dialog_index = 0
        self.label = label
        self.dialog_time = 2

    def start_dialog(self):
        self.label.text = self.dialog_array[0]
        pyglet.clock.schedule_once(self.change_dialog, self.dialog_time)

    def remove_dialog_handler(self):
        pyglet.clock.unschedule(self.change_dialog)

    def callback(self):
        pass
        
    def change_dialog(self, dt):
        self.dialog_index += 1
        if(self.dialog_index < len(self.dialog_array)):
            self.label.text = self.dialog_array[self.dialog_index]
            pyglet.clock.schedule_once(self.change_dialog, self.dialog_time)
        else:
            self.callback()