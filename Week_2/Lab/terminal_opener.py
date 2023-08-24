import pyautogui
import time
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

pyautogui.hotkey("win")
time.sleep(1)
pyautogui.write("Terminal")
time.sleep(1)
pyautogui.click("Terminal.png")
