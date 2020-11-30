from Peter7CardBestHandRemastered2 import *
import itertools
import numpy as np
import pandas as pd
from ordered_enum import OrderedEnum


def calculator(args):
    print(args)
    results = []
    argpip = []
    argsuit = []
    deck2 = deck
    if len(args) == 5:
        for arg in args:
            if arg in deck2: deck2.remove(arg)
        holes = list(itertools.combinations(deck2, 2))
        for x in holes:
            for e in x:
                list(e)
                argpip.append(e[0])
                argsuit.append(e[1])
            for arg in args:
                argpip.append(arg[0])
                argsuit.append(arg[1])
            results.append(str(best_hands(*argpip, *argsuit)))
            for arg in args:
                argpip.remove(arg[0])
                argsuit.remove(arg[1])
            for e in x:
                argpip.remove(e[0])
                argsuit.remove(e[1])
    if len(args) == 6:
        for arg in args:
            if arg in deck2: deck2.remove(arg)
        hole = deck2
        for x in args:
            argpip.append(x[0])
            argsuit.append((x[1]))
        for e in hole:
            argpip.append(e[0])
            argsuit.append((e[1]))
            results.append(str(best_hands(*argpip, *argsuit)))
            argpip.remove(e[0])
            argsuit.remove(e[1])
    if len(args) == 7:
        for x in args:
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
    # print(hand_results)
    score_results = hand_results.groupby('Score').Percent.sum().reset_index()
    score_results.sort_values(by='Percent', inplace=True, ignore_index=True)
    score_results['Percent'] *= 100
    score_results["Value"] = score_results["Score"].apply(lambda x: getattr(Ranking, x).value)
    score_results2 = score_results.sort_values(by='Value')
    return score_results


if __name__ == '__main__':
    print(calculator(random.sample(deck, 5)))