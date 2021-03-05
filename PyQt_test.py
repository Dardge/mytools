from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QDesktopWidget
from PyQt5.QtCore import QBasicTimer,Qt
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QColor
import sys

class Excample(QWidget):
    def __init__(self):
        super(Excample,self).__init__()
        self.initUI()

    def initUI(self):
        # 设置背景图片
        window_pale = QPalette()
        window_pale.setBrush(self.backgroundRole(), QBrush(QPixmap("F:\\mytols\\resources\\IMG_0100.jpg")))
        # window_pale.setColor(QPalette.Background, Qt.transparent)
        self.setPalette(window_pale)

        # 设置背景透明度(要全透明必须设置成无边框)
        # self.setAttribute(Qt.WA_TranslucentBackground,True)

        # 窗口无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # 界面透明度
        # self.setWindowOpacity(0.5)



        # 设置窗口标题
        self.setWindowTitle("我是一个进度条😎")
        # 设置窗口图标
        self.setWindowIcon(QIcon("F:\\mytols\\resources\\IMG_0100.jpg"))
        # 获取屏幕大小
        screen_size = QDesktopWidget().screenGeometry()
        # 设置窗口的大小为屏幕的一半,resize方法窗口默认居中
        self.resize(screen_size.width()/2, screen_size.height()/2)
        # 构建计时器
        self.timer = QBasicTimer()
        # 计数
        self.step = 0

        # 构建一个进度条
        self.pbar = QProgressBar(self)
        # 从窗口的左上角的(30,50)开始，显示一个250*25的进度条,其中进度条的百分比文本部分长度为40
        self.pbar.setGeometry(30, 50, 220, 25)
        # 设置开始按钮
        self.btn1 = QPushButton("开始", self)
        self.btn2 = QPushButton("复位", self)
        # 按钮位置
        self.btn1.move(30, 90)  # QPushButton大小为90*27
        self.btn2.move(120, 90)
        # 设置按钮点击关联到进度条，进而控制进度条的开始和停止
        # self.btn1.clicked.connect(lambda:self.doAction()) # 如果connect里的函数加括号，需使用lambda函数
        self.btn1.clicked.connect(self.doAction)
        self.btn2.clicked.connect(self.reset)
        self.btn3 = QPushButton("EXIT", self)
        # self.btn3.move(10,50)
        self.btn3.move(self.geometry().width() - 115, self.geometry().height() - 50)
        # self.btn3.clicked.connect(self.go_quit)
        self.btn3.clicked.connect(QApplication.instance().quit)  # 退出程序

    def doAction(self):
        # 判断是否已经激活或者是否处于执行状态
        if self.timer.isActive():
            # 停止
            self.timer.stop()
            self.btn1.setText("开始")
        else:
            self.timer.start(100, self)
            self.btn1.setText("停止")

    # 重写timerEvent方法,控制进度条
    def timerEvent(self, *args, **kargs):
        if self.step >= 100:
            # 停止定时器，进而停止进度条
            self.timer.stop()
            self.btn1.setText("完成")
            return
        self.step += 1
        # 把进度条每次重置的值赋值给progressBar
        self.pbar.setValue(self.step)

    def reset(self):
        self.step = 0
        self.pbar.setValue(self.step)
        self.timer.stop()
        self.btn1.setText("开始")

    def go_quit(self):
        # sender = self.sender()  # sender是发送信号的对象，此处发送信号的对象是btn3按钮
        # print(sender.text()+"被按下")
        QApplication.instance().quit()


if __name__ == '__main__':
    # 创建一个QT应用对象
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("D:\\MyWork\\picture\\153.jpg"))
    ui = Excample()
    ui.show()
    sys.exit(app.exec_())  # 等待app退出时程序结束,app.exec_()是一个阻塞函数，等待app结束后此函数返回0
