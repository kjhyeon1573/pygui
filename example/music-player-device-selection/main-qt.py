#!/usr/bin/env python3

# Import the necessary modules
import sys                  # For system-specific parameters and functions
import sounddevice as sd    # For playing audio
import soundfile as sf      # For reading audio files
import logging              # For logging messages
# Import the necessary PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QComboBox, QLabel, QLineEdit, QHBoxLayout
from PyQt5.QtCore import QTimer

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the audio file and stream
        self.file_path = None
        self.data = None
        self.samplerate = None
        self.device_id = None
        self.devices = []

        # Create a vertical layout
        self.layout = QVBoxLayout()

        # Create a label for the device selection
        self.device_label = QLabel("Select Audio Output Device:", self)
        self.layout.addWidget(self.device_label)

        # Create a combo box for device selection
        self.device_combo = QComboBox(self)
        self.update_device_list()
        self.device_combo.currentIndexChanged.connect(self.select_device)
        self.layout.addWidget(self.device_combo)

        # Create a horizontal layout for the check period input
        self.period_layout = QHBoxLayout()
        self.layout.addLayout(self.period_layout)

        # Create a label and input for the check period
        self.period_label = QLabel("Check Period (ms):", self)
        self.period_layout.addWidget(self.period_label)

        self.period_input = QLineEdit(self)
        self.period_input.setText("5000")  # Default period is 5000ms (5 seconds)
        self.period_layout.addWidget(self.period_input)

        # Create a button to load the audio file
        self.load_button = QPushButton("Load Audio File", self)
        self.load_button.clicked.connect(self.load_file)
        self.layout.addWidget(self.load_button)

        # Create a button to play the audio
        self.play_button = QPushButton("Play", self)
        self.play_button.clicked.connect(self.play_audio)
        self.layout.addWidget(self.play_button)

        # Create a button to stop the audio
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_audio)
        self.layout.addWidget(self.stop_button)

        # Set the layout to the main window
        self.setLayout(self.layout)

        # Set window properties
        self.setWindowTitle("Basic Music Player")
        self.setGeometry(100, 100, 300, 250)

        # Set up a timer to periodically update the device list
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_for_device_changes)
        self.set_check_period()
        self.timer.start()

    def set_check_period(self):
        # Set the timer interval based on the input
        try:
            period = int(self.period_input.text())
            self.timer.setInterval(period)
            logging.debug(f"Check period set to {period} ms")
        except ValueError:
            self.timer.setInterval(5000)  # Default to 5000ms if input is invalid
            logging.warning("Invalid input for check period. Defaulting to 5000 ms")

    def update_device_list(self):
        # Reinitialize sounddevice to refresh the device list
        sd._terminate()
        sd._initialize()
        self.devices = sd.query_devices()
        self.device_combo.clear()
        logging.debug("Updating device list")
        for i, device in enumerate(self.devices):
            if device['max_output_channels'] > 0:  # Include only output devices
                logging.debug(f"Adding device: {device['name']} ({device['hostapi']})")
                self.device_combo.addItem(f"{device['name']} ({device['hostapi']})", i)
        self.device_combo.setCurrentIndex(sd.default.device[1])  # Set default output device

    def check_for_device_changes(self):
        # Reinitialize sounddevice to refresh the device list
        sd._terminate()
        sd._initialize()
        current_devices = sd.query_devices()
        if len(current_devices) != len(self.devices):
            logging.info("Device list length changed. Updating device list.")
            self.update_device_list()
        else:
            for i in range(len(current_devices)):
                if (current_devices[i]['name'] != self.devices[i]['name'] or
                    current_devices[i]['hostapi'] != self.devices[i]['hostapi']):
                    logging.info("Device list content changed. Updating device list.")
                    self.update_device_list()
                    break
            else:
                logging.debug("Device list has not changed")

    def select_device(self, index):
        self.device_id = self.device_combo.currentData()
        logging.debug(f"Selected device ID: {self.device_id}")

    def load_file(self):
        # Open a file dialog to select an audio file
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav *.flac *.mp3)")
        if self.file_path:
            self.data, self.samplerate = sf.read(self.file_path)
            logging.debug(f"Loaded file: {self.file_path}")

    def play_audio(self):
        if self.data is not None:
            sd.play(self.data, self.samplerate, device=self.device_id)
            logging.debug("Playing audio")

    def stop_audio(self):
        sd.stop()
        logging.debug("Stopped audio")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec_())