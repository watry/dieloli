# -*- coding: UTF-8 -*-
import os,time
from script.Core import PyCmd,CacheContorl,EraPrint,GameData
from script.Flow import CreatorCharacter,SaveHandleFrame
from script.Panel import MainPanel

# 启动游戏界面
def open_func():
    MainPanel.loadGamePanel()
    time.sleep(1)
    main_func()

# 主界面
def main_func():
    ans = MainPanel.gameMainPanel()
    if ans == 0:
        EraPrint.p('\n')
        newgame_func()
    elif ans == 1:
        loadgame_func()
    elif ans == 2:
        quitgame_func()

# 主界面新建游戏调用
def newgame_func():
    PyCmd.clr_cmd()
    CacheContorl.temporaryCharacter = CacheContorl.temporaryCharacterBak.copy()
    CreatorCharacter.inputName_func()

# 主界面读取游戏调用
def loadgame_func():
    PyCmd.clr_cmd()
    SaveHandleFrame.loadSave_func('MainFlowPanel')

# 主界面退出游戏调用
def quitgame_func():
    os._exit(0)