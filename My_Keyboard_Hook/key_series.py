# to execute a series of key pressing
import keyboard
import time
def key_series(*keys,delay=0.02):
    for key in keys:
        keyboard.press_and_release(key)
        time.sleep(delay)