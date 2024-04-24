import pyautogui
import keyboard
import time

def lock_mouse():
    pyautogui.moveTo(0, 0)

def unlock_mouse():
    pyautogui.moveTo(100, 100)

def main():
    locked = False

    while True:
        if keyboard.is_pressed('alt+m+l') and not locked:
            locked = True
            lock_mouse()
            time.sleep(0.2)  # Add a small delay to avoid rapid key presses
        elif keyboard.is_pressed('alt+m+u') and locked:
            locked = False
            unlock_mouse()
            time.sleep(0.2)  # Add a small delay to avoid rapid key presses

        if locked:
            lock_mouse()
            time.sleep(0.01)  # Adjust this value as needed for smoothness

if __name__ == "__main__":
    main()
