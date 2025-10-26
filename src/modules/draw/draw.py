"""draw.py is a module what handles painting & erasing"""

from core import config, logger
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QPixmap
from PyQt6.QtCore import Qt, QPoint

def make_pen(erase_mode, brush_size = config.DEFAULT_BRUSH_SIZE):
    """A function what returns out pen"""
    logger.log("making pen")

    color = Qt.GlobalColor.white if erase_mode else Qt.GlobalColor.black
    pen = QPen(color, brush_size, Qt.PenStyle.SolidLine)

    logger.log("done!")
    return pen

class PaintWidget(QWidget):
    """Our main custom widget where you can do drawing"""
    def __init__(self, parent = None):
        logger.log("intializing a Paint Widget")
        super().__init__(parent)
        self._canvas = QPixmap(self.size())
        self._canvas.fill(Qt.GlobalColor.white)
        self._drawing = False
        self._erase_mode = False
        self._last_point = QPoint()
        self._brush_size = config.DEFAULT_BRUSH_SIZE

        logger.log("done!")
    
    def mousePressEvent(self, event):
        """Mouse event listener is a method what listens to mouse activity"""
        logger.log("Listening to mouse . . .")

        btn = event.button()
        match btn:
            case Qt.MouseButton.LeftButton:
                logger.log("M1 pressed!")
                self._brush_size = config.DEFAULT_BRUSH_SIZE
                self._drawing = True
                self._erase_mode = False
                self._last_point = event.position().toPoint()
            case Qt.MouseButton.RightButton:
                logger.log("M2 pressed!")
                self._brush_size = config.DEFAULT_BRUSH_SIZE + 15
                self._drawing = True
                self._drawing = True
                self._erase_mode = True
                self._last_point = event.position().toPoint()
            case _:
                super().mousePressEvent(event)
        logger.log("Done!")

    def mouseMoveEvent(self, event):
        """event when mouse will draw"""
        logger.log("Drawing . . .")
        if not self._drawing:
            logger.log("drawing mode is off!")
            super().mouseMoveEvent(event)
        
        painter = QPainter(self._canvas)
        pen = make_pen(self._erase_mode, self._brush_size)
        painter.setPen(pen)
        
        current_point = event.position().toPoint()
        painter.drawLine(self._last_point, current_point)

        self._last_point = current_point

        self.update()
        logger.log("Done!")
    def mouseReleaseEvent(self, event):
        """Event when left or right button will be released"""
        logger.log("Mouse released!")
        btn = event.button()
        if btn in (Qt.MouseButton.LeftButton, Qt.MouseButton.RightButton):
            self._drawing = False
        else:
            super().mouseReleaseEvent(event)

    def paintEvent(self, event):
        """Paint method"""
        logger.log("Painting . . .")
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self._canvas)
        logger.log("Done!")
    def resizeEvent(self, event):
        """Event if window will resized"""
        logger.log("Window resized!")
        new_size = event.size()
        new_cavase = QPixmap(new_size)
        new_cavase.fill(Qt.GlobalColor.white)

        painter = QPainter(new_cavase)
        painter.drawPixmap(0,0,self._canvas)
        self._canvas = new_cavase