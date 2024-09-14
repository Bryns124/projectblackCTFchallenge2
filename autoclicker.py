import pyautogui
import time

correct_x, correct_y = 892, 312
wrong_x, wrong_y = 1019, 312

time.sleep(2)

with open("questions.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    equation, result = line.split("=")
    equation = equation.strip()
    result = int(result.strip())

    correct_result = eval(equation)

    if correct_result == result:
        print(f"{line.strip()} -> Correct")
        pyautogui.click(x=correct_x, y=correct_y)
    else:
        print(f"{line.strip()} -> Wrong")
        pyautogui.click(x=wrong_x, y=wrong_y)