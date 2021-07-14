from multiprocessing import Pool
from Peter7CardBestHandRemastered2 import *
import numpy as np


def monte_carlo_pre_flop(hand, num_of_opponents):
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
    return win_percent


def monte_carlo_post_flop(hand, shared_cards, num_of_opponents):
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
    return win_percent


def retrying(hand, shared_cards, num_of_opponents):
    deck2 = deck
    deck3 = []
    showing_cards = hand + shared_cards
    results = []
    for i in showing_cards:
        if i in deck2:
            deck2.remove(i)
    for j in range(0, 300000):
        if len(deck2) < 20:
            deck2 += deck3
            deck3 = []
        shared_cards2 = shared_cards
        random.shuffle(deck2)
        shared_cards2 += deck2[:5-len(shared_cards2)]
        deck3 += deck2[:5-len(shared_cards2)]
        del deck2[:5-len(shared_cards2)]
        opponents_cards = deck2[-(num_of_opponents*2):]
        deck3 += deck2[-(num_of_opponents*2):]
        del deck2[-(num_of_opponents*2):]
        self_score = best_hands(hand[0][0], hand[1][0], shared_cards2[0][0], shared_cards2[1][0], shared_cards2[2][0], shared_cards2[3][0], shared_cards2[4][0], hand[0][1], hand[1][1], shared_cards2[0][1], shared_cards2[1][1], shared_cards2[2][1], shared_cards2[3][1], shared_cards2[4][1])
        for i in range(0, num_of_opponents):
            current_best = Score(Ranking.HIGH_CARD, [7, 5, 4, 3, 2])
            current_score = best_hands(opponents_cards[i][0], opponents_cards[-(i+1)][0], shared_cards2[0][0], shared_cards2[1][0], shared_cards2[2][0], shared_cards2[3][0], shared_cards2[4][0], opponents_cards[i][1], opponents_cards[-(i+1)][1], shared_cards2[0][1], shared_cards2[1][1], shared_cards2[2][1], shared_cards2[3][1], shared_cards2[4][1])
            if current_best.compare(current_score) < 0:
                current_best = current_score
        if self_score.compare(current_best) > 0:
            results.append(True)
        else:
            results.append(False)
        # print(type(current_best))
    wins = np.array(results)
    win_percent = np.mean(wins == True)
    win_percent = win_percent * 100
    return win_percent

def multi_processing(betting_round, params):
    pool = Pool(processes=4)
    th1 = pool.apply_async(betting_round, params)
    th2 = pool.apply_async(betting_round, params)
    th3 = pool.apply_async(betting_round, params)
    th4 = pool.apply_async(betting_round, params)
    # th5 = pool.apply_async(betting_round, params)
    # th6 = pool.apply_async(betting_round, params)
    # th7 = pool.apply_async(betting_round, params)
    # th8 = pool.apply_async(betting_round, params)
    # print(th1.get())
    pool.close()
    pool.join()
    p8 = ((th1.get() + th2.get() + th3.get() + th4.get())/4)
    return p8

if __name__ == '__main__':
    args = [[('T', 'C'), (9, 'C')], [(9, 'S'), ('Q', 'C'), (7, 'C')], 1]
    # print(retrying(*args))
    print(multi_processing(monte_carlo_post_flop, [*args]))