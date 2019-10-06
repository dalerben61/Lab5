from gfxhat import lcd
from gfxhat import backlight
def horizontalLine()
    lcd.clear()
    lcd.show()

    y = int(input("Set a value for y. "))
    x = 0
    while (x <= 127):
        lcd.set_pixel(x,y,1)
        x = x + 1

    backlight.set_all(0,255,0)
    backlight.show()
    lcd.show()