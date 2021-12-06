Urban Rivals is a massively multi-player online virtual trading card game. In this game the goal is to collect cards, to do that you must seek for prizes and rewards, you can fight other players, compete in tourneys, weekly competitions and ocasional events, or finish missions to be rewarded.

I created a bot in python that can fight other players in Urban Rivals. The bot implements a state machine, it analyzes parts of the screen to discover in which state a match is, and then it takes actions when needed, such as choosing a card to be played, adding power pillz to raise the attack, or starting another match when it is in the _endmatch_ state.

The bot had several interesting results, and a few amazing feats.

- It played 4000 matches with a winrate of 42% (my own winrate is 64%)
- It won 5+ very rare cards in events and hundreds of other simpler cards, enough to buy a relevant part of the entire collection of the game
- It finished one week as the account with most Battle Points won
- It finished the month as the fourth account with most Battle Points won
- It finished sixth and eighth in two Tourneys (one of the Game Modes, a tourney held every other hour)
- It won 14 matches in a row
- It won 62% of the matches in a special period including 540 matches

This bot has played for about 1 month in 2020 and has since been deactivated!

After some time I visited the game again and found out about a Wheel Of Fortune where players also can spin to win rewards, so I created another script to play the wheel too. It played for a week in 2021 and has since been deactivated.

The main packages necessary for this bot were **PIL** (ImageGrab and ImageOps) and **pyautogui**.
