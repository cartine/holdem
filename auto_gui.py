import pyautogui
from Run_OCR2 import *
from matplotlib import pyplot as plt
import cv2
import glob
import os
import time
from twilio.rest import Client

client = Client('ACbd6e091ee9938a7b59d89badf665bbd4', '8d8b5696136ca68bd4acad38e900d73f')


def take_screenshot():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    # pyautogui.moveTo(500, 500, duration=.25)
    pyautogui.keyDown('win')
    pyautogui.keyDown('prtsc')
    pyautogui.keyUp('prtsc')
    pyautogui.keyUp('win')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')


def take_screenshot2():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyDown('win')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
    pyautogui.keyUp('win')
    pyautogui.keyUp('ctrl')
    pyautogui.keyDown('win')
    pyautogui.keyDown('prtsc')
    pyautogui.keyUp('prtsc')
    pyautogui.keyUp('win')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyDown('win')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')
    pyautogui.keyUp('win')
    pyautogui.keyUp('ctrl')


def make_choice(filename):
    hand_num = 1
    self_chips = 120
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    while self_chips < 240:
        img = cv2.imread(filename)
        marker = img[243:280, 580:710, :]
        # plt.imshow(marker)
        # plt.show()
        s = pyautogui.locateOnScreen(marker, confidence=1)
        t = time.time()
        while s is None:
            try:
                s = pyautogui.locateOnScreen(marker)
                t2 = time.time() - t
                if t2 > 300:
                    self_chips = 300
                    s = 1
            except:
                pass
        if s != 1:
            pyautogui.keyDown('win')
            pyautogui.keyDown('prtsc')
            pyautogui.keyUp('prtsc')
            pyautogui.keyUp('win')
            time.sleep(1)
            list_of_files = glob.glob(r'C:\Users\peter\OneDrive\Pictures\Screenshots\*.png')
            latest_file = max(list_of_files, key=os.path.getctime)
            print(str(latest_file))
            hole_cards = find_hole_cards(latest_file)
            if hole_cards[0][1] == 'H' or hole_cards[0][1] == 'S' or hole_cards[0][1] == 'C' or hole_cards[0][1] == 'D':
                try:
                    choice, raise_amount, call_amount, self_chips, pot, self_index, seat_length = run_OCR2(latest_file, hole_cards)
                    print('hand #:', hand_num)
                    print(choice)
                    print('raise amount:', raise_amount)
                    print('call amount:', call_amount)
                    print('chips:', self_chips)
                    print('pot:', pot)
                except Exception as e:
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
    pyautogui.click(1882, 18)
    pyautogui.click(910, 550)
    client.messages.create(to="+12035178290",
                           from_="+12817710887",
                           body="Finished Game")


filename = r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (419).png'


if __name__ == '__main__':
    make_choice(filename)