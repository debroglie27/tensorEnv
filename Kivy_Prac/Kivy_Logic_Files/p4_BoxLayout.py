# import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('../Kivy_Design_Files/boxlayout.kv')


# Main Grid
class MyLayout(Widget):
    pass


class AwesomeApp(App):

    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
