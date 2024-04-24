import keyboard
import time

def lock_keyboard():
    keyboard.block_key("windows")  # Block the Windows key
    keyboard.block_key("alt")  # Block the Alt key

def unlock_keyboard():
    keyboard.unblock_key("windows")  # Unblock the Windows key
    keyboard.unblock_key("alt")  # Unblock the Alt key

def main():
    locked = False

    while True:
        if keyboard.is_pressed('alt+k+l') and not locked:
            locked = True
            lock_keyboard()
            print("Keyboard locked")
            time.sleep(0.2)  # Add a small delay to avoid rapid key presses
        elif keyboard.is_pressed('alt+k+u') and locked:
            locked = False
            unlock_keyboard()
            print("Keyboard unlocked")
            time.sleep(0.2)  # Add a small delay to avoid rapid key presses

if __name__ == "__main__":
    main()
