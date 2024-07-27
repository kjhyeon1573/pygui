import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the counter
        self.counter = 0

        # Create a vertical layout
        self.layout = QVBoxLayout()

        # Create a label to display the counter
        self.label = QLabel(f"Counter: {self.counter}", self)
        self.layout.addWidget(self.label)

        # Create a horizontal layout for the buttons
        self.button_layout = QHBoxLayout()

        # Create a button to increment the counter
        self.increment_button = QPushButton("Increment", self)
        self.increment_button.clicked.connect(self.increment_counter)
        self.button_layout.addWidget(self.increment_button)

        # Create a button to decrement the counter
        self.decrement_button = QPushButton("Decrement", self)
        self.decrement_button.clicked.connect(self.decrement_counter)
        self.button_layout.addWidget(self.decrement_button)

        # Create a button to reset the counter
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.clicked.connect(self.reset_counter)
        self.button_layout.addWidget(self.reset_button)

        # Add the button layout to the main layout
        self.layout.addLayout(self.button_layout)

        # Set the layout to the main window
        self.setLayout(self.layout)

        # Set window properties
        self.setWindowTitle("Counter App")
        self.setGeometry(100, 100, 300, 150)

    def increment_counter(self):
        # Increment the counter
        self.counter += 1
        # Update the label
        self.label.setText(f"Counter: {self.counter}")

    def decrement_counter(self):
        # Decrement the counter
        self.counter -= 1
        # Update the label
        self.label.setText(f"Counter: {self.counter}")

    def reset_counter(self):
        # Reset the counter to zero
        self.counter = 0
        # Update the label
        self.label.setText(f"Counter: {self.counter}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())