from gfxhat import lcd
from gfxhat import backlight
import time
import random

def randomPixels():
    lcd.clear()
    lcd.show()
    length = float(input("For how much seconds will the program show random pixels on the GFX Hat? "))
    timestop = time.time() + length
    backlight.set_all(0,255,0)
    backlight.show()
    
    while time.time() <= timestop:
        x = random.randint(1,127)
        y = random.randint(1,63)
        lcd.set(x,y,1)
        lcd.show()
        time.sleep(0.2)
    
