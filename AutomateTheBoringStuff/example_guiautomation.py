import pyautogui

print(pyautogui.size())
width,height = pyautogui.size()

print(pyautogui.position())

# move mouse to coord
pyautogui.moveTo(10,10)
pyautogui.moveTo(590,500, duration=1.5)

# move mouse to right/left, up/down
pyautogui.moveRel(20,0)
pyautogui.moveRel(-200,0, duration=1.5)

pyautogui.click(590,500) #doubleClick, rightClick, middleClick
pyautogui.click()

# Drag
# pyautogui.dragTo(10,10)
# pyautogui.dragRel(10,10)

# Display mouse nonstop
# pyautogui.displayMousePosition()
