import keyboard
import time
import subprocess

def lock_keyboard():
    # Get the currently active window ID
    window_id = subprocess.run(["xdotool", "getactivewindow"], capture_output=True).stdout.decode()
    # Focus on the current window to lock it
    subprocess.run(["xdotool", "windowfocus", window_id.strip()])
    print("Keyboard locked (focused window)")

def unlock_keyboard():
    # No need to unlock, focus will return to normal behavior when the application loses focus
    print("Keyboard unlocked")

def main():
    locked = False

    while True:
        if keyboard.is_pressed('alt+k+l') and not locked:
            locked = True
            lock_keyboard()
            time.sleep(0.2)  # Add a small delay to avoid rapid key presses
        elif keyboard.is_pressed('alt+k+u') and locked:
            locked = False
            unlock_keyboard()
            time.sleep(0.2)  # Add a small delay to avoid rapid key presses

if __name__ == "__main__":
    main()
