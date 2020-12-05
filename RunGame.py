from HeadsupGame import *
from PeterPokerBot2 import *
from PeterPokerBot3 import *

if __name__ == '__main__':
    hand_numbers = []
    for x in range(0, 1000):
        player1 = CPUPlayer2(1000, "Player 1")
        from PeterPokerBot2 import CPUPlayer2
        player2 = CPUPlayer3(1000, "Player 2")
        print()
        print()
        hand_numbers.append(play_holdem(player1, player2, 5, 10))
    print(hand_numbers)
    np.array(hand_numbers)
    hn_mean = np.mean(hand_numbers)
    print(hn_mean)