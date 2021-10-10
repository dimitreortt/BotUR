from PIL import Image
from PIL import ImageOps
import os
# from numpy import array


class Array(object):
    def __init__(self, lst):
        self.lst = lst

    def sum(self):
        count = 0
        for item in self.lst:
            count += item

        return count


def toArray(tupleList):
    return Array([item[0] for item in tupleList])


def fakeGetColorSum(box, imageName, save=False):
    path = os.getcwd() + '\\snapshots\\TestImages\\' + imageName + '.png'
    im = Image.open(path)
    im = im.crop(box)
    outputPath = os.getcwd() + '\\snapshots\\' + imageName + "_cropped.png'
    if save:
        im.save(outputPath, 'PNG')
    im = ImageOps.grayscale(im)
    colorSums = im.getcolors()
    colorSums = toArray(colorSums)
    totalSum = colorSums.sum()
    return totalSum


def makeFake(imageName):
    def gcs(box):
        return fakeGetColorSum(box, imageName)

    return gcs


if __name__ == "__main__":
    # fakeGetColorSum((584, 645, 766, 665), 'fight_selection')
    fakeGetColorSum((610, 643, 738, 685), 'play_again', True)
