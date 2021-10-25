import pyautogui
# from Run_OCR2 import *
from matplotlib import pyplot as plt
import cv2
import glob
import os
import time
from multiprocessing import Manager, Pool


if __name__ == '__main__':
    img1 = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\DontDelete1.png')
    marker1 = img1[243:280, 580:710]
    img2 = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\DontDelete2.png')
    marker2 = img2[243:280, 990:1120]
    img3 = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\DontDelete3.png')
    marker3 = img3[349:386, 1340:1470]
    img4 = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\DontDelete4.png')
    marker4 = img4[624:661, 1370:1500]
    img5 = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\DontDelete5.png')
    marker5 = img5[754:791, 1087:1217]
    img6 = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\DontDelete6.png')
    marker6 = img6[774:811, 784:914]
    img7 = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\DontDelete7.png')
    marker7 = img7[754:791, 484:614]
    img8 = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\DontDelete8.png')
    marker8 = img8[624:661, 200:330]
    img9 = cv2.imread(r'C:\Users\peter\OneDrive\Pictures\Screenshots\DontDelete9.png')
    marker9 = img9[352:389, 235:365]
    s = None
    while s is None:
        if s is None:
            try:
                s = pyautogui.locateOnScreen(marker1, confidence=.7, region=(540, 241, 130, 37))
            except:
                pass
        if s is None:
            try:
                s = pyautogui.locateOnScreen(marker2, confidence=.7, region=(954, 241, 130, 37))
            except:
                pass
        if s is None:
            try:
                s = pyautogui.locateOnScreen(marker3, confidence=.8, region=(1299, 348, 130, 37))
            except:
                pass
        if s is None:
            try:
                s = pyautogui.locateOnScreen(marker4, confidence=.7, region=(1337, 622, 130, 37))
            except:
                pass
        if s is None:
            try:
                s = pyautogui.locateOnScreen(marker5, confidence=.7, region=(1051, 752, 130, 37))
            except:
                pass
        if s is None:
            try:
                s = pyautogui.locateOnScreen(marker6, confidence=.7, region=(748, 772, 130, 37))
            except:
                pass
        if s is None:
            try:
                s = pyautogui.locateOnScreen(marker7, confidence=.8, region=(474, 752, 130, 37))
            except:
                pass
        if s is None:
            try:
                s = pyautogui.locateOnScreen(marker8, confidence=.8, region=(192, 622, 130, 37))
            except:
                pass
        if s is None:
            try:
                s = pyautogui.locateOnScreen(marker9, confidence=.7, region=(200, 350, 130, 37))
            except:
                pass
    if str(s) == 'Box(left=557, top=244, width=130, height=37)':
        print('Seat 1')
    if str(s) == 'Box(left=954, top=241, width=130, height=37)':
        print('Seat 2')
    if str(s) == 'Box(left=1299, top=348, width=130, height=37)':
        print('Seat 3')
    if str(s) == 'Box(left=1337, top=622, width=130, height=37)':
        print('Seat 4')
    if str(s) == 'Box(left=1051, top=752, width=130, height=37)':
        print('Seat 5')
    if str(s) == 'Box(left=748, top=772, width=130, height=37)':
        print('Seat 6')
    if str(s) == 'Box(left=474, top=752, width=130, height=37)':
        print('Seat 7')
    if str(s) == 'Box(left=192, top=622, width=130, height=37)':
        print('Seat 8')
    if str(s) == 'Box(left=200, top=350, width=130, height=37)':
        print('Seat 9')

# s1 = pyautogui.locateOnScreen(marker1, confidence=.7, region=(540, 241, 130, 37))
# s2 = pyautogui.locateOnScreen(marker2, confidence=.7, region=(954, 241, 130, 37))
# s3 = pyautogui.locateOnScreen(marker3, confidence=.8, region=(1299, 348, 130, 37))
# s4 = pyautogui.locateOnScreen(marker4, confidence=.7, region=(1337, 622, 130, 37))
# s5 = pyautogui.locateOnScreen(marker5, confidence=.7, region=(1051, 752, 130, 37))
# s6 = pyautogui.locateOnScreen(marker6, confidence=.7, region=(748, 772, 130, 37))
# s7 = pyautogui.locateOnScreen(marker7, confidence=.8, region=(474, 752, 130, 37))
# s8 = pyautogui.locateOnScreen(marker8, confidence=.8, region=(192, 622, 130, 37))
# s9 = pyautogui.locateOnScreen(marker9, confidence=.7, region=(200, 350, 130, 37))



# Seat1 - [243:280, 580:710, :], Seat2 - [243:280, 990:1120], Seat3 - [349:386, 1340:1470], Seat4 - [624:661, 1370:1500],
# Seat5 - [754:791, 1087:1217], Seat6 - [774:811, 784:914], Seat7 - [754:791, 484:614], Seat8 - [624:661, 200:330], Seat9 - [352:389, 235:365]