import time
import subprocess
import pyautogui

# Function to open Brave browser with a specific URL
def open_brave(url):
    subprocess.Popen("start brave", shell=True)
    time.sleep(5)
    pyautogui.write(url)
    pyautogui.press('enter')
    print(f"Opened URL: {url}")
    time.sleep(2)

# Function to Close Brave browser
def close_brave():
    print("\nClosing Brave browser...")
    subprocess.run(["taskkill", "/f", "/im", "brave.exe"], shell=True)
