from analyzeScreenTestUtils import *
from analyzeScreen import inFightSelection
from analyzeScreen import inPlayAgain
from analyzeScreen import inTurn
from analyzeScreen import myTurn
from analyzeScreen import isMyDashboardShining
from analyzeScreen import cardInfoOnScreen
from analyzeScreen import inEndMatch
from analyzeScreen import inMatchMaking
from analyzeScreen import inModeSelection
from analyzeScreen import errorMessageOnScreen


def testInFightSelection():
    fakeGcs = makeFake('fight_selection')
    assert inFightSelection(fakeGcs) == True


def testInPlayAgain():
    fakeGcs = makeFake('play_again')
    assert inPlayAgain(fakeGcs) == True


def testInTurn():
    fakeGcs = makeFake('in_turn')
    assert inTurn(fakeGcs) == True

    fakeGcs = makeFake('in_turn_2')
    assert inTurn(fakeGcs) == True


def testIsMyDashboardShining():
    fakeGcs = makeFake('not_my_turn')
    assert isMyDashboardShining(fakeGcs) == False

    fakeGcs = makeFake('not_my_turn_2')
    assert isMyDashboardShining(fakeGcs) == False

    fakeGcs = makeFake('in_my_turn')
    assert isMyDashboardShining(fakeGcs) == True


def testMyTurn():
    # fakeGcs = makeFake('in_my_turn')
    # assert myTurn(fakeGcs) == True
    pass


def testCardInfoOnScreen():
    fakeGcs = makeFake('card_info_on_screen')
    assert cardInfoOnScreen(fakeGcs) == True


def testInEndMatch():
    fakeGcs = makeFake('in_end_match')
    assert inEndMatch(fakeGcs) == True


def testInMatchMaking():
    fakeGcs = makeFake('in_match_making')
    assert inMatchMaking(fakeGcs) == True


def testInModeSelection():
    fakeGcs = makeFake('in_mode_selection')
    assert inModeSelection(fakeGcs) == True


def testErrorMessageOnScreen():
    fakeGcs = makeFake('in_end_match')

    # fakeGcs = makeFake('error_message_on_screen')
    assert errorMessageOnScreen(fakeGcs) == True
# inBattleHasTimeout


if __name__ == "__main__":
    testInFightSelection()
    testInPlayAgain()
    testInTurn()
    # testMyTurn()
    testIsMyDashboardShining()
    testCardInfoOnScreen()
    testInEndMatch()
    testInMatchMaking()
    testInModeSelection()
