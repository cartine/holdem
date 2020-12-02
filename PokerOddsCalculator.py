from Peter7CardBestHandRemastered2 import *
from HeadsupGame import *
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

    def current_score(self, score_results):
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
    card_score = first_hand.current_score(score_results)
    hit_percent = first_hand.hit_percent(score_results, card_score)
    raise_break_even_percent = first_hand.raise_break_even_percent(50, 10)
    call_break_even_percent = first_hand.call_break_even_percent(50, raise_break_even_percent)
    print(score_results)
    print(card_score)
    print(hit_percent)
    print(call_break_even_percent)
    print(raise_break_even_percent)