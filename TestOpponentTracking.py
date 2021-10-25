from multiprocessing import Pool, Manager
import time
import os
import glob
import pyautogui
import random


def process_screenshot(q, h):
    time.sleep(2)
    print(q.get())
    l = random.randint(-100,100)
    print(l)
    l += h.get()
    h.set(l)



def take_screenshot():
    a = random.randint(0, 5)
    b = random.randint(0, 4)
    time.sleep(a)
    pyautogui.keyDown('win')
    pyautogui.keyDown('prtsc')
    pyautogui.keyUp('prtsc')
    pyautogui.keyUp('win')
    print(b)
    return b


if __name__ == '__main__':
    m = Manager()
    h = m.Value('i', 100)
    q = m.Queue()
    for i in range(0,100):
        pool = Pool(processes=2)
        p1 = pool.apply_async(take_screenshot)
        if q.empty() is False:
            p2 = pool.apply_async(process_screenshot, args=(q, h))
        r = p1.get()
        time.sleep(1)
        if r != 0:
            list_of_files = glob.glob(r'C:\Users\peter\OneDrive\Pictures\Screenshots\*.png')
            latest_file = max(list_of_files, key=os.path.getctime)
            q.put(latest_file)
        else:
            pool.terminate()
            print(h.get())