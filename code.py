# coding=utf-8
import threading
import time
import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
import linecache

settingPath = "settings.wl"
text = "<h1><font color={}>{}</font></h1>"
try:
    title = linecache.getline(settingPath, 1).strip()
except:
    title = "title"

try:
    words = eval(linecache.getline(settingPath, 2).strip())
except:
    words = ["Hello!", "你好！"]

try:
    colors = eval(linecache.getline(settingPath, 3).strip())
except:
    colors = ['#E58606', '#5D69B1', '#52BCA3', '#99C945', '#CC61B0', '#24796C', '#DAA51B', '#2F8AC4', '#764E9F',
              '#ED645A']


class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # 设置主窗口标题
        self.setWindowTitle(title)
        # 设置窗口尺寸
        self.resize(500, 60)
        # 获取屏幕尺寸
        screen = QDesktopWidget().screenGeometry()
        width = screen.width()
        height = screen.height()
        # 设置窗口位置
        self.move(random.randint(0, width), random.randint(0, height))
        # 设置状态条
        self.status = self.statusBar()
        statusBar = ["Reboot may fix the problem.", "重启电脑或许可以解决此问题。",
                     "打开任务管理器杀死进程或许可以解决此问题。", "Open Task Manager and kill the process may fix the problem."]
        self.status.showMessage(random.choice(statusBar), 5000)
        # 设置标签
        label = QLabel(self)
        label.setText(text.format(random.choice(colors), random.choice(words)))
        label.resize(300, 50)
        # 在窗口布局中添加控件
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addStretch()


def boom():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("Icon.ico"))  # 设置窗口图标
    widow = Form()
    widow.show()
    sys.exit(app.exec_())


threads = []
i = 0
if __name__ == '__main__':
    while True:
        t = threading.Thread(target=boom)
        threads.append(t)
        time.sleep(1)
        threads[i].start()
        i += 1
