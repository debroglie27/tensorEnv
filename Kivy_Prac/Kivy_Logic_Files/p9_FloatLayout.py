# import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.floatlayout import FloatLayout

Builder.load_file('../Kivy_Design_Files/floatlayout.kv')


# Main Grid
class MyLayout(Widget):
    pass


class AwesomeApp(App):

    def build(self):
        # Second way to change the background of our App
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
