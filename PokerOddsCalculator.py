from PeterBestHand6 import *
from PeterBestHand import *
from OpponentsRanges import *
import itertools
import numpy as np
import pandas as pd
import math


class DataFrameWrapper:
    def __init__(self, the_table):
        self.CARDS = None
        self.POT = None
        self.SCORE_RESULTS = None

    def __str__(self):
        return str(self.CARDS) + ", " + str(self.POT)

    def calculator(self, cards):
        results = []
        argpip = []
        argsuit = []
        deck2 = deck
        if len(cards) == 5:
            for arg in cards:
                if arg in deck2: deck2.remove(arg)
            holes = list(itertools.combinations(deck2, 2))
            for x in holes:
                for e in x:
                    list(e)
                    argpip.append(e[0])
                    argsuit.append(e[1])
                for arg in cards:
                    argpip.append(arg[0])
                    argsuit.append(arg[1])
                results.append(str(best_hands(*argpip, *argsuit)))
                for arg in cards:
                    argpip.remove(arg[0])
                    argsuit.remove(arg[1])
                for e in x:
                    argpip.remove(e[0])
                    argsuit.remove(e[1])
        if len(cards) == 6:
            for arg in cards:
                if arg in deck2: deck2.remove(arg)
            hole = deck2
            for x in cards:
                argpip.append(x[0])
                argsuit.append((x[1]))
            for e in hole:
                argpip.append(e[0])
                argsuit.append((e[1]))
                results.append(str(best_hands(*argpip, *argsuit)))
                argpip.remove(e[0])
                argsuit.remove(e[1])
        if len(cards) == 7:
            for x in cards:
                argpip.append(x[0])
                argsuit.append((x[1]))
            results.append(str(best_hands(*argpip, *argsuit)))
        results = np.array(results)
        unique_results = []
        unique_results_percent = []
        for x in results:
            if x not in unique_results:
                unique_results.append(x)
        for x in unique_results:
            unique_results_percent.append(np.mean(x == results))
        results = list(unique_results)
        results1 = [x.split(',', 1)[0] for x in unique_results]
        results2 = [x.split(',', 1)[1] for x in unique_results]
        results = list(zip(results1, results2, unique_results_percent))
        results = sorted(results, key=lambda per: per[1], reverse=True)
        results = pd.DataFrame(results, columns=['Score', 'Hand', 'Percent'])
        hand_results = results.groupby(['Score', 'Hand'])['Percent'].mean().reset_index()
        score_results = hand_results.groupby('Score').Percent.sum().reset_index()
        score_results.sort_values(by='Percent', inplace=True, ignore_index=True)
        score_results['Percent'] *= 100
        score_results["Value"] = score_results["Score"].apply(lambda x: getattr(Ranking, x).value)
        self.SCORE_RESULTS = score_results
        return score_results

    def current_score5(self, cards):
        pips1 = []
        suits1 = []
        for part in cards:
            pips1.append(part[0])
            suits1.append(part[1])
        current_score = Best_Hand(*pips1, *suits1)
        return current_score

    def current_score6(self, cards):
        argpip = []
        argsuit = []
        for x in cards:
            argpip.append(x[0])
            argsuit.append((x[1]))
        current_score = best_hands6(*argpip, *argsuit)
        return current_score

    def current_score7(self, cards):
        pips1 = []
        suits1 = []
        for part in cards:
            pips1.append(part[0])
            suits1.append(part[1])
        current_score = best_hands(*pips1, *suits1)
        return current_score

    def betting_value_index(self, cards, current_score, opp_range):
        results = []
        argpip = []
        argsuit = []
        hand = []
        deck2 = deck
        if len(cards) == 3:
            for arg in cards:
                if arg in deck2: deck2.remove(arg)
            holes = list(itertools.combinations(deck2, 2))
            if opp_range != 'one_hundred_percent':
                for e, x in holes:
                    argpip = []
                    argsuit = []
                    hand = []
                    argpip.append(e[0])
                    argsuit.append(e[1])
                    argpip.append(x[0])
                    argsuit.append(x[1])
                    argpip = sorted(argpip, key= lambda x: int(face_cards(x)), reverse=True)
                    if argsuit[0] == argsuit[1]:
                        hand = str(pips[0]) + str(pips[1]) + 's'
                    else:
                        hand = pips[0] + pips[1]
                        hand = str(hand)
                    if hand in opp_range:
                        holes.remove(e)
                    argpip.delete[-2:]
                    argsuit.delete[-2:]
                    hand.delete[0]
            for x in holes:
                argpip = []
                argsuit = []
                hand = []
                for e in x:
                    list(e)
                    argpip.append(e[0])
                    argsuit.append(e[1])
                for arg in cards:
                    argpip.append(arg[0])
                    argsuit.append(arg[1])
                results.append(str(best_hands(*argpip, *argsuit)))
                for arg in cards:
                    argpip.remove(arg[0])
                    argsuit.remove(arg[1])
                for e in x:
                    argpip.remove(e[0])
                    argsuit.remove(e[1])
        if len(cards) == 4:
            for arg in cards:
                if arg in deck2: deck2.remove(arg)
            holes = list(itertools.combinations(deck2, 2))
            if opp_range != 'one_hundred_percent':
                for e, x in holes:
                    argpip = []
                    argsuit = []
                    hand = []
                    argpip.append(e[0])
                    argsuit.append(e[1])
                    argpip.append(x[0])
                    argsuit.append(x[1])
                    argpip = sorted(argpip, key= lambda x: int(face_cards(x)), reverse=True)
                    if argsuit[0] == argsuit[1]:
                        hand = str(pips[0]) + str(pips[1]) + 's'
                    else:
                        hand = pips[0] + pips[1]
                        hand = str(hand)
                    if hand in opp_range:
                        holes.remove(e)
                    del argpip
                    del argsuit
                    del hand
            for x in holes:
                argpip = []
                argsuit = []
                hand = []
                for e in x:
                    list(e)
                    argpip.append(e[0])
                    argsuit.append(e[1])
                for arg in cards:
                    argpip.append(arg[0])
                    argsuit.append(arg[1])
                results.append(str(best_hands6(*argpip, *argsuit)))
                for arg in cards:
                    argpip.remove(arg[0])
                    argsuit.remove(arg[1])
                for e in x:
                    argpip.remove(e[0])
                    argsuit.remove(e[1])
        if len(cards) == 5:
            for arg in cards:
                if arg in deck2: deck2.remove(arg)
            holes = list(itertools.combinations(deck2, 2))
            if opp_range != 'one_hundred_percent':
                for e, x in holes:
                    argpip = []
                    argsuit = []
                    hand = []
                    argpip.append(e[0])
                    argsuit.append(e[1])
                    argpip.append(x[0])
                    argsuit.append(x[1])
                    argpip = sorted(argpip, key= lambda x: int(face_cards(x)), reverse=True)
                    if argsuit[0] == argsuit[1]:
                        hand = str(pips[0]) + str(pips[1]) + 's'
                    else:
                        hand = pips[0] + pips[1]
                        hand = str(hand)
                    if hand in opp_range:
                        holes.remove(e)
                    del argpip
                    del argsuit
                    del hand
            for x in holes:
                argpip = []
                argsuit = []
                hand = []
                for e in x:
                    list(e)
                    argpip.append(e[0])
                    argsuit.append(e[1])
                for arg in cards:
                    argpip.append(arg[0])
                    argsuit.append(arg[1])
                results.append(str(best_hands(*argpip, *argsuit)))
                for arg in cards:
                    argpip.remove(arg[0])
                    argsuit.remove(arg[1])
                for e in x:
                    argpip.remove(e[0])
                    argsuit.remove(e[1])
        if str(current_score) not in results:
            results.append(str(current_score))
        results = list(results)
        results1 = [x.split(',', 1)[0] for x in results]
        results2 = [x.split(',', 1)[1] for x in results]
        hand_pip1 = [x.split(',', 1)[0] for x in results2]
        hand_pip1 = [x.split('[', 1)[1] for x in hand_pip1]
        hand_pip2 = [x.split(',', 2)[1] for x in results2]
        hand_pip3 = [x.split(',', 3)[2] for x in results2]
        hand_pip4 = [x.split(',', 4)[3] for x in results2]
        hand_pip5 = [x.split(',', 5)[4] for x in results2]
        hand_pip5 = [x.split(']', 1)[0] for x in hand_pip5]
        hand_pip1 = [int(e.strip()) for e in hand_pip1]
        hand_pip2 = [int(e.strip()) for e in hand_pip2]
        hand_pip3 = [int(e.strip()) for e in hand_pip3]
        hand_pip4 = [int(e.strip()) for e in hand_pip4]
        hand_pip5 = [int(e.strip()) for e in hand_pip5]
        results = pd.DataFrame(results1, columns=['Score'])
        results['Card1'] = hand_pip1
        results['Card2'] = hand_pip2
        results['Card3'] = hand_pip3
        results['Card4'] = hand_pip4
        results['Card5'] = hand_pip5
        results['Value'] = results["Score"].apply(lambda x: getattr(Ranking, x).value)
        results.sort_values(by=['Value', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'], ascending=False, inplace=True)
        results = results.reset_index(drop=True)
        return results

    def betting_value_results(self, current_score, results):
        current_score = str(current_score).split(',')
        current_score[1] = current_score[1].split('[')[1]
        current_score[5] = current_score[5].split(']')[0]
        current_score1 = [current_score[0]]
        current_score2 = [int(e) for e in current_score[1:]]
        current_score = current_score1
        current_score.append(current_score2)
        score_score = results.loc[results.Score == current_score[0]]
        if len(score_score) > 1:
            score_score = score_score.loc[score_score.Card1 == current_score2[0]]
            if len(score_score) > 1:
                score_score = score_score.loc[score_score.Card2 == current_score2[1]]
                if len(score_score) > 1:
                    score_score = score_score.loc[score_score.Card3 == current_score2[2]]
                    if len(score_score) > 1:
                        score_score = score_score.loc[score_score.Card4 == current_score2[3]]
                        if len(score_score) > 1:
                            score_score = score_score.loc[score_score.Card5 == current_score2[4]]
        value_betting_index = score_score.index.min()
        results_index = results.index.max()
        value_betting_index += 1
        results_index += 1
        value_betting_percent = (value_betting_index / results_index) * 100
        return value_betting_percent

    def hit_percent(self, score_results):
        hit_percent = score_results[score_results['Value'] >= 2]
        hit_percent = hit_percent.Percent.sum()
        return hit_percent

    def call_break_even_percent(self, pot, active_pot):
        break_even_percent = active_pot / (active_pot + pot)
        break_even_percent *= 100
        return break_even_percent

    def raise_break_even_percent(self, pot, hit_percent):
        if hit_percent > 99:
            return 0
        raise_amount = abs(math.floor((hit_percent/100) * pot * -1)/((hit_percent/100) - 1))
        return raise_amount


if __name__ == '__main__':
    # pd.set_option("display.max_rows", None, "display.max_columns", None)
    first_hand = DataFrameWrapper(Table)
    hand = random.sample(deck, 7)
    score_results = first_hand.calculator(hand)
    current_score5 = first_hand.current_score5(random.sample(deck, 5))
    current_score6 = first_hand.current_score6(random.sample(deck, 6))
    current_score7 = first_hand.current_score7(hand)
    value_betting_index = first_hand.betting_value_index(hand[:5], current_score7, thirty_three_percent)
    value_betting_percent = first_hand.betting_value_results(current_score7, value_betting_index)
    hit_percent = first_hand.hit_percent(score_results)
    raise_break_even_percent = first_hand.raise_break_even_percent(50, 10)
    call_break_even_percent = first_hand.call_break_even_percent(50, raise_break_even_percent)
    print(hand)
    # print(score_results)
    # print(current_score5)
    # print(current_score6)
    print(current_score7)
    print(value_betting_percent)
    print(value_betting_index)
    # print(hit_percent)
    # print(call_break_even_percent)
    # print(raise_break_even_percent)