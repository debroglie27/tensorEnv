import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg


class MainWindow(Qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a Title
        self.setWindowTitle("Hello World!")

        # Set a Layout
        self.setLayout(Qtw.QVBoxLayout())

        # Create Label
        self.my_label = Qtw.QLabel("What's Your Name?")
        # Change Font of Label
        self.my_label.setFont(Qtg.QFont("Helvetica", 18))
        self.layout().addWidget(self.my_label)

        # Create an Entry Box
        self.my_entry = Qtw.QLineEdit()
        # Set the name of the Entry Box
        self.my_entry.setObjectName("name_field")
        self.my_entry.setText("")
        self.layout().addWidget(self.my_entry)

        # Create a Button
        self.my_button = Qtw.QPushButton("Click Me!", clicked=lambda: self.press_it())
        self.layout().addWidget(self.my_button)

        # Show the App
        self.show()

    def press_it(self):
        # Add Name to Label
        self.my_label.setText(f'Hello {self.my_entry.text()}!')
        # Clear the Entry Box
        self.my_entry.setText("")


app = Qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()
