from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

class Stats:
    def __init__(self):

        qFile_stats = QFile("../ui/httpClient.ui")
        qFile_stats.open(QFile.ReadOnly)
        qFile_stats.close()

        self.ui = QUiLoader().load(qFile_stats)

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()