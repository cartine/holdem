from PeterPokerBot3 import *
import itertools
import threading
import time


def monte_carlo_pre_flop(hand, num_of_opponents):
    print(hand)
    deck2 = deck
    results = []
    win = []
    my_pips = []
    my_suits = []
    for x in hand:
        if x in deck2:
            deck2.remove(x)
        my_pips.append(x[0])
        my_suits.append(x[1])
    for j in range(0, 3000):
        random.shuffle(deck2)
        opponents_beaten = 0
        ties = 0
        i = 0
        hands = []
        for k in range(0, num_of_opponents):
            hands.append(deck2[i:i + 2])
            i = i + 2
        shared_cards = deck2[-5:]
        for e in shared_cards:
            my_pips.append(e[0])
            my_suits.append(e[1])
        current_score = best_hands(*my_pips, *my_suits)
        del my_pips[-5:]
        del my_suits[-5:]
        pips = []
        suits = []
        for x in shared_cards:
            pips.append(x[0])
            suits.append(x[1])
        for e in hands:
            score = 0
            x = e[0]
            y = e[1]
            pips.append(x[0])
            pips.append(y[0])
            suits.append(x[1])
            suits.append(y[1])
            score = best_hands(*pips, *suits)
            c = current_score.compare(score)
            if c > 0:
                opponents_beaten += 1
            if c == 0:
                ties += 1
            del pips[-2:]
            del suits[-2:]
        if opponents_beaten == (num_of_opponents - ties):
            for i in range(0, (num_of_opponents - ties)):
                win.append(True)
        else:
            for i in range(0, num_of_opponents):
                win.append(False)
    wins = np.array(win)
    win_percent = np.mean(wins == True)
    win_percent = win_percent * 100
    print(win_percent)
    return win_percent

def monte_carlo_post_flop(hand, shared_cards, num_of_opponents):
    print(hand) # todo test accuracy
    deck2 = deck
    results = []
    win = []
    my_pips = []
    my_suits = []
    for x in hand:
        if x in deck2:
            deck2.remove(x)
        my_pips.append(x[0])
        my_suits.append(x[1])
    for x in shared_cards:
        if x in deck2:
            deck2.remove(x)
    for j in range(0, 3000):
        random.shuffle(deck2)
        oppenents_beaten = 0
        ties = 0
        i = 0
        hands = []
        for k in range(0, num_of_opponents):
            hands.append(deck2[i:i + 2])
            i = i + 2
        if len(shared_cards) < 5:
            shared_cards2 = shared_cards + deck2[-(5 - len(shared_cards)):]
        else:
            shared_cards2 = shared_cards
        for e in shared_cards2:
            my_pips.append(e[0])
            my_suits.append(e[1])
        current_score = best_hands(*my_pips, *my_suits)
        del my_pips[-5:]
        del my_suits[-5:]
        pips = []
        suits = []
        for x in shared_cards2:
            pips.append(x[0])
            suits.append(x[1])
        for e in hands:
            score = 0
            x = e[0]
            y = e[1]
            pips.append(x[0])
            pips.append(y[0])
            suits.append(x[1])
            suits.append(y[1])
            score = best_hands(*pips, *suits)
            c = current_score.compare(score)
            if c > 0:
                oppenents_beaten += 1
            if c == 0:
                ties += 1
            del pips[-2:]
            del suits[-2:]
        if oppenents_beaten == (num_of_opponents - ties):
            for i in range(0, (num_of_opponents - ties)):
                win.append(True)
        else:
            for i in range(0, num_of_opponents):
                win.append(False)
    wins = np.array(win)
    win_percent = np.mean(wins == True)
    win_percent = win_percent * 100
    print(win_percent)
    return win_percent


if __name__ == '__main__':
    start = time.time()
    for x in range(0, 8):
        doopdoop = random.sample(deck, 5)
        monte_carlo_post_flop(doopdoop[:2], doopdoop[2:5], 4)
    end = time.time()
    print('Time taken in seconds -', end - start)