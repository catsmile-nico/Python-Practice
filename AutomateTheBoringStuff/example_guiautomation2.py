import pyautogui

pyautogui.typewrite("Hello world!", interval=0.2)
pyautogui.typewrite(["a","b","left","left","X","Y"], interval=0.2)

# show all keyboard keys
# pyautogui.KEYBOARD_KEYS

pyautogui.press("F1")

# press ctrl + letter
pyautogui.hotkey("ctrl","o")
