from mouse import setMousePos, leftClick
from coordinates import ButtonsCoords, BoxesCoords, GameItemsCoords
import time

def clickWebGlButton():
  setMousePos(ButtonsCoords.WebGl)
  leftClick()
  print('clicked WebGl Button')

def clickRanked():
  setMousePos(ButtonsCoords.Ranked)
  leftClick()
  time.sleep(0.1)
  print('clicked Ranked')

def clickPvP():
  setMousePos(ButtonsCoords.PvP)
  leftClick()
  time.sleep(0.1)
  print('clicked PvP')

def clickTourneyType1():
  setMousePos(ButtonsCoords.Type1)
  leftClick()
  print('clicked Type1')

def clickTourneyType2():
  setMousePos(ButtonsCoords.Type2)
  leftClick()
  print('clicked Type2')

def clickFreeFight():
  setMousePos(ButtonsCoords.FreeFight)
  leftClick()
  print('clicked Type2')

def clickFight():
  print('clicked Fight')
  setMousePos(ButtonsCoords.Fight)
  leftClick()

def clickTouchToStart():
  print('clicked Touch To Start')
  setMousePos(ButtonsCoords.TouchToStart)
  leftClick()

def clickTimeoutOK():
  setMousePos(GameItemsCoords.TimeOutOK)
  leftClick()

def clickPlayAgain():
  setMousePos(ButtonsCoords.PlayAgain)
  leftClick()

def clickReloadPage():
  setMousePos(ButtonsCoords.Reload)
  leftClick()
  print('Clicked Reload Page')

def clickBlankSpace():
  setMousePos(GameItemsCoords.BlankSpace)
  leftClick()

def clickFightRound():
  setMousePos(GameItemsCoords.FightRound)
  leftClick()
  time.sleep(2)
  setMousePos(GameItemsCoords.FightRound)
  leftClick()
  time.sleep(0.3)
  leftClick()

def clickCard(cardIndex):
  setMousePos(GameItemsCoords.Cards[cardIndex])
  leftClick()

def clickAddPillz(pillzNumber):
  time.sleep(0.9)
  setMousePos(GameItemsCoords.Pillz[pillzNumber - 1])
  leftClick()

def testAddPillz(i):
  for y in range(i):
    clickAddPillz(y + 1)
