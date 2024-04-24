import time
import AppKit

def lock_keyboard():
    AppKit.NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(AppKit.NSKeyDownMask, lambda event: None)

def unlock_keyboard():
    AppKit.NSEvent.removeMonitor_(None)

def main():
    locked = False

    while True:
        if keyboard.is_pressed('alt+k+l') and not locked:  # This line will cause an error
            locked = True
            lock_keyboard()
            print("Keyboard locked")
            time.sleep(0.2)  # Add a small delay to avoid rapid key presses
        elif AppKit.NSEvent.eventType(AppKit.NSKeyDown):  # Use AppKit to check for key presses
            event = AppKit.NSApp.currentEvent()
            if event.modifierFlags() & AppKit.NSAlternateKeyMask and event.keyCode() == 75 and not locked:
                # Check for Alt+K+L shortcut
                locked = True
                lock_keyboard()
                print("Keyboard locked")
                time.sleep(0.2)  # Add a small delay to avoid rapid key presses
        elif locked and AppKit.NSEvent.eventType(AppKit.NSKeyUp):
            event = AppKit.NSApp.currentEvent()
            if event.modifierFlags() & AppKit.NSAlternateKeyMask and event.keyCode() == 75:
                # Check for Alt+K+L release to unlock
                locked = False
                unlock_keyboard()
                print("Keyboard unlocked")
                time.sleep(0.2)  # Add a small delay to avoid rapid key presses

if __name__ == "__main__":
    main()
