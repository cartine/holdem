from PeterPokerBot3 import *

if __name__ == '__main__':
    player1 = CPUPlayer(100, "Player 1")
    from PeterPokerBot2 import CPUPlayer2
    player2 = CPUPlayer2(100, "Player 2")
    player3 = CPUPlayer3(100, "Player 3")
    player4 = CPUPlayer2(100, "Player 4")
    player5 = CPUPlayer2(100, "Player 5")
    print()
    print()
    play_holdem([player1, player2, player3, player4, player5], 5, 10)