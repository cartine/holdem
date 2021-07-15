import pyautogui
import cv2
from matplotlib import pyplot as plt
import time
from multiprocessing import Pool, Manager


def run():
    player2_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (898).png')[240:280, 1000:1100, :]
    player2_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (886).png')[240:280, 1000:1100, :]
    player2_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')[240:280, 1000:1100, :]
    player2_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (899).png')[240:280, 1000:1100, :]
    player2_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1049).png')[240:280, 1000:1100, :]
    player2_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')[240:280, 980:1121, :]
    player2_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1058).png')[240:280, 1000:1100, :]

    player3_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (592).png')[350:390, 1350:1450, :]
    player3_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')[350:390, 1350:1450, :]
    player3_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (999).png')[350:390, 1350:1450, :]
    player3_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (589).png')[350:390, 1350:1450, :]
    player3_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (583).png')[350:390, 1350:1450, :]
    player3_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (679).png')[350:390, 1328:1469, :]
    player3_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (802).png')[350:390, 1350:1450, :]

    player4_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1047).png')[620:660, 1375:1485, :]
    player4_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (770).png')[620:660, 1375:1485, :]
    player4_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1046).png')[620:660, 1375:1485, :]
    player4_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (962).png')[620:660, 1375:1485, :]
    player4_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1048).png')[620:660, 1375:1485, :]
    player4_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (739).png')[620:660, 1360:1501, :]
    player4_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1052).png')[620:660, 1375:1485, :]

    player5_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (648).png')[750:790, 1090:1200, :]
    player5_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')[750:790, 1090:1200, :]
    player5_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (973).png')[750:790, 1090:1200, :]
    player5_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1005).png')[750:790, 1090:1200, :]
    player5_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (649).png')[750:790, 1090:1200, :]
    player5_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1059).png')[750:790, 1075:1216, :]
    player5_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (779).png')[750:790, 1090:1200, :]

    player6_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (728).png')[772:812, 792:902, :]
    player6_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')[772:812, 792:902, :]
    player6_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (627).png')[772:812, 792:902, :]
    player6_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1056).png')[772:812, 792:902, :]
    player6_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')[772:812, 792:902, :]
    player6_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (686).png')[772:812, 776:917, :]
    player6_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1035).png')[772:812, 792:902, :]

    player7_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (577).png')[752:792, 488:598, :]
    player7_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')[752:792, 488:598, :]
    player7_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (618).png')[752:792, 488:598, :]
    player7_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (578).png')[752:792, 488:598, :]
    player7_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')[752:792, 488:598, :]
    player7_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (658).png')[752:792, 474:615, :]
    player7_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (732).png')[752:792, 488:598, :]

    player8_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (695).png')[620:660, 206:316, :]
    player8_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (657).png')[620:660, 206:316, :]
    player8_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (784).png')[620:660, 206:316, :]
    player8_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (709).png')[620:660, 206:316, :]
    player8_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (697).png')[620:660, 206:316, :]
    player8_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (693).png')[620:660, 189:330, :]
    player8_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (866).png')[620:660, 206:316, :]

    player9_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (595).png')[349:389, 240:350, :]
    player9_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (599).png')[349:389, 240:350, :]
    player9_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (419).png')[349:389, 240:350, :]
    player9_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (674).png')[349:389, 240:350, :]
    player9_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (604).png')[349:389, 240:350, :]
    player9_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (590).png')[349:389, 225:366, :]
    player9_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (701).png')[349:389, 240:350, :]

    marker = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (419).png')[243: 280, 580: 710, :]

    # plt.imshow(player3_check)
    # plt.show()

    checks = [player2_check, player3_check, player4_check, player5_check, player6_check, player7_check, player8_check, player9_check]
    calls = [player2_call, player3_call, player4_call, player5_call, player6_call, player7_call, player8_call, player9_call]
    raises = [player2_raise, player3_raise, player4_raise, player5_raise, player6_raise, player7_raise, player8_raise, player9_raise]
    bets = [player2_bet, player3_bet, player4_bet, player5_bet, player6_bet, player7_bet, player8_bet, player9_bet]
    folds = [player2_fold, player3_fold, player4_fold, player5_fold, player6_fold, player7_fold, player8_fold, player9_fold]
    new_players = [player2_new_player, player3_new_player, player4_new_player, player5_new_player, player6_new_player, player7_new_player, player8_new_player, player9_new_player]
    allins = [player2_allin, player3_allin, player4_allin, player5_allin, player6_allin, player7_allin, player8_allin, player9_allin]
    time1 = time.time()
    m = Manager()
    q = m.Queue()
    moves = [0]
    pool = Pool(processes=4)
    th1 = pool.apply_async(call_check, [q, *checks, *calls])
    th2 = pool.apply_async(raise_bet, [q, *raises, *bets])
    th3 = pool.apply_async(new_player_allin, [q, *new_players, *allins])
    th4 = pool.apply_async(fold_marker, [q, marker, *folds])
    # if th4.get() == 'Terminate':
    #     pool.terminate()
    # else:
    pool.close()
    pool.join()
    time2 = time.time() - time1
    print(time2)
    for element in range(q.qsize()):
        a = q.get()
        if a != moves[-1]:
            moves.append(a)
    return moves


# def get_results(result):
#     if result == 'Terminate':
#         pool.terminate()


def call_check(q, player2_check, player3_check, player4_check, player5_check, player6_check, player7_check, player8_check, player9_check, player2_call, player3_call, player4_call, player5_call, player6_call, player7_call, player8_call, player9_call):
    for i in range(5):
        if pyautogui.locateOnScreen(player2_check, region=(1000, 240, 110, 40)) is not None:
            q.put('Player 2 checks')
        if pyautogui.locateOnScreen(player2_call, region=(1000, 240, 110, 40)) is not None:
            q.put('Player 2 calls')
        if pyautogui.locateOnScreen(player3_check, region=(1350, 350, 110, 40)) is not None:
            q.put('Player 3 checks')
        if pyautogui.locateOnScreen(player3_call, region=(1350, 350, 110, 40)) is not None:
            q.put('Player 3 calls')
        if pyautogui.locateOnScreen(player4_check, region=(1375, 620, 110, 40)) is not None:
            q.put('Player 4 checks')
        if pyautogui.locateOnScreen(player4_call, region=(1375, 620, 110, 40)) is not None:
            q.put('Player 4 calls')
        if pyautogui.locateOnScreen(player5_check, region=(1090, 750, 110, 40)) is not None:
            q.put('Player 5 checks')
        if pyautogui.locateOnScreen(player5_call, region=(1090, 750, 110, 40)) is not None:
            q.put('Player 5 calls')
        if pyautogui.locateOnScreen(player6_check, region=(792, 772, 110, 40)) is not None:
            q.put('Player 6 checks')
        if pyautogui.locateOnScreen(player6_call, region=(792, 772, 110, 40)) is not None:
            q.put('Player 6 calls')
        if pyautogui.locateOnScreen(player7_check, region=(488, 752, 110, 40)) is not None:
            q.put('Player 7 checks')
        if pyautogui.locateOnScreen(player7_call, region=(488, 752, 110, 40)) is not None:
            q.put('Player 7 calls')
        if pyautogui.locateOnScreen(player8_check, region=(206, 620, 110, 40)) is not None:
            q.put('Player 8 checks')
        if pyautogui.locateOnScreen(player8_call, region=(206, 620, 110, 40)) is not None:
            q.put('Player 8 calls')
        if pyautogui.locateOnScreen(player9_check, region=(240, 349, 110, 40)) is not None:
            q.put('Player 9 checks')
        if pyautogui.locateOnScreen(player9_call, region=(240, 349, 110, 40)) is not None:
            q.put('Player 9 calls')


def raise_bet(q, player2_raise, player3_raise, player4_raise, player5_raise, player6_raise, player7_raise, player8_raise, player9_raise, player2_bet, player3_bet, player4_bet, player5_bet, player6_bet, player7_bet, player8_bet, player9_bet):
    for i in range(5):
        if pyautogui.locateOnScreen(player2_raise, region=(1000, 240, 110, 40)) is not None:
            q.put('Player 2 raises')
        if pyautogui.locateOnScreen(player2_bet, region=(1000, 240, 110, 40)) is not None:
            q.put('Player 2 bets')
        if pyautogui.locateOnScreen(player3_raise, region=(1350, 350, 110, 40)) is not None:
            q.put('Player 3 raises')
        if pyautogui.locateOnScreen(player3_bet, region=(1350, 350, 110, 40)) is not None:
            q.put('Player 3 bets')
        if pyautogui.locateOnScreen(player4_raise, region=(1375, 620, 110, 40)) is not None:
            q.put('Player 4 raises')
        if pyautogui.locateOnScreen(player4_bet, region=(1375, 620, 110, 40)) is not None:
            q.put('Player 4 bets')
        if pyautogui.locateOnScreen(player5_raise, region=(1090, 750, 110, 40)) is not None:
            q.put('Player 5 raises')
        if pyautogui.locateOnScreen(player5_bet, region=(1090, 750, 110, 40)) is not None:
            q.put('Player 5 bets')
        if pyautogui.locateOnScreen(player6_raise, region=(792, 772, 110, 40)) is not None:
            q.put('Player 6 raises')
        if pyautogui.locateOnScreen(player6_bet, region=(792, 772, 110, 40)) is not None:
            q.put('Player 6 bets')
        if pyautogui.locateOnScreen(player7_raise, region=(488, 752, 110, 40)) is not None:
            q.put('Player 7 raises')
        if pyautogui.locateOnScreen(player7_bet, region=(488, 752, 110, 40)) is not None:
            q.put('Player 7 bets')
        if pyautogui.locateOnScreen(player8_raise, region=(206, 620, 110, 40)) is not None:
            q.put('Player 8 raises')
        if pyautogui.locateOnScreen(player8_bet, region=(206, 620, 110, 40)) is not None:
            q.put('Player 8 bets')
        if pyautogui.locateOnScreen(player9_raise, region=(240, 349, 110, 40)) is not None:
            q.put('Player 9 raises')
        if pyautogui.locateOnScreen(player9_bet, region=(240, 349, 110, 40)) is not None:
            q.put('Player 9 bets')


def new_player_allin(q, player2_new_player, player3_new_player, player4_new_player, player5_new_player, player6_new_player, player7_new_player, player8_new_player, player9_new_player, player2_allin, player3_allin, player4_allin, player5_allin, player6_allin, player7_allin, player8_allin, player9_allin):
    for i in range(5):
        if pyautogui.locateOnScreen(player2_new_player, region=(980, 240, 141, 40)) is not None:
            q.put('Player 2 is new')
        if pyautogui.locateOnScreen(player2_allin, region=(1000, 240, 110, 40)) is not None:
            q.put('Player 2 is all in')
        if pyautogui.locateOnScreen(player3_new_player, region=(1328, 350, 141, 40)) is not None:
            q.put('Player 3 is new')
        if pyautogui.locateOnScreen(player3_allin, region=(1350, 350, 110, 40)) is not None:
            q.put('Player 3 is all in')
        if pyautogui.locateOnScreen(player4_new_player, region=(1360, 620, 141, 40)) is not None:
            q.put('Player 4 is new')
        if pyautogui.locateOnScreen(player4_allin, region=(1375, 620, 110, 40)) is not None:
            q.put('Player 4 is all in')
        if pyautogui.locateOnScreen(player5_new_player, region=(1075, 750, 141, 40)) is not None:
            q.put('Player 5 is new')
        if pyautogui.locateOnScreen(player5_allin, region=(1090, 750, 110, 40)) is not None:
            q.put('Player 5 is all in')
        if pyautogui.locateOnScreen(player6_new_player, region=(776, 772, 141, 40)) is not None:
            q.put('Player 6 is new')
        if pyautogui.locateOnScreen(player6_allin, region=(792, 772, 110, 40)) is not None:
            q.put('Player 6 is all in')
        if pyautogui.locateOnScreen(player7_new_player, region=(474, 752, 141, 40)) is not None:
            q.put('Player 7 is new')
        if pyautogui.locateOnScreen(player7_allin, region=(488, 752, 110, 40)) is not None:
            q.put('Player 7 is all in')
        if pyautogui.locateOnScreen(player8_new_player, region=(189, 620, 141, 40)) is not None:
            q.put('Player 8 is new')
        if pyautogui.locateOnScreen(player8_allin, region=(206, 620, 110, 40)) is not None:
            q.put('Player 8 is all in')
        if pyautogui.locateOnScreen(player9_new_player, region=(225, 349, 141, 40)) is not None:
            q.put('Player 9 is new')
        if pyautogui.locateOnScreen(player9_allin, region=(240, 349, 110, 40)) is not None:
            q.put('Player 9 is all in')


def fold_marker(q, marker, player2_fold, player3_fold, player4_fold, player5_fold, player6_fold, player7_fold, player8_fold, player9_fold):
    for i in range(5):
        time1 = time.time()
        print('Start')
        # if pyautogui.locateOnScreen(marker, region=(580, 243, 130, 37)) is not None:
        #     print('Terminate')
        #     return 'Terminate'
        if pyautogui.locateOnScreen(player2_fold, region=(1000, 240, 110, 40)) is not None:
            q.put('Player 2 folds')
        if pyautogui.locateOnScreen(player3_fold, region=(1350, 350, 110, 40)) is not None:
            q.put('Player 3 folds')
        if pyautogui.locateOnScreen(player4_fold, region=(1375, 620, 110, 40)) is not None:
            q.put('Player 4 folds')
        if pyautogui.locateOnScreen(player5_fold, region=(1090, 750, 110, 40)) is not None:
            q.put('Player 5 folds')
        if pyautogui.locateOnScreen(player6_fold, region=(792, 772, 110, 40)) is not None:
            q.put('Player 6 folds')
        if pyautogui.locateOnScreen(player7_fold, region=(488, 752, 110, 40)) is not None:
            q.put('Player 7 folds')
        if pyautogui.locateOnScreen(player8_fold, region=(206, 620, 110, 40)) is not None:
            q.put('Player 8 folds')
        if pyautogui.locateOnScreen(player9_fold, region=(240, 349, 110, 40)) is not None:
            q.put('Player 9 folds')
        print(time.time() - time1)
        print('End')


if __name__ == '__main__':
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    print(run())
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')



    # for i in range(2, 10):
    #     height = 40
    #     width = 110
    #     nwidth = 141
    #     if i == 2:
    #         y = 240
    #         x = 1000
    #         n = 980
    #     if i == 3:
    #         y = 350
    #         x = 1350
    #         n = 1328
    #     if i == 4:
    #         y = 620
    #         x = 1375
    #         n = 1360
    #     if i == 5:
    #         y = 750
    #         x = 1090
    #         n = 1075
    #     if i == 6:
    #         y = 772
    #         x = 792
    #         n = 776
    #     if i == 7:
    #         y = 752
    #         x = 488
    #         n = 474
    #     if i == 8:
    #         y = 620
    #         x = 206
    #         n = 189
    #     if i == 9:
    #         y = 349
    #         x = 240
    #         n = 225
    #     region = 'region=' + '(' + str(x) + ', ' + str(y) + ', ' + str(width) + ', ' + str(height) + '))'
    #     nregion = 'region=' + '(' + str(n) + ', ' + str(y) + ', ' + str(nwidth) + ', ' + str(height) + '))'
    #     print('player' + str(i) + '_check2 = pyautogui.locateOnScreen(player' + str(i) + '_check, ' + region)
    #     print('player' + str(i) + '_call2 = pyautogui.locateOnScreen(player' + str(i) + '_call, ' + region)
    #     print('player' + str(i) + '_raise2 = pyautogui.locateOnScreen(player' + str(i) + '_raise, ' + region)
    #     print('player' + str(i) + '_bet2 = pyautogui.locateOnScreen(player' + str(i) + '_bet, ' + region)
    #     print('player' + str(i) + '_fold2 = pyautogui.locateOnScreen(player' + str(i) + '_fold, ' + region)
    #     print('player' + str(i) + '_new_player2 = pyautogui.locateOnScreen(player' + str(i) + '_new_player, ' + nregion)
    #     print('player' + str(i) + '_allin2 = pyautogui.locateOnScreen(player' + str(i) + '_allin, ' + region)

        # print('player' + str(i) + '_check2 = pyautogui.locateOnScreen(player' + str(i) + '_check, confidence = 1)')
        # print('player' + str(i) + '_call2 = pyautogui.locateOnScreen(player' + str(i) + '_call)')
        # print('player' + str(i) + '_raise2 = pyautogui.locateOnScreen(player' + str(i) + '_raise)')
        # print('player' + str(i) + '_bet2 = pyautogui.locateOnScreen(player' + str(i) + '_bet)')
        # print('player' + str(i) + '_fold2 = pyautogui.locateOnScreen(player' + str(i) + '_fold)')
        # print('player' + str(i) + '_new_player2 = pyautogui.locateOnScreen(player' + str(i) + '_new_player)')
        # print('player' + str(i) + '_allin2 = pyautogui.locateOnScreen(player' + str(i) + '_allin)')

        # print('player' + str(i) + '_check2 = None')
        # print('player' + str(i) + '_call2 = None')
        # print('player' + str(i) + '_raise2 = None')
        # print('player' + str(i) + '_bet2 = None')
        # print('player' + str(i) + '_fold2 = None')
        # print('player' + str(i) + '_new_player2 = None')
        # print('player' + str(i) + '_allin2 = None')

        # print('player' + str(i) + '_check, ')
        # print('player' + str(i) + '_call, ')
        # print('player' + str(i) + '_raise, ')
        # print('player' + str(i) + '_bet, ')
        # print('player' + str(i) + '_fold, ')
        # print('player' + str(i) + '_new_player, ')
        # print('player' + str(i) + '_allin, ')

        # print('if pyautogui.locateOnScreen(player' + str(i) + '_check, ' + region + ' is not None:')
        # print('    return \'Player ' + str(i) + ' checks\'')

        # print('if pyautogui.locateOnScreen(player' + str(i) + '_call, ' + region + ' is not None:')
        # print('    return \'Player ' + str(i) + ' calls\'')
        #
        # print('if pyautogui.locateOnScreen(player' + str(i) + '_raise, ' + region + ' is not None:')
        # print('    return \'Player ' + str(i) + ' raises\'')
        #
        # print('if pyautogui.locateOnScreen(player' + str(i) + '_bet, ' + region + ' is not None:')
        # print('    return \'Player ' + str(i) + ' bets\'')

        # print('if pyautogui.locateOnScreen(player' + str(i) + '_fold, ' + region + ' is not None:')
        # print('    return \'Player ' + str(i) + ' folds\'')

        # print('if pyautogui.locateOnScreen(player' + str(i) + '_new_player, ' + nregion + ' is not None:')
        # print('    return \'Player ' + str(i) + ' is new\'')
        #
        # print('if pyautogui.locateOnScreen(player' + str(i) + '_allin, ' + region + ' is not None:')
        # print('    return \'Player ' + str(i) + ' is all in\'')