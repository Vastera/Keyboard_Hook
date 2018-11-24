# all meepo hoof 
import keyboard
import mouse
import time
from key_series import*
from mouse import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE
def all_hoof(delay=0.02):
    key_series('f')
    mouse.wait(target_types=UP)
    key_series('tab,f')
    mouse.click()
    time.sleep(delay)
    key_series('tab,f')
    mouse.click()
    time.sleep(delay)
    key_series('tab,f')
    mouse.click()
    time.sleep(delay)
    key_series('tab,f')
    mouse.click()
    time.sleep(delay)
    key_series('1')