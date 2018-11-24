# all the other meepoes hoof
import keyboard
import mouse
import time
from key_series import*
from mouse import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE
def others_hoof(delay=0.02):
    key_series('2,f')
    mouse.wait(target_types=UP)
    key_series('3,f')
    mouse.click()
    time.sleep(delay)
    key_series('4,f')
    mouse.click()
    time.sleep(delay)
    key_series('5,f')
    mouse.click()
    time.sleep(delay)
    key_series('1')

