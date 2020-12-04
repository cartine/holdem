# import pyautogui
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# if __name__ == '__main__':
#     i = Image.open('10ofClubs.png')
#     iar = np.asarray(i)
#     plt.imshow(iar)
#     print(iar)
#
#
#
# pyautogui.hotkey('alt', 'tab')
# pyautogui.moveTo(100, 100)
from PeterPokerGame import *
from PokerOddsCalculator import DataFrameWrapper
from game import *


class CPUPlayer2(Player):

    def decide(self, the_table, betting_round):
        nums1 = []
        shapes = []
        raise_amount = 0
        for e in self.HAND:
            nums1.append(e[0])
            shapes.append(e[1])
        nums2 = [face_cards(num) for num in nums1]
        nums = sorted(nums2, reverse=True)
        if betting_round == BettingRound.PRE_FLOP:
            if the_table.ACTIVE == 0:
                if nums[0] == nums[1]:
                    if nums[0] > 6:
                        if nums[0] == 7:
                            raise_amount = random.randint(the_table.POT/4, (the_table.POT/2))
                        if nums[0] == 8:
                            raise_amount = random.randint((the_table.POT/4) + 1, (the_table.POT/2) + 3)
                        if nums[0] == 9:
                            raise_amount = random.randint((the_table.POT/4) + 2, (the_table.POT/8) * 5)
                        if nums[0] == 10:
                            raise_amount = random.randint((the_table.POT/4) + 3, (the_table.POT/4) * 3)
                        if nums[0] == 11:
                            raise_amount = random.randint((the_table.POT/2), (the_table.POT/8) * 7)
                        if nums[0] == 12:
                            raise_amount = random.randint((the_table.POT/2), the_table.POT)
                        if nums[0] == 13:
                            raise_amount = random.randint((the_table.POT/2), the_table.POT)
                        if nums[0] == 14:
                            raise_amount = random.randint((the_table.POT/2), the_table.POT)
                        return Choice.RAISE, raise_amount
                    else:
                        return Choice.CALL, 0
                else:
                    if nums[0] >= 13:
                        if shapes[0] == shapes[1]:
                            if nums[0] == 14:
                                if nums[1] == 10:
                                    raise_amount = random.randint((the_table.POT/4), (the_table.POT/2))
                                if 13 > nums[1] > 10:
                                    raise_amount = random.randint((the_table.POT/4) + 1, (the_table.POT/2) + 1)
                                if nums[1] == 13:
                                    raise_amount = random.randint((the_table.POT/4) + 1, (the_table.POT/2) + 2)
                                return Choice.RAISE, raise_amount
                            elif nums[0] == 13:
                                if nums[1] == 12:
                                    raise_amount = random.randint((the_table.POT/4) - 1, (the_table.POT/2) - 1)
                                    return Choice.RAISE, raise_amount
                                else:
                                    return Choice.CALL, 0
                            else:
                                return Choice.CALL, 0
                        else:
                            if nums[0] == 14:
                                if 13 > nums[1] > 10:
                                    raise_amount = random.randint((the_table.POT/4) - 1, (the_table.POT/2))
                                if nums[1] == 13:
                                    raise_amount = random.randint((the_table.POT/4) + 1, (the_table.POT/2) + 1)
                                return Choice.RAISE, raise_amount
                            else:
                                return Choice.CALL, 0
                    else:
                        return Choice.CALL, 0
            else:
                if nums[0] == nums[1]:
                    if nums[0] > 6:
                        if nums[0] == 7:
                            raise_amount = random.randint(the_table.POT / 4, (the_table.POT / 2))
                        if nums[0] == 8:
                            raise_amount = random.randint((the_table.POT / 4) + 1, (the_table.POT / 2) + 3)
                        if nums[0] == 9:
                            raise_amount = random.randint((the_table.POT / 4) + 2, (the_table.POT / 8) * 5)
                        if nums[0] == 10:
                            raise_amount = random.randint((the_table.POT / 4) + 3, (the_table.POT / 4) * 3)
                        if nums[0] == 11:
                            raise_amount = random.randint((the_table.POT / 2), (the_table.POT / 8) * 7)
                        if nums[0] == 12:
                            raise_amount = random.randint((the_table.POT / 2), the_table.POT)
                        if nums[0] == 13:
                            raise_amount = random.randint((the_table.POT / 2), the_table.POT)
                        if nums[0] == 14:
                            raise_amount = random.randint((the_table.POT / 2), the_table.POT)
                        return Choice.RAISE, raise_amount
                    else:
                        if (nums[0] == 5) or (nums[0] == 6):
                            return Choice.CALL, 0
                        else:
                            return Choice.FOLD, 0
                else:
                    if shapes[0] == shapes[1]:
                        if nums[0] == 14:
                            if nums[1] > 9:
                                if nums[1] == 10:
                                    raise_amount = random.randint((the_table.POT / 4), (the_table.POT / 2))
                                if 13 > nums[1] > 10:
                                    raise_amount = random.randint((the_table.POT / 4) + 1,
                                                                  (the_table.POT / 2) + 1)
                                if nums[1] == 13:
                                    raise_amount = random.randint((the_table.POT / 4) + 1,
                                                                  (the_table.POT / 2) + 2)
                                return Choice.RAISE, raise_amount
                            else:
                                if (nums[1] == 9) or (nums[1] == 8) or (nums[1] == 7) or (nums[1] == 5):
                                    return Choice.CALL, 0
                                else:
                                    return Choice.FOLD, 0
                        elif nums[0] == 13:
                            if nums[1] == 12:
                                raise_amount = random.randint((the_table.POT / 4) - 1,
                                                              (the_table.POT / 2) - 1)
                                return Choice.RAISE, raise_amount
                            else:
                                if (nums[1] == 9) or (nums[1] == 10) or (nums[1] == 11):
                                    return Choice.CALL, 0
                                else:
                                    return Choice.FOLD, 0
                        elif nums[0] == 12:
                            if (nums[1] == 11) or (nums[1] == 12):
                                return Choice.CALL, 0
                            else:
                                return Choice.FOLD, 0
                        else:
                            return Choice.FOLD, 0
                    else:
                        if nums[0] == 14:
                            if nums[1] > 10:
                                if 13 > nums[1] > 10:
                                    raise_amount = random.randint((the_table.POT / 4) - 1, (the_table.POT / 2))
                                if nums[1] == 13:
                                    raise_amount = random.randint((the_table.POT / 4) + 1,
                                                                  (the_table.POT / 2) + 1)
                                return Choice.RAISE, raise_amount
                            elif nums[1] == 10:
                                return Choice.CALL, 0
                            else:
                                return Choice.FOLD, 0
                        elif nums[0] == 13:
                            if nums[1] > 9:
                                return Choice.CALL, 0
                            else:
                                return Choice.FOLD, 0
                        else:
                            return Choice.FOLD, 0
        if betting_round == BettingRound.POST_FLOP:
            hand = []
            for e in the_table.SHARED_CARDS_SHOWING:
                hand.append(e)
            for e in self.HAND:
                hand.append(e)
            hand_data = DataFrameWrapper(hand)
            if hand_data.current_score(hand_data.calculator(hand)) >= 3:
                raise_amount = random.randint((the_table.POT/2), the_table.POT)
                return Choice.RAISE, raise_amount
            else:
                if the_table.ACTIVE == 0:
                    raise_amount = hand_data.raise_break_even_percent(the_table.POT, hand_data.hit_percent(hand_data.calculator(hand), hand_data.current_score(hand_data.calculator(hand))))
                    if raise_amount > 0:
                        return Choice.RAISE, raise_amount
                    else:
                        return Choice.CALL, 0
                else:
                    break_even_percent = hand_data.call_break_even_percent(the_table.POT, the_table.ACTIVE)
                    hit_percent = hand_data.hit_percent(hand_data.calculator(hand), hand_data.current_score(hand_data.calculator(hand)))
                    if hit_percent > break_even_percent:
                        return Choice.CALL, 0
                    else:
                        return Choice.FOLD, 0
        if betting_round is BettingRound.POST_TURN:
            hand = []
            for e in the_table.SHARED_CARDS_SHOWING:
                hand.append(e)
            for e in self.HAND:
                hand.append(e)
            hand_data = DataFrameWrapper(hand)
            if hand_data.current_score(hand_data.calculator(hand)) >= 3:
                raise_amount = random.randint((the_table.POT/2), the_table.POT)
                return Choice.RAISE, raise_amount
            else:
                if the_table.ACTIVE == 0:
                    raise_amount = hand_data.raise_break_even_percent(the_table.POT, hand_data.hit_percent(hand_data.calculator(hand), hand_data.current_score(hand_data.calculator(hand))))
                    if raise_amount > 0:
                        return Choice.RAISE, raise_amount
                    else:
                        return Choice.CALL, 0
                else:
                    break_even_percent = hand_data.call_break_even_percent(the_table.POT, the_table.ACTIVE)
                    hit_percent = hand_data.hit_percent(hand_data.calculator(hand), hand_data.current_score(hand_data.calculator(hand)))
                    if hit_percent > break_even_percent:
                        return Choice.CALL, 0
                    else:
                        return Choice.FOLD, 0
        if betting_round is BettingRound.POST_RIVER:
            hand = []
            for e in the_table.SHARED_CARDS_SHOWING:
                hand.append(e)
            for e in self.HAND:
                hand.append(e)
            hand_data = DataFrameWrapper(hand)
            hit_score = hand_data.current_score(hand_data.calculator(hand))
            if hit_score >= 3:
                raise_amount = random.randint((the_table.POT/2), (the_table.POT/4) * hit_score)
                return Choice.RAISE, raise_amount
            else:
                return Choice.FOLD, 0
        return Choice.FOLD, 0


if __name__ == '__main__':
    CPU2 = CPUPlayer2(1000, 'CPU2')
    player_1 = CPU
    player_2 = CPU2
    play2(player_1, player_2)
    # while CPU.CHIPS and CPU2.CHIPS > 0:
    #     print()
    #     play2(player_1, player_2)
    #     y = player_1
    #     player_1 = player_2
    #     player_2 = y
