# import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# Top Grid on top of Main Grid
class TopGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(TopGridLayout, self).__init__(**kwargs)

        # Set Columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Name: ", size_hint_x=None, height=50, size_hint_y=None, width=300))
        # Add Input Box
        self.name = TextInput(multiline=True, size_hint_x=None, height=50, size_hint_y=None, width=500)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favourite Pizza: ", size_hint_x=None, height=50, size_hint_y=None, width=300))
        # Add Input Box
        self.pizza = TextInput(multiline=False, size_hint_x=None, height=50, size_hint_y=None, width=500)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favourite Color: ", size_hint_x=None, height=50, size_hint_y=None, width=300))
        # Add Input Box
        self.color = TextInput(multiline=False, size_hint_x=None, height=50, size_hint_y=None, width=500)
        self.add_widget(self.color)


# Main Grid
class MainGridLayout(GridLayout):
    # Initialise infinite Keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MainGridLayout, self).__init__(**kwargs)

        # Set Columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 120

        # Add the top GridLayout
        self.top_grid = TopGridLayout()
        self.add_widget(self.top_grid)

        # Create a Submit Button
        self.submit = Button(text="Submit", font_size=32, size_hint_x=None, height=50, size_hint_y=None, width=200)
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.top_grid.name.text
        pizza = self.top_grid.pizza.text
        color = self.top_grid.color.text

        # print(f'Hello {name}, you like {pizza} pizza and your favourite color is {color}')
        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza and your favourite color is {color}'))

        # Remove the stuff written on TextInput
        self.top_grid.name.text = ""
        self.top_grid.pizza.text = ""
        self.top_grid.color.text = ""


class MyApp(App):

    def build(self):
        return MainGridLayout()


if __name__ == '__main__':
    MyApp().run()
