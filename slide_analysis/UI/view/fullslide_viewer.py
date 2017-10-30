from PyQt5.QtCore import Qt, QRectF, QEvent, QTimer
from PyQt5.QtGui import QPixmap, QResizeEvent, QMouseEvent, QCursor
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QFrame, QGraphicsPixmapItem

from slide_analysis.UI.view import ImageHelper


class FullslideViewer(QGraphicsView):
    def __init__(self, parent):
        super(FullslideViewer, self).__init__(parent)
        self._zoom = 0
        self.image_helper = None
        self._scene = QGraphicsScene(self)
        self._photo = QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameShape(QFrame.NoFrame)

    # def resizeEvent(self, event: QResizeEvent):
    #     self.fitInView()
    #
    # def get_scene(self):
    #     return self._scene

    # def mouseMoveEvent(self, event):
    #     width, height = self.width(), self.height()
    #     event_x, event_y = event.x(), event.y()
    #
    #     if event_y < 0 or event_y > height or \
    #                     event_x < 0 or event_x > width:
    #         # Mouse cursor has left the widget. Wrap the mouse.
    #         global_pos = self.mapToGlobal(event.pos())
    #         if event_y < 0 or event_y > height:
    #             # Cursor left on the y axis. Move cursor to the
    #             # opposite side.
    #             global_pos.setY(global_pos.y() +
    #                             (height if event_y < 0 else -height))
    #         else:
    #             # Cursor left on the x axis. Move cursor to the
    #             # opposite side.
    #             global_pos.setX(global_pos.x() +
    #                             (width if event_x < 0 else -width))
    #
    #         # For the scroll hand dragging to work with mouse wrapping
    #         # we have to emulate a mouse release, move the cursor and
    #         # then emulate a mouse press. Not doing this causes the
    #         # scroll hand drag to stop after the cursor has moved.
    #         r_event = QMouseEvent(QEvent.MouseButtonRelease,
    #                               self.mapFromGlobal(QCursor.pos()),
    #                               Qt.LeftButton,
    #                               Qt.NoButton,
    #                               Qt.NoModifier)
    #         self.mouseReleaseEvent(r_event)
    #         QCursor.setPos(global_pos)
    #         p_event = QMouseEvent(QEvent.MouseButtonPress,
    #                               self.mapFromGlobal(QCursor.pos()),
    #                               Qt.LeftButton,
    #                               Qt.LeftButton,
    #                               Qt.NoModifier)
    #         QTimer.singleShot(0, lambda: self.mousePressEvent(p_event))
    #     else:
    #         QGraphicsView.mouseMoveEvent(self, event)

    def fitInView(self, **kwargs):
        rect = QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            unity = self.transform().mapRect(QRectF(0, 0, 1, 1))
            # self.scale(1 / unity.width(), 1 / unity.height())
            viewrect = self.viewport().rect()
            scenerect = self.transform().mapRect(rect)
            factor = min(viewrect.width() / scenerect.width(),
                         viewrect.height() / scenerect.height())
            # if factor <= 0.8:
            #     self.move_to_next_image_level()
            self.scale(factor, factor)
            self.centerOn(rect.center())
            self._zoom = 0

    # def move_to_next_image_level(self):
    #     pixmap = QPixmap.fromImage(self.image_helper.zoom_in())
    #     if pixmap and not pixmap.isNull():
    #         self.setDragMode(QGraphicsView.ScrollHandDrag)
    #         # self._photo =  QGraphicsPixmapItem()
    #         self._photo.setPixmap(pixmap)
    #         # self._scene.addItem(self._photo)
    #         # self._scene.addPixmap(pixmap)
    #         self.fitInView()
    #     else:
    #         self.setDragMode(QGraphicsView.NoDrag)
    #         self._photo.setPixmap(QPixmap())

    def set_image(self, filepath):
        self._zoom = 0
        # self._scene.clear()
        self.image_helper = ImageHelper(filepath)
        viewrect = [self.viewport().rect().width(), self.viewport().rect().height()]
        pixmap = QPixmap.fromImage(self.image_helper.get_q_image(viewrect))
        if pixmap and not pixmap.isNull():
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            # self._photo =  QGraphicsPixmapItem()
            self._photo.setPixmap(pixmap)
            # self._scene.addItem(self._photo)
            # self._scene.addPixmap(pixmap)
            self.fitInView()
        else:
            self.setDragMode(QGraphicsView.NoDrag)
            self._photo.setPixmap(QPixmap())

    def zoomFactor(self):
        return self._zoom

    def wheelEvent(self, event):
        if not self._photo.pixmap().isNull():
            if event.pixelDelta().y() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                print(self.mapToScene(self.viewport().rect()).boundingRect())
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0
