# import kivy
from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('../Kivy_Design_Files/new.kv')


# Main Grid
class MainGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    colour = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        colour = self.colour.text

        # print(f'Hello {name}, you like {pizza} pizza and your favourite color is {color}')
        # self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza and your favourite color is {color}'))
        print(f'Hello {name}, you like {pizza} pizza and your favourite color is {colour}')

        # Remove the stuff written on TextInput
        self.name.text = ""
        self.pizza.text = ""
        self.colour.text = ""


class AwesomeApp(App):

    def build(self):
        return MainGridLayout()


if __name__ == '__main__':
    AwesomeApp().run()
