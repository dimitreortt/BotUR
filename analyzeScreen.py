from coordinates import BoxesCoords, ButtonsCoords, GameItemsCoords
from pixels import getColorSum as gcs, ColorSums, getColorSumeExcluaPorFavor, saveImage
from pixels import ButtonPixels
from quickGrab import screenGrab, grabEntireScreen
import time
from click import clickBlankSpace


def checkMyBackground(getColorSum=gcs):
    return getColorSum(BoxesCoords.MyBackground)


def checkOpponentsBackground(getColorSum=gcs):
    return getColorSum(BoxesCoords.OpponentsBackground)
    # background = getColorSum(BoxesCoords.)


def checkMyDashBoard(getColorSum=gcs):
    return getColorSum(BoxesCoords.MyPlayerDashBoard)


def checkEndMatch(getColorSum=gcs):
    return getColorSum(BoxesCoords.EndMatch)


def inPlayAgain(getColorSum=gcs):
    return getColorSum(BoxesCoords.PlayAgain) in ColorSums.PlayAgain


def errorMessageOnScreen(getColorSum=gcs):
    im = grabEntireScreen()
    # print(im.getpixel(GameItemsCoords.ErrorOK), ButtonPixels.ErrorOK)
    return im.getpixel(GameItemsCoords.ErrorOK) == ButtonPixels.ErrorOK


def cardInfoOnScreen(getColorSum=gcs):
    return getColorSum(BoxesCoords.CardInfo) in ColorSums.CardInfo


def loopCardInfoOnScreen():
    while True:
        print(cardInfoOnScreen())
        time.sleep(0.3)


def inEndMatch(getColorSum=gcs):
    print('Checking end match...')
    if(getColorSum(BoxesCoords.EndMatch) in ColorSums.EndMatch):
        print('Endmatch!')
        return True

    elif(inPlayAgain()):
        print('I didnt find the end match, \
    but i found the play again, so I am returning true...')
        return True
    # if errorMessageOnScreen():
    #   clickTimeoutOK()

    return False


def inBattleHasTimeout(getColorSum=gcs):
    return getColorSum(BoxesCoords.TheBattleHasTimeout) == ColorSums.TheBattleHasTimeout


def inModeSelection(getColorSum=gcs):
    return getColorSum(BoxesCoords.GameModesNavbarBox) in ColorSums.GameModes


def inFightSelection(getColorSum=gcs):
    return getColorSum(BoxesCoords.Fight) == ColorSums.Fight


def inTurn(getColorSum=gcs):
    return getColorSum(BoxesCoords.MyPlayerDashBoard) in ColorSums.MyDashBoard


def inMatchMaking(getColorSum=gcs):
    return getColorSum(BoxesCoords.StuckMatchMaking) in ColorSums.StuckMatchMaking


def isMyDashboardShining(getColorSum=gcs):
    # print(getColorSum(BoxesCoords.MyPlayerDashBoardIncludingShineableRegion),
    #       ColorSums.MyDashBoardNotShining)

    return getColorSum(BoxesCoords.MyPlayerDashBoardIncludingShineableRegion) not in ColorSums.MyDashBoardNotShining


def loopInTurn():
    while True:
        print(inTurn())


def myTurn(getColorSum=gcs):
    if not inTurn(getColorSum):
        print('Error! Not in turn, imagine in mine! -> We are fighting!')
        return 'Not in turn!'

    return isMyDashboardShining(getColorSum)

    # soma, fullsnap = getColorSumeExcluaPorFavor(BoxesCoords.MyBackground)
    # if soma != ColorSums.MyBackground:
    #     # saveImage(fullsnap)
    #     return True

    # return False


def scanUnexpectedPages():
    print('Scanning unexpected pages...')
    if inFightSelection():
        return 'Fight Selection!'

    elif inPlayAgain():
        return 'Play Again!'

    elif inModeSelection():
        # return 'Mode Selection'    # não posso retratar tudo em todo lugar!
        pass

    elif cardInfoOnScreen():
        clickBlankSpace()


def stuckInMatchMaking():
    for i in range(10):
        if not inMatchMaking():
            return False

        time.sleep(2)
    return True


if __name__ == '__main__':
    # print(inFightSelection())
    # print(inPlayAgain())
    # print(inTurn())
    # print(isMyDashboardShining())
    # print(myTurn())
    # print(inEndMatch())
    print(errorMessageOnScreen())
