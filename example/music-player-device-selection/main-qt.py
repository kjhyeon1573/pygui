import sys
import sounddevice as sd
import soundfile as sf
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QComboBox, QLabel

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the audio file and stream
        self.file_path = None
        self.data = None
        self.samplerate = None
        self.device_id = None

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
        self.setGeometry(100, 100, 300, 200)

    def update_device_list(self):
        # Get a list of audio devices
        devices = sd.query_devices()
        self.device_combo.clear()
        for i, device in enumerate(devices):
            if device['max_output_channels'] > 0:  # Include only output devices
                self.device_combo.addItem(f"{device['name']} ({device['hostapi']})", i)
        self.device_combo.setCurrentIndex(sd.default.device[1])  # Set default output device

    def select_device(self, index):
        self.device_id = self.device_combo.currentData()

    def load_file(self):
        # Open a file dialog to select an audio file
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav *.flac *.mp3)")
        if self.file_path:
            self.data, self.samplerate = sf.read(self.file_path)

    def play_audio(self):
        if self.data is not None:
            sd.play(self.data, self.samplerate, device=self.device_id)

    def stop_audio(self):
        sd.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec_())