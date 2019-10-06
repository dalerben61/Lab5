from gfxhat import lcd
from gfxhat import backlight

def staircase():
    lcd.clear()
    lcd.show()

    x = 15
    y = 8
    w = int(input("Input the width of one stair. "))
    h = int(input("Set the height of one stair. "))

    while x >= 0 and x <= 127 and y >=0 and y <= 63:
        for x in range(w):
            lcd.set_pixel(x,y,1)
            x = x + 1
        
        for y in range(h):
            lcd.set_pixel
            y = y + 1

    backlight.set_all(0,255,0)
    backlight.show()
    lcd.show()


