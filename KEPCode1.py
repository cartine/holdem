import poker5
def twoPlayerRiverOddsCalculator(YourCard1, YourCard2, Upturned1, Upturned2, Upturned3, Upturned4, Upturned5):
    deck = poker5.get_deck()
    YourHand = [YourCard1, YourCard2]
    deck.remove(YourCard1)
    deck.remove(YourCard2)
    upturned = [Upturned1, Upturned2, Upturned3, Upturned4, Upturned5]

    deck.remove(Upturned1)
    deck.remove(Upturned2)
    deck.remove(Upturned3)
    deck.remove(Upturned4)
    deck.remove(Upturned5)

    OpponetsHand = []
    win = 0
    lose = 0
    tie = 0
    x = 0
    y = 1

    while True:
        OpponetsHand = [deck[x],deck[y]]
        score1 = poker5.get_score(YourHand + upturned)
        score2 = poker5.get_score(OpponetsHand + upturned)
        c = score1.compare(score2)
        if c > 0:
            win += 1
        elif c < 0:
            lose += 1
        else:
            tie += 1

        if y != len(deck) - 1:
            y += 1
        else:
            if x != len(deck) - 2:
                x += 1
                y = x + 1
            else:
                break


    print('win')
    print(win)
    print('tie')
    print(tie)
    print('lose')
    print(lose)

twoPlayerRiverOddsCalculator('AH', 'KH', 'QH', 'JH', 'TH', '9H', '8H')
