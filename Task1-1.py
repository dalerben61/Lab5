from gfxhat import lcd
from gfxhat import backlight
def verticalLine()
    lcd.clear()
    lcd.show()

    x = int(input("Set a value for x. "))
    y = 0
    while (y <= 63):
        lcd.set_pixel(x,y,1)
        y = y + 1

    backlight.set_all(0,255,0)
    backlight.show()
    lcd.show()