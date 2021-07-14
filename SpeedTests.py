import pyautogui
import time
import cv2
from multiprocessing import Manager, Pool


player2_check = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (898).png')[240:280, 1000:1100, :]
player2_call = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (886).png')[240:280, 1000:1100, :]
player2_raise = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')[240:280, 1000:1100, :]
player2_bet = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (899).png')[240:280, 1000:1100, :]
player2_fold = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1049).png')[240:280, 1000:1100, :]
player2_new_player = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')[240:280, 980:1121,
                     :]
player2_allin = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1058).png')[240:280, 1000:1100, :]
player2_refs = [player2_check, player2_call, player2_raise, player2_bet, player2_fold, player2_allin]


def seat2_move(q, thread, player2_check, player2_call, player2_raise, player2_bet, player2_fold, player2_allin):
    print('Run 2', 'size:', q.qsize(), 'thread:', thread)
    queue_size = q.qsize()
    if queue_size < 1:
        return
    if thread == 1:
        while q.qsize() == queue_size:
            time1 = time.time()
            print('size:', q.qsize(), 'var:', queue_size)
            if pyautogui.locateOnScreen(player2_check, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 checks')
                break
            if pyautogui.locateOnScreen(player2_call, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 calls')
                break
            if pyautogui.locateOnScreen(player2_raise, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 raises')
                break
            if pyautogui.locateOnScreen(player2_bet, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 bets')
                break
            if pyautogui.locateOnScreen(player2_allin, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 is all in')
                break
            if pyautogui.locateOnScreen(player2_fold, region=(1000, 240, 110, 40)) is not None:
                print('YY')
                q.put('Player 2 folds')
                break
            if q.qsize() > queue_size:
                break
            print('PLAYER 2 TIME:', time.time() - time1)
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            if pyautogui.locateOnScreen(player2_check, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 checks')
                break
            if pyautogui.locateOnScreen(player2_call, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 calls')
                break
            if pyautogui.locateOnScreen(player2_raise, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 raises')
                break
            if pyautogui.locateOnScreen(player2_bet, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 bets')
                break
            if pyautogui.locateOnScreen(player2_allin, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 is all in')
                break
            if pyautogui.locateOnScreen(player2_fold, region=(1000, 240, 110, 40)) is not None:
                q.put('Player 2 folds')
                break
    for m in range(0, q.qsize()):
        print(q.get())

if __name__ == '__main__':
    time1 = time.time()
    m = Manager()
    print('time2:', time.time() - time1)
    q = m.Queue()
    print('time3:', time.time() - time1)
    q.put('New')
    print('time4:', time.time() - time1)
    pool = Pool(processes=1)
    print('time5:', time.time() - time1)
    p1 = pool.apply_async(seat2_move, args=(q, 1, *player2_refs))
    print('time6:', time.time() - time1)
    pool.close()
    print('time7:', time.time() - time1)
    pool.join()
    print('time8:', time.time() - time1)