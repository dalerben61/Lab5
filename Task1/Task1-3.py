from gfxhat import lcd
from gfxhat import backlight

def staircase(w, h):
    lcd.clear()
    lcd.show()

    x = 15
    y = 8

    while x >= 0 and x <= 127 and y >=0 and y <= 63:
        a = 0
        b = 0

        for a in range(0,w):
            lcd.set_pixel(x,y,1)
            x = x + 1
            if a == w - 1 or x == 127:
                break
        
        for b in range(0,h):
            lcd.set_pixel(x,y,1)
            y = y + 1
            if b == h - 1 or y == 127:
                break

    
    backlight.set_all(0,255,0)
    backlight.show()
    lcd.show()
    return


width = int(input("Set the width of one stair. "))
height = int(input("Set the height of one stair. "))
staircase(width, height)