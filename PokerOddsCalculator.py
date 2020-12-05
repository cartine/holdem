from Peter7CardBestHandRemastered2 import *
from HeadsupGame import *
from PeterBestHand import *
import itertools
import numpy as np
import pandas as pd


class DataFrameWrapper:
    def __init__(self, the_table):
        self.CARDS = None
        self.POT = None
        self.SCORE_RESULTS = None

    def __str__(self):
        return str(self.CARDS) + ", " + str(self.POT)

    def calculator(self, cards):
        print(cards)
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

    def current_score(self, cards):
        pips1 = []
        suits1 = []
        for part in cards:
            pips1.append(part[0])
            suits1.append(part[1])
        current_score = Best_Hand(*pips1, *suits1)
        return current_score

    def betting_value_results(self, cards, current_score):
        results = []
        argpip = []
        argsuit = []
        deck2 = deck
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
        results = np.array(results)
        unique_results = []
        for x in results:
            if x not in unique_results:
                unique_results.append(x)
        if current_score not in unique_results:
            unique_results.append(str(current_score))
        results = list(unique_results)
        print(results)
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
        current_score = str(current_score).split(',')
        current_score[1] = current_score[1].split('[')[1]
        current_score[5] = current_score[5].split(']')[0]
        current_score1 = [current_score[0]]
        current_score2 = [int(e) for e in current_score[1:]]
        current_score = current_score1
        current_score.append(current_score2)
        results['Value'] = results["Score"].apply(lambda x: getattr(Ranking, x).value)
        results.sort_values(by=['Value', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'], ascending=False, inplace=True)
        results = results.reset_index(drop=True)
        # self.SCORE_RESULTS = score_results
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
        value_betting_index = score_score.index.max()
        results_index = results.index.max()
        value_betting_index += 1
        results_index += 1
        value_betting_percent = (value_betting_index / results_index) * 100
        return value_betting_percent

    def card_score(self, cards):
        card_score = score_results.Value.min()
        return card_score

    def hit_percent(self, score_results, card_score):
        hit_percent = score_results[score_results['Value'] > card_score]
        hit_percent = hit_percent.Percent.sum()
        return hit_percent

    def call_break_even_percent(self, pot, active_pot):
        break_even_percent = active_pot / (active_pot + pot)
        break_even_percent *= 100
        return break_even_percent

    def raise_break_even_percent(self, pot, hit_percent):
        raise_amount = ((hit_percent/100) * pot * -1)/((hit_percent/100) - 1)
        return raise_amount


if __name__ == '__main__':
    first_hand = DataFrameWrapper(Table)
    score_results = first_hand.calculator(random.sample(deck, 5))
    current_score = first_hand.current_score(random.sample(deck, 5))
    value_betting_percent = first_hand.betting_value_results(random.sample(deck, 5), current_score)
    card_score = first_hand.card_score(score_results)
    hit_percent = first_hand.hit_percent(score_results, card_score)
    raise_break_even_percent = first_hand.raise_break_even_percent(50, 10)
    call_break_even_percent = first_hand.call_break_even_percent(50, raise_break_even_percent)
    print(score_results)
    print(current_score)
    print(value_betting_percent)
    print(card_score)
    print(hit_percent)
    print(call_break_even_percent)
    print(raise_break_even_percent)