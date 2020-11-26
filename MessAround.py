import pyautogui
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    i = Image.open('10ofClubs.png')
    iar = np.asarray(i)
    plt.imshow(iar)
    print(iar)



pyautogui.hotkey('alt', 'tab')
pyautogui.moveTo(100, 100)