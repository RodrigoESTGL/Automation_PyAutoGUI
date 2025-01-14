import pyautogui
import time 

def google():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=791, y=74)
    pyautogui.write("https://www.google.com")
    pyautogui.press("enter")
    time.sleep(2)

def youtube():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=791, y=74)
    pyautogui.write("https://www.youtube.com/")
    pyautogui.press("enter")
    time.sleep(2)

def github():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=791, y=74)
    pyautogui.write("https://github.com/RodrigoESTGL/")
    pyautogui.press("enter")
    time.sleep(2)

def chatgpt():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=791, y=74)
    pyautogui.write("https://chatgpt.com/")
    pyautogui.press("enter")
    time.sleep(2)

def vscode():
    pyautogui.press("win")
    pyautogui.write("Visual Studio Code")
    pyautogui.press("enter")

def position():
    time.sleep(5)
    print(pyautogui.position())
