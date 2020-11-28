# import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# Set the App Size
Window.size = (400, 520)

Builder.load_file('./Calc.kv')


class MyLayout(Widget):

    def clear(self):
        self.ids.calc_input.text = '0'


class CalculatorApp(App):

    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
