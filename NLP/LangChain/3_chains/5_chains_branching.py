import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        # Create a QCheckBox widget
        widget = QCheckBox("This is a checkbox")
        
        # Set the checkbox to be checked by default
        widget.setCheckState(Qt.Checked)
        
        # For tristate option: widget.setCheckState(Qt.PartiallyChecked)
        widget.setTristate(True)
        
        # Connect stateChanged signal to the show_state method
        widget.stateChanged.connect(self.show_state)
        
        # Set the widget as the central widget
        self.setCentralWidget(widget)

    def show_state(self, s):
        # Print whether the checkbox is checked
        if s == Qt.Checked:
            print("Checked")
        elif s == Qt.Unchecked:
            print("Unchecked")
        elif s == Qt.PartiallyChecked:
            print("Partially Checked")
        
        # Print the raw state value
        print(s)

# Create the application and window
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

