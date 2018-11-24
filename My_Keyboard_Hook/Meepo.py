# assemble all the shotcuts
import keyboard
import mouse
import time
from key_series import*
from others_hoof import*
from all_hoof import*
from mouse import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE

while True:
    keyboard.add_hotkey('b',others_hoof, args=(''),suppress=True,timeout=0.01,trigger_on_release=True),
    keyboard.add_hotkey('space',all_hoof, args=(''),suppress=True,timeout=0.01,trigger_on_release=True)
    keyboard.wait('enter')
    keyboard.clear_all_hotkeys()
    keyboard.wait('enter')