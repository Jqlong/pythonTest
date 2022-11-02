from PySide2.QtGui import QPalette, QPixmap, QBrush, QPainter
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, Qt
from PySide2 import QtSvg


class Stats:
    def __init__(self):
        qFile_stats = QFile("StackWidgetTest.ui")
        qFile_stats.open(QFile.ReadOnly)
        qFile_stats.close()

        self.ui = QUiLoader().load(qFile_stats)

        self.ui.treeWidget.clicked.connect(self.title_text)

        # 背景自适应
        palette = QPalette()
        pix = QPixmap('images/back_icon.png')
        pix = pix.scaled(self.ui.width(), self.ui.height())
        palette.setBrush(QPalette.Window, QBrush(pix))
        self.ui.setPalette(palette)



        # 获取当前控件的标题
        # self.index_title()

    def title_text(self):
        item = self.ui.treeWidget.currentItem()  # 返回一个QTreeWidgetItem类型 当前
        # count = item.childCount()  # 获取父节点中子树的个数
        # 返回项目的子列表中给定子项的索引
        # index = item.indexOfChild(item)

        # 先获取header的QTreeWidgetItem
        item_header = self.ui.treeWidget.headerItem()

        list = self.ui.treeWidget.selectedItems()

        index_1 = self.ui.treeWidget.indexOfTopLevelItem(item)  # 返回顶级项的索引 有就返回索引值，无就返回-1
        column = self.ui.treeWidget.columnCount()  # 显示列数

        name = item.text(0)
        print(name)  # 输出各个控件的名称
        # print(column)  # 输出列
        # print(count)
        # print(index)
        # print(item_header.text(0))  # 输出头标题 可视化
        # print(list)
        # --------------------------------分割线  获取索引------------------------
        titles_list = ['各频率出现的概率及分布',
                       '固定某一频率其它频率出现的概率',
                       '各频率对应位置点的聚类分析',
                       '固定频率下位置信息的统计特性',
                       '固定频率下强度信息的统计特性',
                       '辐射噪声线谱的位置与强度联合分析',
                       '振动噪声的位置与强度统计分析',
                       '艇端振动噪声与辐射噪声数据映射关系分析'
                       ]

        for title in titles_list:
            if name == title:
                print(titles_list.index(name))
                # ----添加点击事件
                self.page_select(titles_list.index(name))

    def page_select(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)



app = QApplication([])
stats = Stats()
# 设置背景图

stats.ui.showMaximized()
stats.ui.show()
app.exec_()
