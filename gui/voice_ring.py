from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QRadialGradient
)
from PySide6.QtCore import Qt, QTimer

class VoiceRing(QWidget):

    def __init__(self):
    
        super().__init__()

        self.setMinimumSize(300, 300)

        self.radius = 80

        self.growing = True
        
        self.angle = 0

        self.timer = QTimer()

        self.timer.timeout.connect(self.animate)

        self.timer.start(30)

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        center_x = self.width() / 2
        center_y = self.height() / 2

        radius = self.radius
        
        gradient = QRadialGradient(center_x, center_y, radius + 35)

        gradient.setColorAt(0, QColor(0,217,255,80))
        gradient.setColorAt(1, QColor(0,217,255,0))
        
        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(
            int(center_x-radius-35),
            int(center_y-radius-35),
            (radius+35)*2,
            (radius+35)*2
        )

        pen = QPen(QColor("#00D9FF"))

        pen.setWidth(8)

        painter.setPen(pen)

        painter.setBrush(Qt.NoBrush)

        painter.drawEllipse(
            int(center_x-radius),
            int(center_y-radius),
            radius*2,
            radius*2
        )
        
        arc_pen = QPen(QColor("#66F2FF"))
        arc_pen.setWidth(8)

        painter.setPen(arc_pen)

        arc_radius = radius + 12

        painter.drawArc(
            int(center_x - arc_radius),
            int(center_y - arc_radius),
            int(arc_radius * 2),
            int(arc_radius * 2),
            -self.angle * 16,
            -70 * 16
        )

        painter.setPen(Qt.NoPen)

        painter.setBrush(QColor("#00D9FF"))

        painter.drawEllipse(
            int(center_x-12),
            int(center_y-12),
            30,
            30
        )
        
    def animate(self):
    
        if self.growing:

            self.radius += 0.5

            if self.radius >= 90:
    
                self.growing = False

        else:

            self.radius -= 0.5

            if self.radius <= 80:

                self.growing = True
                
        self.angle += 4

        if self.angle >= 360:
            self.angle = 0

        self.update()