# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])  # 程序实例
dlg = QtWidgets.QDialog()  # 创建对话框

# 创建输入框
ipt = QtWidgets.QLineEdit("在这里输入你想要的内容")

# 创建按钮
btn = QtWidgets.QPushButton("确定")
btn.clicked.connect(
    lambda: QtWidgets.QMessageBox.information(
        dlg, "消息", ipt.text(), QtWidgets.QMessageBox.Ok))  # 给按钮添加响应

# 创建垂直布局，并将输入框和按钮都添加到布局中
vbl = QtWidgets.QVBoxLayout(dlg)
vbl.addWidget(ipt)
vbl.addWidget(btn)

dlg.show()  # 显示对话框
app.exec_()  # 运行程序
