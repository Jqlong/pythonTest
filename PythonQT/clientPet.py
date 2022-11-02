from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon

class Stats:
    def __init__(self):

        qFile_stats = QFile("../ui/clientPet.ui")
        qFile_stats.open(QFile.ReadOnly)
        qFile_stats.close()

        self.ui = QUiLoader().load(qFile_stats)

app = QApplication([])

# 加载icon
app.setWindowIcon(QIcon('logo.png'))
stats = Stats()
stats.ui.show()
app.exec_()
