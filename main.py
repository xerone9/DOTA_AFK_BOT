import os
import time
import pyautogui
import datetime
from pynput.keyboard import Key, Controller

pyautogui.FAILSAFE = False

condition = 0
bot = False
user_is_back = 0
start_time = ""
show_afk_time = True

# def on_press(key):
#     time.sleep(1.0)
#     global list_letters
#     list_letters.append(key)
#     list_letters.pop(0)
#     print(list_letters)


while True:
    try:
        seconds = int(input("After how many seconds the bot will trigger: "))
        break
    except ValueError:
        print("Incorrect Value Entered\n")
print("""
What you want your AFK bot to do...

Select Chioce

1- Move Mouse
2- Cast Spells
3- Enter Message
    """)

while True:
    try:
        choice = int(input("Select Choice: "))
        if choice == 1:
            os.system('cls')
            print("BOT ACTIVATED...")
            print("````````````````\n")
            print("Move will automatically start moving after " + str(seconds) + " seconds of inactivity\n")
            break
        elif choice == 2:
            os.system('cls')
            print("BOT ACTIVATED...")
            print("````````````````\n")
            print("Bot will cast random spell (Except Ultimate) after " + str(seconds) + " seconds of inactivity\n")
            break
        elif choice == 3:
            message = input("What message you want to send to Allies: ")
            os.system('cls')
            print("BOT ACTIVATED...")
            print("````````````````\n")
            print("Bot will send this message '" + message + "' after " + str(seconds) + " seconds of inactivity\n")
            break
        else:
            print("Incorrect Choice Made")
    except ValueError:
        print("Incorrect Value Entered")

global list_letters
list_letters = []
for i in range(1, int(seconds) + 1):
    list_letters.append(i)

while True:
    time.sleep(1.0)
    datex = str(datetime.datetime.now()).split(".")
    date_and_time = str(datex[0]).split(" ")
    date = date_and_time[0]
    timex = date_and_time[1]
    x, y = pyautogui.position()
    value = x * y
    list_letters.append(value)
    list_letters.pop(0)
    # with Listener(on_press=on_press) as listener:
    #     listener.join()
    result = list_letters.count(list_letters[0]) == len(list_letters)
    if (result):
        show_afk_time = True
        if condition < 1:
            if bot is False:
                start_time = timex
                bot = True
            condition += 1
        print("You are AFK")
        if choice == 1:
            m_x, m_y = pyautogui.size()
            start_x = int((m_x / 2) / 2)
            end_x = m_x - start_x
            start_y = int((m_y / 2) / 2)
            end_y = m_y - start_y
            pyautogui.moveTo(start_x, int(m_y / 2), duration=1)
            pyautogui.rightClick()
            pyautogui.moveTo(int(m_x/2), end_y, duration=1)
            pyautogui.rightClick()
            pyautogui.moveTo(end_x, int(m_y / 2), duration=1)
            pyautogui.rightClick()
            pyautogui.moveTo(int(m_x/2), start_y, duration=1)
            pyautogui.rightClick()
            list_letters.append('mouse_moved')
            list_letters.pop(0)
            user_is_back = 0

        if choice == 2:
            keyboard = Controller()
            keyboard.press('q')
            keyboard.release('q')
            keyboard.press('w')
            keyboard.release('w')
            keyboard.press('e')
            keyboard.release('e')
            list_letters.append('q')
            list_letters.pop(0)
            user_is_back = 0

        if choice == 3:
            keyboard = Controller()
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            for i in message:
                time.sleep(0.1)
                keyboard.press(i)
                keyboard.release(i)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            list_letters.append('message')
            list_letters.pop(0)
            user_is_back = 0
    else:
        user_is_back += 1
        if condition > 0:
            datex = str(datetime.datetime.now()).split(".")
            date_and_time = str(datex[0]).split(" ")
            date = date_and_time[0]
            timex = date_and_time[1]
            condition = 0

        if user_is_back > 10:
            if show_afk_time is True:
                print("you were AFK From " + start_time + " to " + timex)
                show_afk_time = False
                bot = False
                condition = 0
