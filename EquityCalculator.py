from multiprocessing import Pool
from Peter7CardBestHandRemastered2 import *
from PeterPokerBot3 import *


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


def multi_processing(betting_round, params):
    pool = Pool(processes=4)
    th1 = pool.apply_async(betting_round, [params])
    th2 = pool.apply_async(betting_round, [params])
    th3 = pool.apply_async(betting_round, [params])
    th4 = pool.apply_async(betting_round, [params])
    th5 = pool.apply_async(betting_round, [params])
    th6 = pool.apply_async(betting_round, [params])
    th7 = pool.apply_async(betting_round, [params])
    th8 = pool.apply_async(betting_round, [params])
    pool.close()
    pool.join()
    target = 0
    # p1 = th1.get() - target
    # p2 = ((th1.get() + th2.get())/2) - target
    # p3 = ((th1.get() + th2.get() + th3.get())/3) - target
    # p4 = ((th1.get() + th2.get() + th3.get() + th4.get())/4) - target
    # p5 = ((th1.get() + th2.get() + th3.get() + th4.get() + th5.get())/5) - target
    # p6 = ((th1.get() + th2.get() + th3.get() + th4.get() + th5.get() + th6.get())/6) - target
    # p7 = ((th1.get() + th2.get() + th3.get() + th4.get() + th5.get() + th6.get() + th7.get())/7) - target
    p8 = ((th1.get() + th2.get() + th3.get() + th4.get() + th5.get() + th6.get() + th7.get() + th8.get())/8)
    return p8
