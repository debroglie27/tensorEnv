# import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('../Kivy_Design_Files/update_label.kv')


# Main Grid
class MyLayout(Widget):

    def press(self):
        # Create a variable
        name = self.ids.name_input.text

        # Update the Label
        self.ids.name_label.text = f"Hello {name}!"

        # Clear the TextInput Box
        self.ids.name_input.text = ""

class AwesomeApp(App):

    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
