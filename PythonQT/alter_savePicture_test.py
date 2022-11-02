from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class GraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(GraphicsView, self).__init__(parent)
        self.setGeometry(300, 300, 250, 150)
        self.setScene(QtWidgets.QGraphicsScene(self))
        self.pixmapItem = (
            QtWidgets.QGraphicsPixmapItem()
        )  # check if everytime you open a new image the old image is still an item
        self.scene().addItem(self.pixmapItem)
        self._path_item = None

    def initial_path(self):
        self._path = QtGui.QPainterPath()
        pen = QtGui.QPen(
            QtGui.QColor("green"), 4, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap
        )
        self._path_item = self.scene().addPath(self._path, pen)

    @QtCore.pyqtSlot()
    def setImage(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "select Image", "", "Image Files (*.png *.jpg *jpg *.bmp)"
        )
        if filename:
            pixmap1 = QtGui.QPixmap(filename)
            self.pixmapItem.setPixmap(pixmap1)
            self.resize(pixmap1.width(),pixmap1.height())


    def mousePressEvent(self, event):
        start = event.pos()
        if (
            not self.pixmapItem.pixmap().isNull()
            and event.buttons() & QtCore.Qt.LeftButton
        ):
            self.initial_path()
            self._path.moveTo(self.mapToScene(start))
            self._path_item.setPath(self._path)
        super(GraphicsView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if (
            not self.pixmapItem.pixmap().isNull()
            and event.buttons() & QtCore.Qt.LeftButton
            and self._path_item is not None
        ):
            self._path.lineTo(self.mapToScene(event.pos()))
            self._path_item.setPath(self._path)
        super(GraphicsView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        end = event.pos()
        if (
            not self.pixmapItem.pixmap().isNull()
            and self._path_item is not None
        ):
            self._path.lineTo(self.mapToScene(end))
            self._path.closeSubpath()
            self._path_item.setPath(self._path)
            self._path_item.setBrush(QtGui.QBrush(QtGui.QColor("red")))
            self._path_item.setFlag(
                QtWidgets.QGraphicsItem.ItemIsSelectable, True
            )
            self._path_item = None

        super(GraphicsView, self).mouseReleaseEvent(event)

    def save(self):
        rect = self.scene().sceneRect()
        pixmap = QtGui.QImage(rect.height(),rect.width(),QtGui.QImage.Format_ARGB32_Premultiplied)
        painter = QtGui.QPainter(pixmap)
        rectf = QRectF(0,0,pixmap.rect().height(),pixmap.rect().width())
        self.scene().render(painter,rectf,rect)
        pixmap.save('file.png')






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QWidget()
    btnSave = QPushButton("Save image")
    view = GraphicsView()
    view.setImage()
    view.resize(640, 480)
    w.setLayout(QVBoxLayout())
    w.layout().addWidget(btnSave)
    w.layout().addWidget(view)
    btnSave.clicked.connect(lambda: view.save())
    w.show()
    # w.save()
    sys.exit(app.exec_())
