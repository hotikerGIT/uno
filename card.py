from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel

class CardWidget(QWidget):
    def __init__(self, card_picture, size=None, parent=None):
        super().__init__(parent)

        if size is None:
            size = [300, 200]

        picture = QPixmap(card_picture)
        picture = picture.scaled(*size, Qt.AspectRatioMode.KeepAspectRatio)

        self.cardImage = QLabel(self)
        self.cardImage.setPixmap(picture)
        self.cardImage.resize(card_picture.size())

    def widget(self):
        return self.cardImage
