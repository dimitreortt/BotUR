from quickGrab import x_pad, y_pad

# Coordenadas de Play Area


class ButtonsCoords():
    WebGl = (673, 596)
    # Ranked = (840, 38)
    Ranked = (783, 32)
    PvP = (842, 202)
    Type1 = (675, 176)
    Type2 = (778, 176)
    FreeFight = (840, 383)
    # Fight = (510, 547)
    Fight = (673, 668)

    TouchToStart = (673, 571)
    PlayAgain = (676, 666)
    Reload = (86, 51)

# Coordenadas Globais


class BoxesCoords():
    # GameModesNavbarBox = (580, 129, 1143, 150)
    GameModesNavbarBox = (658, 189, 1027, 215)
    Fight = (584, 645, 766, 665)
    MyBackground = (1060, 640, 1090, 660)
    OpponentsBackground = (274, 122, 290, 140)
    MyPlayerDashBoard = (834, 659, 867, 665)
    MyPlayerDashBoardIncludingShineableRegion = (834, 648, 1002, 659)
    EndMatch = (1000, 500, 1060, 550)
    PlayAgain = (610, 643, 738, 690)
    TheBattleHasTimeout = (382, 360, 590, 373)
    CardInfo = (776, 536, 806, 550)
    StuckMatchMaking = (1050, 207, 1124, 224)
# (915, 61)
# (757, 13)
# x_pad = 163
# y_pad = 107


class GameItemsCoords():
    Card1 = (450, 535)
    Card2 = (600, 535)
    Card3 = (750, 535)
    Card4 = (900, 535)

    Cards = [Card1, Card2, Card3, Card4]

    # Pillz = [(415, 297), (447, 296), (469, 296), (500, 298), (529, 299), (552, 299), (576, 298), (603, 298), (628, 298), (660, 304), (682, 298), (706, 295)]

    Pillz = [(587, 444), (611, 444), (635, 444), (659, 444), (683, 444), (707, 444),
             (731, 444), (755, 444), (779, 444), (803, 444), (827, 444), (851, 444)]

    Fury = (832, 299)
    FightRound = (782, 522)

    TimeOutOK = (674, 526)
    ErrorOK = (674, 526)
    BlankSpace = (700, 640)


def generatePillzCoords():
    start = 587
    end = 851
    pillz = [start]
    soma = 0
    for i in range(11):
        soma += 24
        # if i in [2, 5, 8, 10]:
        #     soma -= 1
        pillz.append(start+soma)

    return [(item, 444) for item in pillz]


if __name__ == "__main__":
    print(generatePillzCoords())
    pass
