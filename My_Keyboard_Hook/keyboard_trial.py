# this is to try to use 'keyboard' repository
import keyboard
import mouse
import time
from mouse import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE
print('Hello World~')
keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))
# recorded = keyboard.record(until='esc') 
# # Then replay back at three times the speed.
# keyboard.play(recorded, speed_factor=3)
# keyboard.add_abbreviation('@@', 'my.long.email@example.com')
# def my_click():
    # keyboard.press_and_release('1')
time.sleep(0.01)
mouse.wait(button=LEFT,target_types=UP)
mouse.double_click(button=LEFT)
print('Hello World~')
# mouse.on_click(my_click,args=())
while True:
    keyboard.wait('esc')
    keyboard.write('The quick brown fox jumps over the lazy dog.')
    keyboard.press_and_release('shift+s, space')
    print('Hello World~')

