from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPixmap
from card_ui import Ui_Form

class CardWidget(QWidget, Ui_Form):
    def __init__(self, card_picture, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.cardImage.setPixmap(card_picture)
