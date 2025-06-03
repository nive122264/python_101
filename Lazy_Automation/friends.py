import time
import pyautogui
from datetime import datetime, timedelta

def watch_episodes(max_minutes=120):
    center_x = 1300
    center_y = 800
    end_time = datetime.now() + timedelta(minutes=max_minutes)

    # Click to play current episode
    print(f"Moving cursor to ({center_x}, {center_y})")
    pyautogui.moveTo(center_x, center_y, duration=1)
    time.sleep(1)
    pyautogui.doubleClick()
    print("Clicked to Play")
    
    while datetime.now() < end_time:
        start_action = datetime.now()
        pyautogui.moveTo(center_x, center_y, duration=1)
        time.sleep(2)
        print("Clicked to Play")
        pyautogui.doubleClick()
        pyautogui.doubleClick()

        print("Watching episode...")
        time.sleep(1380)  # 23 minutes
        # Click next episode
        print("Clicking next episode...")
        pyautogui.moveTo(600, 1130, duration=1)
        pyautogui.doubleClick()
        
        # Wait for next episode to load
        print("Loading next episode...")
        time.sleep(2)
