from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QConicalGradient, QPen
from PyQt5.QtCore import Qt, QRectF

class DialIndicator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0  # Current value

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Define indicator colors
        green_color = QColor(0, 255, 0)
        yellow_color = QColor(255, 255, 0)
        red_color = QColor(255, 0, 0)

        # Define gradient
        gradient = QConicalGradient(self.width() / 2, self.height() / 2, 0)
        gradient.setColorAt(0.0, green_color)
        gradient.setColorAt(0.5, yellow_color)
        gradient.setColorAt(1.0, red_color)

        # Define dial parameters
        outer_radius = min(self.width(), self.height()) / 2
        inner_radius = outer_radius * 0.7
        start_angle = 45
        span_angle = 270
        value_angle = start_angle + (span_angle * self.value / 100)

        # Draw dial indicator
        rect = QRectF(0, 0, self.width(), self.height())
        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawPie(rect, start_angle * 16, span_angle * 16)

        # Draw indicator needle
        pen = QPen(Qt.white)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(self.width() / 2, self.height() / 2, outer_radius * 0.9, self.height() / 2)
        painter.drawLine(self.width() / 2, self.height() / 2, inner_radius, self.height() / 2)
        painter.drawLine(self.width() / 2, self.height() / 2, outer_radius * 0.9, self.height() / 2 + 5)

        # Draw value text
        value_font = painter.font()
        value_font.setPointSize(20)
        painter.setFont(value_font)
        painter.drawText(rect, Qt.AlignCenter, str(self.value))

    def set_value(self, value):
        self.value = value
        self.update()

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    window.setLayout(layout)

    dial_indicator = DialIndicator()
    layout.addWidget(dial_indicator)

    # Set value
    dial_indicator.set_value(75)

    window.show()
    app.exec()
