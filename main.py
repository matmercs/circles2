import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
import random
from circles import Ui_Circles


class Circles(QWidget, Ui_Circles):
    def __init__(self):
        super(Circles, self).__init__()
        self.setupUi(self)
        self.qp = QPainter()
        self.draw = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.repaint()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        else:
            self.draw = True

    def draw_circle(self, qp):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        size = random.randint(5, 200)
        qp.drawEllipse(240, 100, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())