import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap
from card import CardWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        blue_one_png = QPixmap('assets/blue/1_blue.png')
        blue_one = CardWidget(blue_one_png)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())