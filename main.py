#main
import sys, math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QGroupBox, QMainWindow, QMessageBox
from box import Ui_MainWindow
from gorun import installapk,root_func,wechat_func,winfodis,update_func,devicecon,dangerfunc,pro_func,dpichanger
import win32api,win32con
import webbrowser

class MyMainWindow(QMainWindow, Ui_MainWindow):  # 继承 QMainWindow 类和 Ui_MainWindow 界面类
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类

    def click_pushButton(self):  # 点击 pushButton_01 触发
        installapk(self.QlineEdit.text())
        return

    def click_pushButton_03(self):  # 点击 pushButton_03 触发
        webbrowser.open("https://wwxl.lanzoul.com/b041k7g6f")
        return

    def click_pushButton_04(self):  # 点击 pushButton_04 触发
        root_func(1)
        return

    def click_pushButton_05(self):  # 点击 pushButton_05 触发
        root_func(2)
        return

    def click_pushButton_06(self):  # 点击 pushButton_06 触发
        root_func(3)
        return

    def click_pushButton_07(self):  # 点击 pushButton_07 触发
        root_func(4)
        return

    def click_pushButton_08(self):  # 点击 pushButton_08 触发
        root_func(5)
        return

    def click_pushButton_09(self):  # 点击 pushButton_09 触发
        
        return

    def click_pushButton_10(self):  # 点击 pushButton_10 触发
        
        return

    def aboutToShow_menubug(self):  
        win32api.MessageBox(0,'XunTu Wacth工具箱 v1.0\n code by被遗忘的骨块, XunTu Team 2023','关于',win32con.MB_OK)
        return
class dragbox(QGroupBox_2):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        
        self.setAcceptDrops(True)
        

    def dragEnterEvent(self, e):
      
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore() 

    def dropEvent(self, e):
        installapk(e.mineData().text())


class dragbox(QgroupBox_7):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        
        self.setAcceptDrops(True)
        

    def dragEnterEvent(self, e):
      
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore() 

    def dropEvent(self, e):
        wechat_func(e.mineData().text())


