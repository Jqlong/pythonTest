# coding=utf-8
from tkinter import *
root = Tk()
root.geometry('200x200')
root.title('计算器示例')
L1 = Button(root, text='1', width=5, bg='yellow')
L2 = Button(root, text='2', width=5)
L3 = Button(root, text='3', width=5)
L4 = Button(root, text='4', width=5)
L5 = Button(root, text='5', width=5, bg='green')
L6 = Button(root, text='6', width=5)
L7 = Button(root, text='7', width=5)
L8 = Button(root, text='8', width=5)
L9 = Button(root, text='9', width=5, bg='yellow')
L0 = Button(root, text='0', width=5)
Lp = Button(root, text='.', width=5)

L1.grid(row=0, column=0)  # 0行0列
L2.grid(row=0, column=1)  # 0行0列
L3.grid(row=0, column=2)  # 0行0列
L4.grid(row=1, column=0)  # 0行0列
L5.grid(row=1, column=1)  # 0行0列
L6.grid(row=1, column=2)  # 0行0列
L7.grid(row=2, column=0)  # 0行0列
L8.grid(row=2, column=1)  # 0行0列
L9.grid(row=2, column=2)  # 0行0列
L0.grid(row=3, column=0, columnspan=2, sticky=E+W)  # 0行0列  左右贴紧
Lp.grid(row=3, column=2, sticky=E+W)  # 0行0列  左右贴紧
root.mainloop()

