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
        my_label = Qtw.QLabel("What's Your Name?")
        # Change Font of Label
        my_label.setFont(Qtg.QFont("Helvetica", 18))
        self.layout().addWidget(my_label)

        # Create an Entry Box
        my_entry = Qtw.QLineEdit()
        # Set the name of the Entry Box
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # Create a Button
        my_button = Qtw.QPushButton("Click Me!", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the App
        self.show()

        def press_it():
            # Add Name to Label
            my_label.setText(f'Hello {my_entry.text()}!')
            # Clear the Entry Box
            my_entry.setText("")


app = Qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()
