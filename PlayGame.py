import pyautogui

if __name__ == '__main__':
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    pyautogui.click(900, 350)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')
    pyautogui.keyUp('alt')