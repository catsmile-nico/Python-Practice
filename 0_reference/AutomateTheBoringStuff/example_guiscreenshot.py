import pyautogui

# take ss
pyautogui.screenshot("example.png")

# locate png on screen
print(pyautogui.locateOnScreen("examplegmailicon.png"))

# locate center of png
print(pyautogui.locateCenterOnScreen("examplegmailicon.png"))

pyautogui.moveTo((62,19), duration=1)


