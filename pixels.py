import os
from PIL import ImageGrab
from PIL import ImageOps
from quickGrab import x_pad, y_pad
from numpy import *
import time


class ButtonPixels():
    ErrorOK = (255, 160, 0)


class ColorSums():
    # GameModes = 41435
    GameModes = 38565  # 38373 #38767
    Fight = 3640  # 28708
    MyBackground = 10718
    MyDashBoard = (29925, 29128, 28052, 32482, 32482)
    EndMatch = (3577, 3820, 5409)
    PlayAgain = (25168, 25033, 6016)
    TheBattleHasTimeout = 31684
    CardInfo = (2121, -1)
    StuckMatchMaking = (39924, -1)

# Deve receber a box em coordenadas globais!


def getColorSum(box, save=False):

    bx1, by1, bx2, by2 = box
    # print(x_pad, y_pad)
    box = (bx1, by1, bx2, by2)
    # print(box)
    im = ImageGrab.grab(box)
    if save:
        im.save(os.getcwd() + '\\snapshots\\' +
                str(int(time.time())) + '.png', 'PNG')

    im = ImageOps.grayscale(im)
    a = array(im.getcolors())
    a = a.sum()
    # print(a)
    return a

# Deve receber a box em coordenadas globais!


def getColorSumeExcluaPorFavor(box, save=False):

    bx1, by1, bx2, by2 = box
    # print(x_pad, y_pad)
    box = (bx1, by1, bx2, by2)
    # print(box)
    im = ImageGrab.grab(box)
    fullsnap = ImageGrab.grab()
    if save:
        im.save(os.getcwd() + '\\snapshots\\' +
                str(int(time.time())) + '.png', 'PNG')

    im = ImageOps.grayscale(im)
    a = array(im.getcolors())
    a = a.sum()
    # print(a)
    return a, fullsnap


def saveImage(im):
    im.save(os.getcwd() + '\\snapshots\\' +
            str(int(time.time())) + '.png', 'PNG')
