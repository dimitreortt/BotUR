from analyzeScreenTestUtils import *
from analyzeScreen import inFightSelection
from analyzeScreen import inPlayAgain


def testInFightSelection():
    fakeGcs = makeFake('fight_selection')
    assert inFightSelection(fakeGcs) == True


def testInPlayAgain():
    fakeGcs = makeFake('play_again')
    assert inPlayAgain(fakeGcs) == True


if __name__ == "__main__":
    testInFightSelection()
    testInPlayAgain()
