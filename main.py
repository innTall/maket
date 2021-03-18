from time import time
from kivy.app import App
from os.path import dirname, join
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

class BoxLayout(BoxLayout):
  pass
class MaketApp(App):
  def build(self):
    return BoxLayout()

if __name__ == '__main__':
  app = MaketApp()
  app.run()
