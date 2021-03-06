from script.Core import CacheContorl,TextLoading,EraPrint,PyCmd,GameConfig
from script.Design import GameTime,CmdButtonQueue,MapHandle,CharacterHandle
import math

# 用于查看当前场景的面板
def seeScenePanel():
    titleText = TextLoading.getTextData(TextLoading.stageWordPath,'75')
    EraPrint.plt(titleText)
    timeText = GameTime.getDateText()
    EraPrint.p(timeText)
    EraPrint.p(' ')
    scenePath = CacheContorl.characterData['character']['0']['Position']
    scenePathStr = MapHandle.getMapSystemPathStrForList(scenePath)
    sceneData = CacheContorl.sceneData[scenePathStr].copy()
    sceneName = sceneData['SceneName']
    sceneInfoHead = TextLoading.getTextData(TextLoading.stageWordPath, '76')
    sceneInfo = sceneInfoHead + sceneName
    EraPrint.p(sceneInfo)
    EraPrint.plittleline()

# 用于查看当前场景上角色列表的面板
def seeSceneCharacterListPanel():
    inputS = []
    seeCharacterText = TextLoading.getTextData(TextLoading.messagePath,'26')
    EraPrint.p(seeCharacterText)
    EraPrint.p('\n')
    scenePath = CacheContorl.characterData['character']['0']['Position']
    nameList = MapHandle.getSceneCharacterNameList(scenePath,True)
    nameList = getNowPageNameList(nameList)
    inputS = CmdButtonQueue.optionstr('',cmdColumn=10,cmdSize='center',askfor=False,cmdListData=nameList)
    return inputS

# 用于切换角色列表页面的面板
def changeSceneCharacterListPanel():
    nameListMax = int(GameConfig.in_scene_see_player_max)
    nowPage = int(CacheContorl.panelState['SeeSceneCharacterListPanel'])
    characterMax = CharacterHandle.getCharacterIndexMax()
    pageMax = math.floor(characterMax / nameListMax)
    pageText = '(' + str(nowPage) + '/' + str(pageMax) + ')'
    EraPrint.printPageLine(sample = '-',string = pageText)

# 用于获取当前页面下的名字列表
def getNowPageNameList(nameList):
    nowPage = int(CacheContorl.panelState['SeeSceneCharacterListPanel'])
    nameListMax = int(GameConfig.in_scene_see_player_max)
    newNameList = []
    nowNameStartId = nowPage * nameListMax
    for i in range(nowNameStartId,nowNameStartId + nameListMax):
        if i < len(nameList):
            newNameList.append(nameList[i])
    return newNameList

# 用于查看对象信息的面板
def seeCharacterInfoPanel():
    characterInfo = TextLoading.getTextData(TextLoading.stageWordPath, '77')
    EraPrint.p(characterInfo)
    characterId = CacheContorl.characterData['characterId']
    characterData = CacheContorl.characterData['character'][characterId]
    characterName = characterData['Name']
    EraPrint.p(characterName)
    EraPrint.p(' ')
    intimateInfo = TextLoading.getTextData(TextLoading.stageWordPath,'16')
    gracesInfo = TextLoading.getTextData(TextLoading.stageWordPath,'17')
    characterIntimate = characterData['Intimate']
    characterGraces = characterData['Graces']
    characterIntimateText = intimateInfo + characterIntimate
    characterGracesText = gracesInfo + characterGraces
    EraPrint.p(characterIntimateText)
    EraPrint.p(' ')
    EraPrint.p(characterGracesText)
    EraPrint.plittleline()

def inSceneButtonPanel():
    inputs = CmdButtonQueue.optionint(cmdList=CmdButtonQueue.inscenelist1, cmdColumn=9, askfor=False, cmdSize='center')
    EraPrint.plittleline()
    return inputs
