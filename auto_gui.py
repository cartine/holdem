import pyautogui
from Run_OCR2 import *
from matplotlib import pyplot as plt
import cv2
import glob
import os
import time

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


def make_choice(filename):
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    for i in range(0, 1000):
        time.sleep(2)
        img = cv2.imread(filename)
        marker = img[243:280, 580:710, :]
        # plt.imshow(marker)
        # plt.show()
        s = pyautogui.locateOnScreen(marker, confidence=1)
        while s is None:
            try:
                s = pyautogui.locateOnScreen(marker)
            except:
                pass
        pyautogui.keyDown('win')
        pyautogui.keyDown('prtsc')
        pyautogui.keyUp('prtsc')
        pyautogui.keyUp('win')
        time.sleep(1)
        list_of_files = glob.glob(r'C:\Users\peter\OneDrive\Pictures\Screenshots\*.png')
        latest_file = max(list_of_files, key=os.path.getctime)
        print(str(latest_file))
        try:
            choice, raise_amount, call_amount, self_chips = run_OCR2(latest_file)
            print(choice)
            print('raise amount:', raise_amount)
            print('call amount:', call_amount)
            print('chips:', self_chips)
        except Exception as e:
            print(e)
            time.sleep(10)
        else:
            if choice == Action.FOLD:
                pyautogui.click(675, 850)
            if choice == Action.CALL:
                if self_chips == call_amount:
                    pyautogui.click(1200, 850)
                else:
                    pyautogui.click(925, 850)
            if choice == Action.RAISE:
                pyautogui.click(1250, 925)
                pyautogui.write(str(raise_amount))
                pyautogui.click(1200, 850)


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


filename = r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (419).png'


if __name__ == '__main__':
    make_choice(filename)