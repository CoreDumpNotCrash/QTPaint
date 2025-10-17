"""main.py this for intializing and running project"""

from core import logger, config
from PyQt6.QtWidgets import QApplication, QMainWindow

from modules.draw import draw
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTPaint")
        self.setGeometry(200, 200, 800, 600)

        self.canvas = draw.PaintWidget()
        self.setCentralWidget(self.canvas)

def main():
    logger.log(f"Starting {config.APP_NAME} v{config.APP_VERSION}")
    
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

    logger.log(f"Finishing {config.APP_NAME} v{config.APP_VERSION}")

if __name__ == "__main__":
    main()