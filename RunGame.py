from PeterPokerBot3 import *
from multiplayer_holdem_game3 import *
from multiplayer_holdem_game2 import *
import numpy as np


# if __name__ == '__main__':
#     player1 = CPUPlayer(100, "Player 1")
#     from PeterPokerBot2 import CPUPlayer2
#     player2 = CPUPlayer2(100, "Player 2")
#     player3 = CPUPlayer3(100, "Player 3")
#     player4 = CPUPlayer2(100, "Player 4")
#     player5 = CPUPlayer2(100, "Player 5")
#     print()
#     print()
#     play_holdem([player1, player2, player3, player4, player5], 5, 10)


# if __name__ == '__main__':
#     player1 = CPUPlayer3(500, "Player 1")
#     from PeterPokerBot2 import CPUPlayer2
#     player2 = CPUPlayer(random.randint(150, 500), "Player 2")
#     player3 = CPUPlayer2(random.randint(150, 500), "Player 3")
#     player4 = CPUPlayer2(random.randint(150, 500), "Player 4")
#     player5 = CPUPlayer2(random.randint(150, 500), "Player 5")
#     print()
#     print()
#     play_holdem2([player1, player2, player3, player4, player5], 2, 5)


if __name__ == '__main__':
    player1 = CPUPlayer3(400, "Player 1")
    player56 = CLPlayer(810, "Player")
    from PeterPokerBot2 import CPUPlayer2
    player2 = CLPlayer(448, "Player 2")
    player3 = CLPlayer(506, "Player 3")
    player4 = CLPlayer(152, "Player 4")
    player5 = CLPlayer(784, "Player 5")
    player6 = CLPlayer(338, "Player 6")
    player7 = CLPlayer(376, 'Player 7')
    print()
    print()
    play_holdem3([player1, player2, player56, player3, player4, player5, player6, player7], 2, 5)
