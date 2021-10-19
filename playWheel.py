from mouse import leftClick
import time
import pyautogui as gui


def clickCardAndSpinButton(x, yc, yb):
    gui.moveTo(x, yc)
    leftClick()
    time.sleep(0.4)
    leftClick()
    time.sleep(0.2)
    gui.moveTo(x, yb)
    leftClick()


def playFirst():
    clickCardAndSpinButton(-29, -951, -842)
    pass


def playSecond():
    clickCardAndSpinButton(1251, -951, -842)
    pass


def playThird():
    clickCardAndSpinButton(-29, -254, -135)
    pass


def playFourth():
    clickCardAndSpinButton(1251, -254, -135)
    pass


def playFifth():
    clickCardAndSpinButton(360, 418, 505)
    pass


def playSixth():
    clickCardAndSpinButton(1044, 418, 505)
    pass


def playWheel():
    time.sleep(2)

    count = 0
    while (count < 125):
        count += 1
        print(count)
        playFirst()
        playSecond()
        playThird()
        playFourth()
        playFifth()
        #playSixth()
        time.sleep(0.5)


playWheel()
print(gui.position())
