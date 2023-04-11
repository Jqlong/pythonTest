# coding=utf-8
import tkinter
root = tkinter.Tk()  # 创建窗口
label = tkinter.Label(root, text='Hello, Python')
label.pack()  # 将label添加到窗口显示
button = tkinter.Button(root, text='Button1')
button.pack(side=tkinter.LEFT)  # 将button添加到窗口
button1 = tkinter.Button(root, text='Button2')
button1.pack(side=tkinter.RIGHT)  # 将button2添加到窗口
root.mainloop()


