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

        # Create an Combo Box
        self.my_combo = Qtw.QComboBox(self,
                                      editable=True,
                                      insertPolicy=Qtw.QComboBox.InsertAtTop)
        # Add Items to Combo Box
        self.my_combo.addItem("Pepperoni", "Something")
        self.my_combo.addItem("Cheese", 2)
        self.my_combo.addItem("Mushrooms", Qtw.QWidget)
        self.my_combo.addItem("Peppers")
        self.my_combo.addItems(["One", "Two", "Three"])
        self.my_combo.insertItem(2, "Third Item")
        self.my_combo.insertItems(2, ["One", "Two", "Three"])
        # Put combo box on screen
        self.layout().addWidget(self.my_combo)

        # Create a Button
        self.my_button = Qtw.QPushButton("Click Me!", clicked=lambda: self.press_it())
        self.layout().addWidget(self.my_button)

        # Show the App
        self.show()

    def press_it(self):
        # Add Name to Label
        self.my_label.setText(f'You Picked {self.my_combo.currentText()}!')
        # self.my_label.setText(f'You Picked {self.my_combo.currentData()}!')
        # self.my_label.setText(f'You Picked {self.my_combo.currentIndex()}!')


app = Qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()
