from PIL import Image
from PIL import ImageOps
import os
from coordinates import BoxesCoords
from numpy import *


class Array(object):
    def __init__(self, lst):
        self.lst = lst

    def sum(self):
        count = 0
        i = 0
        for item in self.lst:
            count += item
            i += 1
            # if i % 10 == 0:
            #     print(count)

        return count


def toArray(tupleList):
    return Array([item[0] for item in tupleList])


def saveCroppedTestImg(imageName, im):
    outputPath = os.getcwd() + '\\snapshots\\TestImages\\' + \
        imageName + '_cropped.png'
    im.save(outputPath, 'PNG')
    pass


def fakeGetColorSum(box, imageName, save=True):
    path = os.getcwd() + '\\snapshots\\TestImages\\' + imageName + '.png'
    im = Image.open(path)
    im = im.crop(box)
    if save:
        saveCroppedTestImg(imageName, im)
    im = ImageOps.grayscale(im)
    a = array(im.getcolors())
    a = a.sum()
    # print(a)
    return a


def makeFake(imageName):
    def gcs(box):
        return fakeGetColorSum(box, imageName)

    return gcs


if __name__ == "__main__":
    # fakeGetColorSum((584, 645, 766, 665), 'fight_selection')
    # fakeGetColorSum((610, 643, 738, 685), 'play_again', True)
    print(fakeGetColorSum(
        BoxesCoords.MyPlayerDashBoardIncludingShineableRegion, 'in_my_turn', True))

    print(fakeGetColorSum(
        BoxesCoords.MyPlayerDashBoardIncludingShineableRegion, 'not_my_turn', True))
