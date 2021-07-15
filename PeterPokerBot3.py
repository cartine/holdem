from PeterPokerGame import *
from PokerOddsCalculator import DataFrameWrapper
from multiplayer_holdem_game import *
from game2 import *
from StartingHandsBot3 import *
from OpponentsRanges import *
from EquityCalculator import *
import math
import sys


class CPUPlayer3(Player):
    def decide(self, the_table, betting_round, call_amount, seats, your_index):
        try:
            if self.CHIPS == 0:
                self.ALL_IN is True
            num_seats = len(seats)
            pos = 0
            if num_seats == 2:
                if your_index == 1:
                    pos = 'post_flop_last'
                elif your_index == 0:
                    pos = 'post_flop_first'
            if num_seats > 2:
                if num_seats - 1 == your_index:
                    pos = 'BU'
                elif your_index == 0:
                    pos = 'SB'
                elif your_index == 1:
                    pos = 'BB'
                elif num_seats > 3:
                    if num_seats - 2 == your_index:
                        pos = 'CU'
                    elif num_seats > 4:
                        if num_seats - 3 == your_index:
                            pos = 'CU'
                        else:
                            pos = 'EP'
                    else:
                        pos = 'EP'
            print('\'' + str(pos) + '\'' + ', ')
            nums = []
            shapes = []
            raise_amount = 0
            for e in self.HAND:
                nums.append(e[0])
                shapes.append(e[1])
            if betting_round == BettingRound.PRE_FLOP:
                print(str(0) + ', ')
                print(str(0) + ', ')
                limps = 0
                nums = sorted(nums, key=lambda x: int(face_cards(x)), reverse=True)
                if shapes[0] == shapes[1]:
                    hand2 = nums[0] + nums[1] + 's'
                else:
                    hand2 = nums[0] + nums[1]
                    hand2 = str(hand2)
                if pos == 'SB':
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        if call_amount != (the_table.BIG_BLIND/2):
                            hand_index = hand2 in ep_and_blind_raise_starting_hands_3bet
                            if hand_index is True:
                                raise_amount = math.floor((call_amount - (the_table.BIG_BLIND/2)) * 3.5)
                                return Action.RAISE, raise_amount
                            else:
                                hand_index = hand2 in ep_and_blind_raise_starting_hands_call
                                if hand_index is True:
                                    return Action.CALL, 0
                                else:
                                    if call_amount > 0:
                                        return Action.FOLD, 0
                                    else:
                                        return Action.CALL, 0
                        else:
                            hand_index = hand2 in blind_limp_starting_hands_open_raise
                            for seat in seats:
                                if seat.HAD_CHANCE_TO_ACT is True:
                                    limps += 1
                                if seat.NOT_FOLDED is False:
                                    limps -= 1
                            if hand_index is True:
                                raise_amount = math.floor((3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND))
                                return Action.RAISE, raise_amount
                            else:
                                if call_amount > 0:
                                    return Action.FOLD, 0
                                else:
                                    return Action.CALL, 0
                    else:
                        hand_index = hand2 in ep_and_blind_raise_starting_hands_3bet
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            hand_index = hand2 in ep_and_blind_raise_starting_hands_call
                            if hand_index is True:
                                return Action.CALL, 0
                            else:
                                if call_amount > 0:
                                    return Action.FOLD, 0
                                else:
                                    return Action.CALL, 0
                if pos == 'BB':
                    if call_amount > 0:
                        hand_index = hand2 in ep_and_blind_raise_starting_hands_3bet
                        if hand_index is True:
                            raise_amount = math.floor(call_amount * 3.5)
                            return Action.RAISE, raise_amount
                        else:
                            hand_index = hand2 in ep_and_blind_raise_starting_hands_call
                            if hand_index is True:
                                return Action.CALL, 0
                            else:
                                if call_amount > 0:
                                    return Action.FOLD, 0
                                else:
                                    return Action.CALL, 0
                    else:
                        hand_index = hand2 in blind_limp_starting_hands_open_raise
                        for seat in seats:
                            if seat.HAD_CHANCE_TO_ACT is True:
                                limps += 1
                            if seat.NOT_FOLDED is False:
                                limps -= 1
                        if hand_index is True:
                            raise_amount = math.floor((3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND))
                            return Action.RAISE, raise_amount
                        else:
                            return Action.CALL, 0
                if pos == 'BU':
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        if call_amount != the_table.BIG_BLIND:
                            hand_index = hand2 in dealer_starting_hands_3bet
                            if hand_index is True:
                                raise_amount = math.floor((call_amount - the_table.BIG_BLIND) * 3.5)
                                return Action.RAISE, raise_amount
                            else:
                                hand_index = hand2 in dealer_starting_hands_call
                                if hand_index is True:
                                    return Action.CALL, 0
                                else:
                                    if call_amount > 0:
                                        return Action.FOLD, 0
                                    else:
                                        return Action.CALL, 0
                        else:
                            hand_index = hand2 in dealer_starting_hands_open_raise
                            for seat in seats:
                                if seat.HAD_CHANCE_TO_ACT is True:
                                    limps += 1
                                if seat.NOT_FOLDED is False:
                                    limps -= 1
                            if hand_index is True:
                                raise_amount = math.floor((3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND))
                                return Action.RAISE, raise_amount
                            else:
                                if call_amount > 0:
                                    return Action.FOLD, 0
                                else:
                                    return Action.CALL, 0
                    else:
                        hand_index = hand2 in dealer_starting_hands_3bet
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            hand_index = hand2 in dealer_starting_hands_call
                            if hand_index is True:
                                return Action.CALL, 0
                            else:
                                if call_amount > 0:
                                    return Action.FOLD, 0
                                else:
                                    return Action.CALL, 0
                if pos == 'CU':
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        if call_amount != the_table.BIG_BLIND:
                            hand_index = hand2 in cutoff_starting_hands_3bet
                            if hand_index is True:
                                raise_amount = math.floor((call_amount - the_table.BIG_BLIND) * 3.5)
                                return Action.RAISE, raise_amount
                            else:
                                hand_index = hand2 in cutoff_starting_hands_call
                                if hand_index is True:
                                    return Action.CALL, 0
                                else:
                                    if call_amount > 0:
                                        return Action.FOLD, 0
                                    else:
                                        return Action.CALL, 0
                        else:
                            hand_index = hand2 in cutoff_starting_hands_open_raise
                            for seat in seats:
                                if seat.HAD_CHANCE_TO_ACT is True:
                                    limps += 1
                                if seat.NOT_FOLDED is False:
                                    limps -= 1
                            if hand_index is True:
                                raise_amount = math.floor((3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND))
                                return Action.RAISE, raise_amount
                            else:
                                if call_amount > 0:
                                    return Action.FOLD, 0
                                else:
                                    return Action.CALL, 0
                    else:
                        hand_index = hand2 in cutoff_starting_hands_3bet
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            hand_index = hand2 in cutoff_starting_hands_call
                            if hand_index is True:
                                return Action.CALL, 0
                            else:
                                if call_amount > 0:
                                    return Action.FOLD, 0
                                else:
                                    return Action.CALL, 0
                if pos == 'EP':
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        if call_amount != the_table.BIG_BLIND:
                            hand_index = hand2 in ep_and_blind_raise_starting_hands_3bet
                            if hand_index is True:
                                raise_amount = math.floor((call_amount - the_table.BIG_BLIND) * 3.5)
                                return Action.RAISE, raise_amount
                            else:
                                hand_index = hand2 in ep_and_blind_raise_starting_hands_call
                                if hand_index is True:
                                    return Action.CALL, 0
                                else:
                                    if call_amount > 0:
                                        return Action.FOLD, 0
                                    else:
                                        return Action.CALL, 0
                        else:
                            hand_index = hand2 in ep_starting_hands_open_raise
                            for seat in seats:
                                if seat.HAD_CHANCE_TO_ACT is True:
                                    limps += 1
                                if seat.NOT_FOLDED is False:
                                    limps -= 1
                            if hand_index is True:
                                raise_amount = math.floor((3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND))
                                return Action.RAISE, raise_amount
                            else:
                                if call_amount > 0:
                                    return Action.FOLD, 0
                                else:
                                    return Action.CALL, 0
                    else:
                        hand_index = hand2 in ep_and_blind_raise_starting_hands_3bet
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            hand_index = hand2 in ep_and_blind_raise_starting_hands_call
                            if hand_index is True:
                                return Action.CALL, 0
                            else:
                                if call_amount > 0:
                                    return Action.FOLD, 0
                                else:
                                    return Action.CALL, 0
                if pos == 'post_flop_last':
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        hand_index = hand2 in heads_up_button_open_raise
                        for seat in seats:
                            if seat.HAD_CHANCE_TO_ACT is True:
                                limps += 1
                            if seat.NOT_FOLDED is False:
                                limps -= 1
                        if hand_index is True:
                            raise_amount = math.floor((3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND))
                            return Action.RAISE, raise_amount
                        else:
                            if call_amount > 0:
                                return Action.FOLD, 0
                            else:
                                return Action.CALL, 0
                    else:
                        hand_index = hand2 in heads_up_button_open_raise
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            if call_amount > 0:
                                return Action.FOLD, 0
                            else:
                                return Action.CALL, 0
                if pos == 'post_flop_first':
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        if call_amount > 0:
                            hand_index = hand2 in heads_up_ep_3bet
                            if hand_index is True:
                                raise_amount = math.floor(call_amount * 3.5)
                                return Action.RAISE, raise_amount
                            else:
                                hand_index = hand2 in heads_up_ep_open_raise
                                if hand_index is True:
                                    return Action.CALL, 0
                                else:
                                    if call_amount > 0:
                                        return Action.FOLD, 0
                                    else:
                                        return Action.CALL, 0
                        else:
                            hand_index = hand2 in heads_up_ep_open_raise
                            for seat in seats:
                                if seat.HAD_CHANCE_TO_ACT is True:
                                    limps += 1
                                if seat.NOT_FOLDED is False:
                                    limps -= 1
                            if hand_index is True:
                                raise_amount = math.floor((3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND))
                                return Action.RAISE, raise_amount
                            else:
                                return Action.CALL, 0
                    else:
                        hand_index = hand2 in heads_up_ep_3bet
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            if call_amount > 0:
                                return Action.FOLD, 0
                            else:
                                return Action.CALL, 0
            if betting_round == BettingRound.POST_FLOP:
                value_betting_percent = 0
                pot_odds = 0
                equity = 0
                opp_left = -1
                hand2 = []
                for e in the_table.SHARED_CARDS_SHOWING:
                    hand2.append(e)
                for e in self.HAND:
                    hand2.append(e)
                hand_data = DataFrameWrapper(hand2)
                if call_amount == 0:
                    print(str(0) + ', ')
                    print(str(0) + ', ')
                    value_betting_percent = hand_data.betting_value_results(hand_data.current_score5(hand2), hand_data.betting_value_index(hand2, hand_data.current_score5(hand2), thirty_three_percent))
                    if value_betting_percent < 50:
                        raise_amount = math.floor((the_table.POT/4)*3)
                        return Action.RAISE, raise_amount
                    else:
                        return Action.CALL, 0
                if call_amount > 0:
                    for seat in seats:
                        if seat.NOT_FOLDED is True:
                            opp_left += 1
                    pot_odds = hand_data.call_break_even_percent(the_table.POT, call_amount)
                    print(str(pot_odds) + ', ')
                    equity = multi_processing(monte_carlo_post_flop, [self.HAND, the_table.SHARED_CARDS_SHOWING, opp_left])
                    print(str(equity) + ', ')
                    if equity > pot_odds:
                        return Action.CALL, 0
                    else:
                        if call_amount > 0:
                            return Action.FOLD, 0
                        else:
                            return Action.CALL, 0
            if betting_round is BettingRound.POST_TURN:
                value_betting_percent = 0
                pot_odds = 0
                equity = 0
                opp_left = -1
                hand3 = []
                for e in the_table.SHARED_CARDS_SHOWING:
                    hand3.append(e)
                for e in self.HAND:
                    hand3.append(e)
                hand_data2 = DataFrameWrapper(hand3)
                if call_amount == 0:
                    print(str(0) + ', ')
                    print(str(0) + ', ')
                    value_betting_percent = hand_data2.betting_value_results(hand_data2.current_score6(hand3), hand_data2.betting_value_index(the_table.SHARED_CARDS_SHOWING, hand_data2.current_score6(hand3), thirty_three_percent))
                    if value_betting_percent < 50:
                        raise_amount = math.floor((the_table.POT/4)*3)
                        return Action.RAISE, raise_amount
                    else:
                        return Action.CALL, 0
                if call_amount > 0:
                    for seat in seats:
                        if seat.NOT_FOLDED is True:
                            opp_left += 1
                    pot_odds = hand_data2.call_break_even_percent(the_table.POT, call_amount)
                    print(str(pot_odds) + ', ')
                    equity = multi_processing(monte_carlo_post_flop, [self.HAND, the_table.SHARED_CARDS_SHOWING, opp_left])
                    print(str(equity) + ', ')
                    if equity > pot_odds:
                        return Action.CALL, 0
                    else:
                        if call_amount > 0:
                            return Action.FOLD, 0
                        else:
                            return Action.CALL, 0
                return Action.CALL, 0
            if betting_round is BettingRound.POST_RIVER:
                value_betting_percent = 0
                pot_odds = 0
                equity = 0
                opp_left = -1
                hand4 = []
                for e in the_table.SHARED_CARDS_SHOWING:
                    hand4.append(e)
                for e in self.HAND:
                    hand4.append(e)
                hand_data3 = DataFrameWrapper(hand4)
                if call_amount == 0:
                    print(str(0) + ', ')
                    print(str(0) + ', ')
                    value_betting_percent = hand_data3.betting_value_results(hand_data3.current_score7(hand4), hand_data3.betting_value_index(hand4, hand_data3.current_score7(hand4), thirty_three_percent))
                    if value_betting_percent < 50:
                        raise_amount = math.floor((the_table.POT/4)*3)
                        return Action.RAISE, raise_amount
                    else:
                        return Action.CALL, 0
                if call_amount > 0:
                    for seat in seats:
                        if seat.NOT_FOLDED is True:
                            opp_left += 1
                    pot_odds = hand_data3.call_break_even_percent(the_table.POT, call_amount)
                    print(str(pot_odds) + ', ')
                    equity = multi_processing(monte_carlo_post_flop, [self.HAND, the_table.SHARED_CARDS_SHOWING, opp_left])
                    print(str(equity) + ', ')
                    if equity > pot_odds:
                        return Action.CALL, 0
                    else:
                        if call_amount > 0:
                            return Action.FOLD, 0
                        else:
                            return Action.CALL, 0
                return Action.CALL, 0
        except Exception as e:
            print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
