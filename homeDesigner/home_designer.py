from time import sleep

from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        qFile_stats = QFile('homeDesigner_1_1.ui')
        qFile_stats.open(QFile.ReadOnly)
        qFile_stats.close()

        self.ui = QUiLoader().load(qFile_stats)

        self.ui.pushButton_39.clicked.connect(self.first_list_button())
        # self.ui.pushButton_40.clicked.connect(self.second_list_button())

    # 第一个按钮的事件
    def first_list_button(self):
        self.ui.stackedWidget.setCurrentIndex(5)
    def second_list_button(self):
        self.ui.stackedWidget.setCurrentIndex(3)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
