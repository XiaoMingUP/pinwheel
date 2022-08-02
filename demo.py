import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class pinwheel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('../pic/1.png'))
        self.setWindowTitle('旋转的风车')
        self.resize(600,600)
        self.move(400,150)

        self.timer = QTimer()
        # 设置窗口计时器
        self.timer.timeout.connect(self.update)
        self.timer.start(5)
        # self.timer.start(20)
        # self.timer.start(50)
        self.k = 10

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 将QWidget对象的中心位置作为绘制的中心坐标点
        painter.translate(self.width() / 2, self.height() / 2)
        # 画线
        painter.drawLine(0, 0, 0, 200)
        # 画点
        painter.drawPoint(0, 0)

        # 将画布旋转角度
        painter.rotate(self.k)
        self.k = self.k - 20

        # 画半圆
        # drawArc syntax:x轴坐标，y轴坐标，宽，长度，开始角度，跨角度
        # drawArc(x_axis, y_axis, width, length, startAngle, spanAngle)
        painter.drawArc(0, -50, 100, 100, 0, 180 * 16)
        painter.drawArc(-50, -100, 100, 100, 90 * 16, 180 * 16)
        painter.drawArc(-100, -50, 100, 100, 180 * 16, 180 * 16)
        painter.drawArc(-50, 0, 100, 100, -90 * 16, 180 * 16)
        painter.drawLine(0, 0, 100, 0)
        painter.drawLine(0, 0, 0, -100)
        painter.drawLine(0, 0, -100, 0)
        painter.drawLine(0, 0, 0, 100)

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 声明对象
    pinwheel = pinwheel()
    # 显示窗口
    pinwheel.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
