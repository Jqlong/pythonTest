

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('薪资统计')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资表")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)

        self.button.clicked.connect(self.handleCalc)


    def handleCalc(self):
        info = self.textEdit.toPlainText()

        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()


# def handleCalc():
#     info = textEdit.toPlainText()
#
#     # 薪资20000 以上 和 以下 的人员名单
#     salary_above_20k = ''
#     salary_below_20k = ''
#     for line in info.splitlines():
#         if not line.strip():
#             continue
#         parts = line.split(' ')
#         # 去掉列表中的空字符串内容
#         parts = [p for p in parts if p]
#         name,salary,age = parts
#         if int(salary) >= 20000:
#             salary_above_20k += name + '\n'
#         else:
#             salary_below_20k += name + '\n'
#
#     QMessageBox.about(window,
#                 '统计结果',
#                 f'''薪资20000 以上的有：\n{salary_above_20k}
#                 \n薪资20000 以下的有：\n{salary_below_20k}'''
#                 )
#
#
# app = QApplication([])   # QApplication 提供了整个图形界面程序的底层管理功能
#
# window = QMainWindow()   # 主窗口
# window.resize(500, 400)  # 窗口的大小
# window.move(300, 310)    # 出现的位置
# window.setWindowTitle('薪资统计')
#
# textEdit = QPlainTextEdit(window)   # 文本框  window是父类
# textEdit.setPlaceholderText("请输入薪资表")   # 提示文本
# textEdit.move(10, 25)   # 出现在父类的位置
# textEdit.resize(300, 350)
#
# button = QPushButton('统计', window)  # 按钮
# button.move(380, 80)
#
# button.clicked.connect(handleCalc)
#
# window.show()   # 显示窗口
#
# app.exec_()  # 等待用户输入事件
