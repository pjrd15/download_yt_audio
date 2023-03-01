import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QVBoxLayout, QTextEdit, QPushButton, QInputDialog, QComboBox)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from yt_dlp import YoutubeDL

class MainWindow(QWidget):
    # GUI function
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app
        self.init_ui()

    def init_ui(self):
        # Set the window Title and position on the screen
        self.setWindowTitle("YouTube Audio Downloader")
        self.resize(600, 300)

        # Create the field where the Links will go
        self.link_entry = QTextEdit(self, placeholderText = 'Youtube Links here separated by a comma or newline')

        # Create the dropdown menu to select format type
        self.drp_combo = QComboBox(self)
        audio_formats = ['mp3', 'm4a', 'flac']
        self.drp_combo.addItems(audio_formats)
        self.drp_combo.setFixedSize(70, 25)
        
        # Create the download button
        dwn_button = QPushButton(('\tDownload'))
        dwn_button.clicked.connect(lambda: self.download_audio())
        dwn_button.setIcon(QIcon(('download_icon.png')))
        dwn_button.setFixedSize(QSize(100, 30))
        
        # Place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(self.link_entry)
        layout.addWidget(self.drp_combo)
        layout.addWidget(dwn_button)
        self.setLayout(layout)

        # Show the window
        self.center()
        self.show()

    # Function to download the audio
    def download_audio(self):
        # Get the youtube links from the input field
        links_text = self.link_entry.toPlainText()
        links = [link.strip() for link in links_text.split('\n') + links_text.split(',')]

        # Use yt_dlp to download the audio for each link
        ydl_opts = {
            'format': 'bestaudio/best',
            'ignoreerrors': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.drp_combo.currentText(),
                'preferredquality': '192',
            }],
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            for link in links:
                # Download the audio
                ydl.download([link])
    
    def center(self):
        # Get the geometry of the main window
        qr = self.frameGeometry()
        
        # Center point of screen
        cp = self.app.primaryScreen().availableGeometry().center()
        
        # Move Rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # Top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the Main Window
    window = MainWindow(app)

    # Start the event Loop
    sys.exit(app.exec())
