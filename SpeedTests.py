import cv2
import pyautogui
from matplotlib import pyplot as plt

player2_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (898).png')[240:280, 1000:1100, :]
player2_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (886).png')[240:280, 1000:1100, :]
player2_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')[240:280, 1000:1100, :]
player2_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (899).png')[240:280, 1000:1100, :]
player2_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1049).png')[240:280, 1000:1100, :]
player2_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')[240:280, 980:1121,
                     :]
player2_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1058).png')[240:280, 1000:1100, :]

player3_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (592).png')[350:390, 1350:1450, :]
player3_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')[350:390, 1350:1450, :]
player3_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (999).png')[350:390, 1350:1450, :]
player3_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (589).png')[350:390, 1350:1450, :]
player3_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (583).png')[350:390, 1350:1450, :]
player3_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (679).png')[350:390,
                     1328:1469, :]
player3_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (802).png')[350:390, 1350:1450, :]

player4_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1047).png')[620:660, 1375:1485, :]
player4_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (770).png')[620:660, 1375:1485, :]
player4_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1046).png')[620:660, 1375:1485, :]
player4_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (962).png')[620:660, 1375:1485, :]
player4_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1048).png')[620:660, 1375:1485, :]
player4_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (739).png')[620:660,
                     1360:1501, :]
player4_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1052).png')[620:660, 1375:1485, :]

player5_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (648).png')[750:790, 1090:1200, :]
player5_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')[750:790, 1090:1200, :]
player5_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (973).png')[750:790, 1090:1200, :]
player5_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1005).png')[750:790, 1090:1200, :]
player5_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (649).png')[750:790, 1090:1200, :]
player5_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1059).png')[750:790,
                     1075:1216, :]
player5_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (779).png')[750:790, 1090:1200, :]

player6_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (728).png')[772:812, 792:902, :]
player6_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')[772:812, 792:902, :]
player6_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (627).png')[772:812, 792:902, :]
player6_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1056).png')[772:812, 792:902, :]
player6_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')[772:812, 792:902, :]
player6_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (686).png')[772:812, 776:917,
                     :]
player6_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1035).png')[772:812, 792:902, :]

player7_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (577).png')[752:792, 488:598, :]
player7_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')[752:792, 488:598, :]
player7_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (618).png')[752:792, 488:598, :]
player7_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (578).png')[752:792, 488:598, :]
player7_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')[752:792, 488:598, :]
player7_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (658).png')[752:792, 474:615,
                     :]
player7_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (732).png')[752:792, 488:598, :]

player8_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (695).png')[620:660, 206:316, :]
player8_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (657).png')[620:660, 206:316, :]
player8_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (784).png')[620:660, 206:316, :]
player8_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (709).png')[620:660, 206:316, :]
player8_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (697).png')[620:660, 206:316, :]
player8_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (693).png')[620:660, 189:330,
                     :]
player8_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (866).png')[620:660, 206:316, :]

player9_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (595).png')[349:389, 240:350, :]
player9_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (599).png')[349:389, 240:350, :]
player9_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (419).png')[349:389, 240:350, :]
player9_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (674).png')[349:389, 240:350, :]
player9_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (604).png')[349:389, 240:350, :]
player9_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (590).png')[349:389, 225:366,
                     :]
player9_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (701).png')[349:389, 240:350, :]

if __name__ == '__main__':
    while pyautogui.locateOnScreen(player9_call, confidence=0.9, region=(240, 349, 110, 40)) is None:
        # print(pyautogui.locateOnScreen(player9_fold, region=(240, 349, 110, 40)))
        print('LL')
    print('Player 9 folds')