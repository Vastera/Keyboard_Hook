# all the other meepoes hoof
import keyboard
import mouse
import time
from key_series import*
from mouse import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE




def others_hoof(delay=0.02):
    key_series('2,f')
    def Action_others(event):
        delay=0.02
        if isinstance(event, ButtonEvent):
                if event.button is LEFT:
                        lock.release()
                        mouse.unhook(Action_others)
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
                        lock.release()
                elif event.button is RIGHT:
                        lock.release()
                        mouse.unhook(Action_others)
                return Action_others

    from threading import Lock
    lock = Lock()
    lock.acquire()
    Action_others=mouse.hook(Action_others)
    lock.acquire()
    return Action_others
    

