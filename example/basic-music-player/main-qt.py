import sys
import sounddevice as sd
import soundfile as sf
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the audio file and stream
        self.file_path = None
        self.data = None
        self.samplerate = None

        # Create a vertical layout
        self.layout = QVBoxLayout()

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
        self.setGeometry(100, 100, 300, 150)

    def load_file(self):
        # Open a file dialog to select an audio file
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav *.flac *.mp3)")
        if self.file_path:
            self.data, self.samplerate = sf.read(self.file_path)

    def play_audio(self):
        if self.data is not None:
            sd.play(self.data, self.samplerate)

    def stop_audio(self):
        sd.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec_())