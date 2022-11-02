from PyQt5.QtGui import QPixmap
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QApplication, QMessageBox, QGraphicsView
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QRectF


class Stats:
    def __init__(self):

        qFile_stats = QFile("../../QT Designer/first_alter.ui")
        qFile_stats.open(QFile.ReadOnly)
        qFile_stats.close()

        self.ui = QUiLoader().load(qFile_stats)

        self.ui.button


    def savePicture(self):
        rect = QGraphicsView.viewport(self.dlg.gvPointRecords).rect()
        pixmap = QPixmap(rect.size())
        painter = QPainter(pixmap)
        painter.begin(pixmap)
        self.dlg.gvPointRecords.render(painter,QRectF(pixmap.rect()),rect)
        painter.end()


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()