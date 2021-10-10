from quickGrab import x_pad, y_pad

# Coordenadas de Play Area


class ButtonsCoords():
    WebGl = (515, 469)
    # Ranked = (840, 38)
    Ranked = (783, 32)
    PvP = (642, 32)
    Type1 = (675, 176)
    Type2 = (778, 176)
    FreeFight = (698, 234)
    # Fight = (510, 547)
    Fight = (673, 668)

    TouchToStart = (510, 439)
    PlayAgain = (512, 550)
    Reload = (-75, -55)

# Coordenadas Globais


class BoxesCoords():
    # GameModesNavbarBox = (580, 129, 1143, 150)
    GameModesNavbarBox = (660, 125, 1060, 150)
    Fight = (584, 645, 766, 665)
    MyBackground = (1060, 640, 1090, 660)
    OpponentsBackground = (274, 122, 290, 140)
    MyPlayerDashBoard = (850, 603, 1020, 650)
    EndMatch = (1000, 500, 1060, 550)
    PlayAgain = (610, 643, 738, 690)
    TheBattleHasTimeout = (382, 360, 590, 373)
    CardInfo = (789, 497, 822, 513)
    StuckMatchMaking = (920, 120, 1078, 168)
# (915, 61)
# (757, 13)
# x_pad = 163
# y_pad = 107


class GameItemsCoords():
    Card1 = (275, 380)
    Card2 = (433, 386)
    Card3 = (598, 393)
    Card4 = (766, 368)

    Cards = [Card1, Card2, Card3, Card4]

    # Pillz = [(415, 297), (447, 296), (469, 296), (500, 298), (529, 299), (552, 299), (576, 298), (603, 298), (628, 298), (660, 304), (682, 298), (706, 295)]

    Pillz = [(415, 302), (442, 302), (469, 302), (495, 302), (522, 302), (549, 302),
             (575, 302), (602, 302), (629, 302), (655, 302), (682, 302), (708, 302)]

    Fury = (832, 299)
    FightRound = (638, 384)

    TimeOutOK = (516, 389)
    ErrorOK = (509, 401)
    BlankSpace = (485, 516)


def generatePillzCoords():
    start = 578
    pillz = [start]
    soma = 0
    for i in range(11):
        soma += 27
        if i in [2, 5, 8, 10]:
            soma -= 1
        pillz.append(start+soma)

    return [(item - x_pad, 409 - y_pad) for item in pillz]


if __name__ == "__main__":
    pass
