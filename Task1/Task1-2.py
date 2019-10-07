from gfxhat import lcd
from gfxhat import backlight

def horizontalLine(y):
    lcd.clear()
    lcd.show()

    x = 0
    while (x <= 127):
        lcd.set_pixel(x,y,1)
        x = x + 1

    backlight.set_all(0,255,0)
    backlight.show()
    lcd.show()
    return

y = int(input("Set a value for y. "))
horizontalLine(y)