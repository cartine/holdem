# from poker5 import get_deck
from game import Player

if __name__ == "__main__":

    players = []
    players.append(Player(0, "Player 1"))
    players.append(Player(0, "Player 2"))
    players.append(Player(0, "Player 3"))
    players.append(Player(0, "Player 4"))
    players.append(Player(0, "Player 5"))

    # n = len(players)
    #
    # deck = get_deck(shuffled=True)
    # for i in range(0, n):
    #     players[i].HAND = deck[2*i:(2*i)+2]
    # shared_cards = deck[n*2:(n*2)+5]
    #
    # print(f'deck: {deck}')
    # for player in players:
    #     print(f'player: {player.NAME}, hand: {player.HAND}')
    # print(f'shared cards: {shared_cards}')

    p = players.copy()
    p.pop(2)
    print(players)
    print(p)
