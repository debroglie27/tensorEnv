import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg


class MainWindow(Qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a Title
        self.setWindowTitle("ComboBox")

        # Set a Layout
        self.setLayout(Qtw.QVBoxLayout())

        # Create Label
        self.my_label = Qtw.QLabel("Pick Something from the List Below")
        # Change Font of Label
        self.my_label.setFont(Qtg.QFont("Helvetica", 24))
        self.layout().addWidget(self.my_label)

        # Create an Spin Box
        # Use Qtw.DoubleSpinBox for decimal values
        self.my_spin = Qtw.QSpinBox(self,
                                    value=10,
                                    maximum=100,
                                    minimum=0,
                                    singleStep=5,
                                    prefix="#",
                                    suffix=" Order")
        # Change Font of Spin Box
        self.my_spin.setFont(Qtg.QFont("Helvetica", 18))
        # Put spin box on screen
        self.layout().addWidget(self.my_spin)

        # Create a Button
        self.my_button = Qtw.QPushButton("Click Me!", clicked=lambda: self.press_it())
        self.layout().addWidget(self.my_button)

        # Show the App
        self.show()

    def press_it(self):
        # Add Name to Label
        self.my_label.setText(f'You Picked #{self.my_spin.value()} Order!')


app = Qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()
