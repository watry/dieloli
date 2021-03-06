import time
from script.Core import EraPrint,FlowHandle,TextLoading,TextHandle,GameConfig,PyCmd,GameData
from script.Design import CmdButtonQueue

# 载入游戏面板
def loadGamePanel():
    FlowHandle.initCache()
    EraPrint.pnextscreen()
    EraPrint.pnextscreen()
    EraPrint.pobo(1 / 3, TextLoading.getTextData(TextLoading.messagePath, '1'))
    EraPrint.p('\n')

# 游戏主面板
def gameMainPanel():
    EraPrint.pline()
    EraPrint.pl(TextHandle.align(GameConfig.game_name, 'center'))
    EraPrint.pl(TextHandle.align(GameConfig.author, 'right'))
    EraPrint.pl(TextHandle.align(GameConfig.verson, 'right'))
    EraPrint.pl(TextHandle.align(GameConfig.verson_time, 'right'))
    EraPrint.p('\n')
    EraPrint.pline()
    EraPrint.lcp(1 / 3, TextLoading.getTextData(TextLoading.messagePath, '2'))
    time.sleep(1)
    EraPrint.p('\n')
    EraPrint.pline()
    time.sleep(1)
    PyCmd.focusCmd()
    menuInt = CmdButtonQueue.optionint(CmdButtonQueue.logomenu)
    return menuInt
