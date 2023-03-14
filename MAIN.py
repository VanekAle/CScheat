from PIL import Image, ImageGrab
from pynput.mouse import Button, Controller
import keyboard

def foo():
     img1 = ImageGrab.grab((1024/2-50,768/2-50,1024/2+50,768/2+50))
     img2 = ImageGrab.grab((1024/2-50,768/2-50,1024/2+50,768/2+50))
     if img1 != img2:
          mouse.click(Button.left, 2)

mouse = Controller()
keyboard.add_hotkey('c + Shift', foo)
