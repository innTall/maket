from time import time
from kivy.app import App
from os.path import dirname, join
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen

class ShowcaseScreen(Screen):
  pass
  
class MaketApp(App):
  def build(self):
    self.title = 'maket'
    
if __name__ == '__main__':
  MaketApp().run()