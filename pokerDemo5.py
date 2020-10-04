import poker5


def demo():
    deck = poker5.get_deck()
    player1 = deck[0:2]
    player2 = deck[2:4]
    shared = deck[4:9]

    print("Player1's cards are:", player1)
    print("Player2's cards are:", player2)
    print("The shared cards are: ", shared)
    print()
    score1 = poker5.get_score(player1 + shared)
    score2 = poker5.get_score(player2 + shared)
    print("Player1's score: ", score1)
    print("Player2's score: ", score2)
    c = score1.compare(score2)
    if c > 0:
        print("Player1 wins!")
    elif c < 0:
        print("Player2 wins!")
    elif c == 0:
        print("It is a tie!")


if __name__ == '__main__':
    demo()
