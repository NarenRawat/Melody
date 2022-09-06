from os import path
import json

from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder


class Root(ScreenManager):

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        Clock.schedule_once(self.add_screens)

    def add_screens(self, delta):
        with open(path.join("json", "root_screens.json")) as file:
            screens = json.load(file)

        for screen_name in screens.keys():
            screen_details = screens[screen_name]
            Builder.load_file(screen_details["kv"])
            exec(screen_details["import"])
            screen_object = eval(screen_details["object"])
            screen_object.name = screen_name
            self.add_widget(screen_object)
