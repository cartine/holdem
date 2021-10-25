import pyautogui
from Run_OCR2 import *
import time
import os
import glob
from multiprocessing import Pool, Manager


# tracking by seat
def make_choice(filename):
    time1 = time.time()
    player2_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (898).png')[240:280, 1000:1100, :]
    player2_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (886).png')[240:280, 1000:1100, :]
    player2_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')[240:280, 1000:1100, :]
    player2_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (899).png')[240:280, 1000:1100, :]
    player2_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1049).png')[240:280, 1000:1100, :]
    player2_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')[240:280, 980:1121, :]
    player2_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1058).png')[240:280, 1000:1100, :]
    print('Timer1:', time.time() - time1)

    player3_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (592).png')[350:390, 1350:1450, :]
    player3_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')[350:390, 1350:1450, :]
    player3_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (999).png')[350:390, 1350:1450, :]
    player3_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (589).png')[350:390, 1350:1450, :]
    player3_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (583).png')[350:390, 1350:1450, :]
    player3_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (679).png')[350:390, 1328:1469, :]
    player3_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (802).png')[350:390, 1350:1450, :]
    print('Timer2:', time.time() - time1)

    player4_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1047).png')[620:660, 1375:1485, :]
    player4_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (770).png')[620:660, 1375:1485, :]
    player4_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1046).png')[620:660, 1375:1485, :]
    player4_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (962).png')[620:660, 1375:1485, :]
    player4_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1048).png')[620:660, 1375:1485, :]
    player4_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (739).png')[620:660, 1360:1501, :]
    player4_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1052).png')[620:660, 1375:1485, :]
    print('Timer3:', time.time() - time1)

    player5_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (648).png')[750:790, 1090:1200, :]
    player5_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')[750:790, 1090:1200, :]
    player5_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (973).png')[750:790, 1090:1200, :]
    player5_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1005).png')[750:790, 1090:1200, :]
    player5_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (649).png')[750:790, 1090:1200, :]
    player5_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1059).png')[750:790, 1075:1216, :]
    player5_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (779).png')[750:790, 1090:1200, :]
    print('Timer4:', time.time() - time1)

    player6_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (728).png')[772:812, 792:902, :]
    player6_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')[772:812, 792:902, :]
    player6_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (627).png')[772:812, 792:902, :]
    player6_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1056).png')[772:812, 792:902, :]
    player6_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')[772:812, 792:902, :]
    player6_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (686).png')[772:812, 776:917, :]
    player6_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1035).png')[772:812, 792:902, :]
    print('Timer5:', time.time() - time1)

    player7_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (577).png')[752:792, 488:598, :]
    player7_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')[752:792, 488:598, :]
    player7_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (618).png')[752:792, 488:598, :]
    player7_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (578).png')[752:792, 488:598, :]
    player7_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')[752:792, 488:598, :]
    player7_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (658).png')[752:792, 474:615, :]
    player7_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (732).png')[752:792, 488:598, :]
    print('Timer6:', time.time() - time1)

    player8_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (695).png')[620:660, 206:316, :]
    player8_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (657).png')[620:660, 206:316, :]
    player8_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (784).png')[620:660, 206:316, :]
    player8_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (709).png')[620:660, 206:316, :]
    player8_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (697).png')[620:660, 206:316, :]
    player8_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (693).png')[620:660, 189:330, :]
    player8_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (866).png')[620:660, 206:316, :]
    print('Timer7:', time.time() - time1)

    player9_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (595).png')[349:389, 240:350, :]
    player9_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (599).png')[349:389, 240:350, :]
    player9_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (419).png')[349:389, 240:350, :]
    player9_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (674).png')[349:389, 240:350, :]
    player9_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (604).png')[349:389, 240:350, :]
    player9_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (590).png')[349:389, 225:366, :]
    player9_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (701).png')[349:389, 240:350, :]
    print('Timer8:', time.time() - time1)

    img = cv2.imread(filename)
    marker = img[243:280, 580:710, :]
    print('Timer9:', time.time() - time1)

    player2_refs = [player2_check, player2_call, player2_raise, player2_bet, player2_fold, player2_allin]
    player3_refs = [player3_check, player3_call, player3_raise, player3_bet, player3_fold, player3_allin]
    player4_refs = [player4_check, player4_call, player4_raise, player4_bet, player4_fold, player4_allin]
    player5_refs = [player5_check, player5_call, player5_raise, player5_bet, player5_fold, player5_allin]
    player6_refs = [player6_check, player6_call, player6_raise, player6_bet, player6_fold, player6_allin]
    player7_refs = [player7_check, player7_call, player7_raise, player7_bet, player7_fold, player7_allin]
    player8_refs = [player8_check, player8_call, player8_raise, player8_bet, player8_fold, player8_allin]
    player9_refs = [player9_check, player9_call, player9_raise, player9_bet, player9_fold, player9_allin]
    player_refs = [player2_refs, player3_refs, player4_refs, player5_refs, player6_refs, player7_refs, player8_refs, player9_refs]
    new_players = [player2_new_player, player3_new_player, player4_new_player, player5_new_player, player6_new_player, player7_new_player, player8_new_player, player9_new_player, ]
    player_functs = [seat2_move, seat3_move, seat4_move, seat5_move, seat6_move, seat7_move, seat8_move, seat9_move]
    print('Timer10:', time.time() - time1)

    print('data = [')
    index = 0
    hand_num = 1
    self_chips = 120
    print('Timer11:', time.time() - time1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    print('Timer12:', time.time() - time1)
    m = Manager()
    q = m.Queue()
    q2 = m.Queue()
    print('Timer13:', time.time() - time1)
    pool3 = Pool(processes=1)
    print('Timer14:', time.time() - time1)
    p4 = pool3.apply_async(find_new_player, args=(q2, *new_players))
    print('Timer15:', time.time() - time1)
    seat_functs = []
    while self_chips > 20:
        print(', ')
        # plt.imshow(marker)
        # plt.show()

        q.put('New')
        pool = Pool(processes=1)
        print('Timer16:', time.time() - time1)
        p1 = pool.apply_async(find_marker, args=(q, q2, marker))
        print('Timer17:', time.time() - time1)
        print('<><><><><>', seat_functs)
        if len(seat_functs) > 0:
            print('Timer18:', time.time() - time1)
            for i in range(0, len(seat_functs)):
                print('Timer19:', time.time() - time1)
                if i % 2 == 1:
                    print('Timer20:', time.time() - time1)
                    continue
                print('Timer21:', time.time() - time1)
                pool2 = Pool(processes=2)
                print('Timer22:', time.time() - time1)
                try:
                    print('Timer23:', time.time() - time1)
                    p2 = pool2.apply_async(seat_functs[i].__call__, args=(q, 1, *player_refs[i]))
                    print('Timer24:', time.time() - time1)
                    p3 = pool2.apply_async(seat_functs[i+1].__call__, args=(q, 2, *player_refs[i+1]))
                    print('Timer25:', time.time() - time1)
                except:
                    pass
                print('Timer26:', time.time() - time1)
                pool2.close()
                print('Timer27:', time.time() - time1)
                pool2.join()
                print('Timer28:', time.time() - time1)
        print('Timer29:', time.time() - time1)
        pool.close()
        print('Timer30:', time.time() - time1)
        pool.join()
        print('Timer31:', time.time() - time1)
        list_of_files = glob.glob(r'C:\Users\peter\OneDrive\Pictures\Screenshots\*.png')
        latest_file = max(list_of_files, key=os.path.getctime)
        latest_file2 = str(latest_file).replace('\\', '\\\\')
        print('Timer32:', time.time() - time1)
        hole_cards = find_hole_cards(latest_file)
        print('Timer33:', time.time() - time1, hole_cards)
        will = find_not_mistake(latest_file)
        print('Timer34:', time.time() - time1, will)
        if hole_cards[0][1] == 'H' or hole_cards[0][1] == 'S' or hole_cards[0][1] == 'C' or hole_cards[0][1] == 'D':
            if will != 'will':
                print('Not Mistake')
                try:
                    print('(')
                    print('\'' + latest_file2 + '\'' + ', ')
                    seat_indices = []
                    seat_functs = []
                    choice, raise_amount, call_amount, self_chips, pot, self_index, seat_length, seats = run_OCR2(latest_file, hole_cards)
                    for seat in seats:
                        l = seat.PLAYER.NAME[-1]
                        if l != 'f' and seat.NOT_FOLDED is True:
                            seat_indices.append(int(l))
                    seat_indices = sorted(seat_indices)
                    for i in seat_indices:
                        seat_functs.append(player_functs[i-2])
                    print(str(hand_num) + ', ')
                    print('\'' + str(choice) + '\'' + ', ')
                    print(str(raise_amount) + ', ')
                    print(str(call_amount) + ', ')
                    print(str(self_chips) + ', ')
                    print(str(pot) + ')')
                except Exception as e:
                    print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
                    print('Error:', e)
                    time.sleep(1)
                else:
                    if choice == Action.FOLD:
                        pyautogui.click(675, 850)
                        hand_num += 1
                    if choice == Action.CALL:
                        if self_chips == call_amount:
                            pyautogui.click(1200, 850)
                        else:
                            pyautogui.click(925, 850)
                    if choice == Action.RAISE:
                        pyautogui.click(1250, 925)
                        pyautogui.write(str(raise_amount))
                        pyautogui.click(1200, 850)
    pool3.terminate()
    pyautogui.click(1882, 18)
    pyautogui.click(910, 550)
    print(']')
    # client.messages.create(to="+12035178290",
    #                        from_="+12817710887",
    #                        body="Finished Game")


def find_marker(q, q2, marker):
    s = pyautogui.locateOnScreen(marker)
    while s is None:
        try:
            s = pyautogui.locateOnScreen(marker)
        except:
            pass
    time1 = time.time()
    pyautogui.keyDown('win')
    pyautogui.keyDown('prtsc')
    pyautogui.keyUp('prtsc')
    pyautogui.keyUp('win')
    time.sleep(3)
    q.put('Done')
    q.put('Done')
    print('PLAYER MOVES {{{{{{{{{{')
    for m in range(0, q2.qsize()):
        print(q2.get())
    for m in range(0, q.qsize()):
        print(q.get())
    print('TIME:', time.time() - time1)
    print('}}}}}}}}}}}')


def seat2_move(q, thread, player2_check, player2_call, player2_raise, player2_bet, player2_fold, player2_allin):
    print('Run 2', 'size:', q.qsize(), 'thread:', thread)
    queue_size = q.qsize()
    if queue_size < 1:
        return
    if thread == 1:
        while q.qsize() == queue_size:
            time1 = time.time()
            if pyautogui.locateOnScreen(player2_check, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 checks')
                break
            if pyautogui.locateOnScreen(player2_call, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 calls')
                break
            if pyautogui.locateOnScreen(player2_raise, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 raises')
                break
            if pyautogui.locateOnScreen(player2_bet, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 bets')
                break
            if pyautogui.locateOnScreen(player2_allin, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 is all in')
                break
            if pyautogui.locateOnScreen(player2_fold, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 folds')
                break
            if q.qsize() > queue_size:
                break
            print('PLAYER 2 TIME:', time.time() - time1)
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            if pyautogui.locateOnScreen(player2_check, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 checks')
                break
            if pyautogui.locateOnScreen(player2_call, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 calls')
                break
            if pyautogui.locateOnScreen(player2_raise, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 raises')
                break
            if pyautogui.locateOnScreen(player2_bet, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 bets')
                break
            if pyautogui.locateOnScreen(player2_allin, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 is all in')
                break
            if pyautogui.locateOnScreen(player2_fold, confidence=0.9, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 folds')
                break


def seat3_move(q, thread, player3_check, player3_call, player3_raise, player3_bet, player3_fold, player3_allin):
    print('Run 3', 'size:', q.qsize(), 'var:', thread)
    queue_size = q.qsize()
    if queue_size < 1:
        return
    if thread == 1:
        while q.qsize() == queue_size:
            if pyautogui.locateOnScreen(player3_check, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 checks')
                break
            if pyautogui.locateOnScreen(player3_call, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 calls')
                break
            if pyautogui.locateOnScreen(player3_raise, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 raises')
                break
            if pyautogui.locateOnScreen(player3_bet, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 bets')
                break
            if pyautogui.locateOnScreen(player3_allin, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 is all in')
                break
            if pyautogui.locateOnScreen(player3_fold, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 folds')
                break
            if q.qsize() > queue_size:
                break
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            if pyautogui.locateOnScreen(player3_check, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 checks')
                break
            if pyautogui.locateOnScreen(player3_call, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 calls')
                break
            if pyautogui.locateOnScreen(player3_raise, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 raises')
                break
            if pyautogui.locateOnScreen(player3_bet, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 bets')
                break
            if pyautogui.locateOnScreen(player3_allin, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 is all in')
                break
            if pyautogui.locateOnScreen(player3_fold, confidence=0.9, region=(1350, 350, 110, 40)) is not None:
                q.put('Player 3 folds')
                break


def seat4_move(q, thread, player4_check, player4_call, player4_raise, player4_bet, player4_fold, player4_allin):
    print('Run 4', 'size:', q.qsize(), 'var:', thread)
    queue_size = q.qsize()
    if queue_size < 1:
        return
    if thread == 1:
        while q.qsize() == queue_size:
            if pyautogui.locateOnScreen(player4_check, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 checks')
                break
            if pyautogui.locateOnScreen(player4_call, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 calls')
                break
            if pyautogui.locateOnScreen(player4_raise, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 raises')
                break
            if pyautogui.locateOnScreen(player4_bet, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 bets')
                break
            if pyautogui.locateOnScreen(player4_allin, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 is all in')
                break
            if pyautogui.locateOnScreen(player4_fold, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 folds')
                break
            if q.qsize() > queue_size:
                break
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            if pyautogui.locateOnScreen(player4_check, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 checks')
                break
            if pyautogui.locateOnScreen(player4_call, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 calls')
                break
            if pyautogui.locateOnScreen(player4_raise, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 raises')
                break
            if pyautogui.locateOnScreen(player4_bet, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 bets')
                break
            if pyautogui.locateOnScreen(player4_allin, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 is all in')
                break
            if pyautogui.locateOnScreen(player4_fold, confidence=0.9, region=(1375, 620, 110, 40)) is not None:
                q.put('Player 4 folds')
                break


def seat5_move(q, thread, player5_check, player5_call, player5_raise, player5_bet, player5_fold, player5_allin):
    print('Run 5', 'size:', q.qsize(), 'var:', thread)
    queue_size = q.qsize()
    if queue_size < 1:
        return
    if thread == 1:
        while q.qsize() == queue_size:
            if pyautogui.locateOnScreen(player5_check, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 checks')
                break
            if pyautogui.locateOnScreen(player5_call, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 calls')
                break
            if pyautogui.locateOnScreen(player5_raise, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 raises')
                break
            if pyautogui.locateOnScreen(player5_bet, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 bets')
                break
            if pyautogui.locateOnScreen(player5_allin, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 is all in')
                break
            if pyautogui.locateOnScreen(player5_fold, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 folds')
                break
            if q.qsize() > queue_size:
                break
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            if pyautogui.locateOnScreen(player5_check, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 checks')
                break
            if pyautogui.locateOnScreen(player5_call, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 calls')
                break
            if pyautogui.locateOnScreen(player5_raise, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 raises')
                break
            if pyautogui.locateOnScreen(player5_bet, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 bets')
                break
            if pyautogui.locateOnScreen(player5_allin, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 is all in')
                break
            if pyautogui.locateOnScreen(player5_fold, confidence=0.9, region=(1090, 750, 110, 40)) is not None:
                q.put('Player 5 folds')
                break


def seat6_move(q, thread, player6_check, player6_call, player6_raise, player6_bet, player6_fold, player6_allin):
    print('Run 6', 'size:', q.qsize(), 'thread:', thread)
    queue_size = q.qsize()
    if queue_size < 1:
        return
    if thread == 1:
        while q.qsize() == queue_size:
            if pyautogui.locateOnScreen(player6_check, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 checks')
                break
            if pyautogui.locateOnScreen(player6_call, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 calls')
                break
            if pyautogui.locateOnScreen(player6_raise, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 raises')
                break
            if pyautogui.locateOnScreen(player6_bet, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 bets')
                break
            if pyautogui.locateOnScreen(player6_allin, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 is all in')
                break
            if pyautogui.locateOnScreen(player6_fold, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 folds')
                break
            if q.qsize() > queue_size:
                break
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            if pyautogui.locateOnScreen(player6_check, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 checks')
                break
            if pyautogui.locateOnScreen(player6_call, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 calls')
                break
            if pyautogui.locateOnScreen(player6_raise, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 raises')
                break
            if pyautogui.locateOnScreen(player6_bet, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 bets')
                break
            if pyautogui.locateOnScreen(player6_allin, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 is all in')
                break
            if pyautogui.locateOnScreen(player6_fold, confidence=0.9, region=(792, 772, 110, 40)) is not None:
                q.put('Player 6 folds')
                break


def seat7_move(q, thread, player7_check, player7_call, player7_raise, player7_bet, player7_fold, player7_allin):
    print('Run 7', 'size:', q.qsize(), 'var:', thread)
    queue_size = q.qsize()
    if queue_size < 1:
        return
    if thread == 1:
        while q.qsize() == queue_size:
            if pyautogui.locateOnScreen(player7_check, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 checks')
                break
            if pyautogui.locateOnScreen(player7_call, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 calls')
                break
            if pyautogui.locateOnScreen(player7_raise, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 raises')
                break
            if pyautogui.locateOnScreen(player7_bet, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 bets')
                break
            if pyautogui.locateOnScreen(player7_allin, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 is all in')
                break
            if pyautogui.locateOnScreen(player7_fold, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 folds')
                break
            if q.qsize() > queue_size:
                break
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            if pyautogui.locateOnScreen(player7_check, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 checks')
                break
            if pyautogui.locateOnScreen(player7_call, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 calls')
                break
            if pyautogui.locateOnScreen(player7_raise, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 raises')
                break
            if pyautogui.locateOnScreen(player7_bet, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 bets')
                break
            if pyautogui.locateOnScreen(player7_allin, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 is all in')
                break
            if pyautogui.locateOnScreen(player7_fold, confidence=0.9, region=(488, 752, 110, 40)) is not None:
                q.put('Player 7 folds')
                break


def seat8_move(q, thread, player8_check, player8_call, player8_raise, player8_bet, player8_fold, player8_allin):
    print('Run 8', 'size:', q.qsize(), 'var:', thread)
    queue_size = q.qsize()
    if queue_size < 1:
        return
    if thread == 1:
        while q.qsize() == queue_size:
            if pyautogui.locateOnScreen(player8_check, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 checks')
                break
            if pyautogui.locateOnScreen(player8_raise, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 raises')
                break
            if pyautogui.locateOnScreen(player8_bet, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 bets')
                break
            if pyautogui.locateOnScreen(player8_call, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 calls')
                break
            if pyautogui.locateOnScreen(player8_allin, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 is all in')
                break
            if pyautogui.locateOnScreen(player8_fold, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 folds')
                break
            if q.qsize() > queue_size:
                break
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            if pyautogui.locateOnScreen(player8_check, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 checks')
                break
            if pyautogui.locateOnScreen(player8_raise, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 raises')
                break
            if pyautogui.locateOnScreen(player8_bet, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 bets')
                break
            if pyautogui.locateOnScreen(player8_call, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 calls')
                break
            if pyautogui.locateOnScreen(player8_allin, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 is all in')
                break
            if pyautogui.locateOnScreen(player8_fold, confidence=0.9, region=(206, 620, 110, 40)) is not None:
                q.put('Player 8 folds')
                break


def seat9_move(q, thread, player9_check, player9_call, player9_raise, player9_bet, player9_fold, player9_allin):
    print('Run 9', 'size:', q.qsize(), 'var:', thread)
    queue_size = q.qsize()
    if queue_size < 1:
        return
    if thread == 1:
        while q.qsize() == queue_size:
            time1 = time.time()
            if pyautogui.locateOnScreen(player9_check, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 checks')
                break
            if pyautogui.locateOnScreen(player9_call, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 calls')
                break
            if pyautogui.locateOnScreen(player9_raise, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 raises')
                break
            if pyautogui.locateOnScreen(player9_bet, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 bets')
                break
            if pyautogui.locateOnScreen(player9_allin, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 is all in')
                break
            if pyautogui.locateOnScreen(player9_fold, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 folds')
                break
            if q.qsize() > queue_size:
                break
            print('PLAYER 9 TIME:', time.time() - time1)
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            time1 = time.time()
            if pyautogui.locateOnScreen(player9_check, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 checks')
                break
            if pyautogui.locateOnScreen(player9_call, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 calls')
                break
            if pyautogui.locateOnScreen(player9_raise, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 raises')
                break
            if pyautogui.locateOnScreen(player9_bet, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 bets')
                break
            if pyautogui.locateOnScreen(player9_allin, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 is all in')
                break
            if pyautogui.locateOnScreen(player9_fold, confidence=0.9, region=(240, 349, 110, 40)) is not None:
                q.put('Player 9 folds')
                break
            print('PLAYER 9 TIME:', time.time() - time1)


def find_new_player(q, player2_new_player, player3_new_player, player4_new_player, player5_new_player, player6_new_player, player7_new_player, player8_new_player, player9_new_player):
    counter = 0
    for i in range(10000000000):
        if i % 20 == 0:
            counter = 0
        if pyautogui.locateOnScreen(player2_new_player, confidence=0.9, region=(980, 240, 141, 40)) is not None and counter != 2:
            q.put('Player 2 is new')
            counter = 2
        if pyautogui.locateOnScreen(player3_new_player, confidence=0.9, region=(1328, 350, 141, 40)) is not None and counter != 3:
            q.put('Player 3 is new')
            counter = 3
        if pyautogui.locateOnScreen(player4_new_player, confidence=0.9, region=(1360, 620, 141, 40)) is not None and counter != 4:
            q.put('Player 4 is new')
            counter = 4
        if pyautogui.locateOnScreen(player5_new_player, confidence=0.9, region=(1075, 750, 141, 40)) is not None and counter != 5:
            q.put('Player 5 is new')
            counter = 5
        if pyautogui.locateOnScreen(player6_new_player, confidence=0.9, region=(776, 772, 141, 40)) is not None and counter != 6:
            q.put('Player 6 is new')
            counter = 6
        if pyautogui.locateOnScreen(player7_new_player, confidence=0.9, region=(474, 752, 141, 40)) is not None and counter != 7:
            q.put('Player 7 is new')
            counter = 7
        if pyautogui.locateOnScreen(player8_new_player, confidence=0.9, region=(189, 620, 141, 40)) is not None and counter != 8:
            q.put('Player 8 is new')
            counter = 8
        if pyautogui.locateOnScreen(player9_new_player, confidence=0.9, region=(225, 349, 141, 40)) is not None and counter != 9:
            q.put('Player 9 is new')
            counter = 9


filename = r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (419).png'

if __name__ == '__main__':
    make_choice(filename)

# if someone folds the program should know to skip them and also need to optimize speed for opponent tracking.
# Either track opponents and datamine the screenshot at same time or figure out a way to speed program up