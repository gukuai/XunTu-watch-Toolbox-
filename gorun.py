#gorun
import subprocess
import sys
import os
import sys, math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import win32api,win32con
def adbcomu(command):
        backt=subprocess.check_call(command)
        return backt


    
def installapk(apk):
    
    if apk != '':
        baco=adbcomu("adb install "+apk)
    return baco
    
def dpichanger():
    dpi=self.QlineEdit_2.text()
    bacod=adbcomu("adb shell wm density "+dpi)
    return bacod

def root_func(func):
    if func==1:
        win32api.MessageBox(0,'root之后造成的一切损失和问题后果自负！\n是否继续？（若无需root请关闭本窗口）','root警告',win32con.MB_OK)
    if func==2:
        adbcomu()
    if func==3:
        adbcomu('adb shell am start ') 
    
    if func==4:
        adbcomu()
    if func==5:
        adbcomu()
    
    
    

def wechat_func():
    adbcomu()


def winfodis(model):
    if model != '':

    
def update_func():
        


def devicecon():



def dangerfunc():



def pro_func():


    return
return