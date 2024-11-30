import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap
from card import CardWidget
from main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.center_layout = QVBoxLayout()
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.center_layout.addItem(spacer)
        self.centralwidget.setLayout(self.center_layout)

        card1 = CardWidget(QPixmap('assets/blue/1_blue.png'))
        card2 = CardWidget(QPixmap('assets/blue/2_blue.png'))
        card3 = CardWidget(QPixmap('assets/blue/3_blue.png'))

        self.playerCardLayout.addWidget(card1.widget())
        self.playerCardLayout.addWidget(card2.widget())
        self.playerCardLayout.addWidget(card3.widget())

        self.playerCardLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.playerCardLayout.setContentsMargins(0, 0, 0, 0)

        self.center_layout.addLayout(self.playerCardLayout)
        self.center_layout.setStretch(0, 1)
        self.center_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())