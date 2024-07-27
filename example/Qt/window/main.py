import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

# Create the application object
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("My First Window")
window.setGeometry(100, 100, 400, 300)

# Create a layout
layout = QVBoxLayout()

# Add a label
label = QLabel("Hello, World!")
layout.addWidget(label)

# Add a button to close the window
button = QPushButton("Close")
button.clicked.connect(window.close)
layout.addWidget(button)

# Set the layout to the main window
window.setLayout(layout)

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())