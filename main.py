import os

from kivymd.app import MDApp
from kivy.lang.builder import Builder

from libs.uix.baseclass.root import Root

KV_DIR = os.path.join("libs", "uix", "kv")

# Load all kv files
for kv_file in os.listdir(KV_DIR):
    file = os.path.join(KV_DIR, kv_file)
    if not os.path.isdir(file):
        Builder.load_file(file)


class MelodyApp(MDApp):

    def __init__(self, **kwargs):
        super(MelodyApp, self).__init__(**kwargs)
        self.title = "Melody"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "800"

    def build(self):
        return Root()

    def on_start(self):
        pass

    def on_pause(self):
        return True

    def on_stop(self):
        pass


if __name__ == "__main__":
    MelodyApp().run()
