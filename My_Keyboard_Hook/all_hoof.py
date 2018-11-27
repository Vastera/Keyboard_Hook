# all meepo hoof 
import keyboard
import mouse
import time
from key_series import*
from mouse import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE


def all_hoof(delay=0.02):
    # Action_all(True)
    key_series('f')
    def Action_all(event):
        delay=0.02
        if isinstance(event, ButtonEvent):
                if event.button is LEFT:
                        lock.release()
                        mouse.unhook(Action_all)
                        mouse.click()
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
                elif event.button is RIGHT:
                        lock.release()
                        mouse.unhook(Action_all)
                return Action_all

    from threading import Lock
    lock = Lock()
    lock.acquire()
    Action_others=mouse.hook(Action_all)
    lock.acquire()
    return Action_all
    
    