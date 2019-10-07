from gfxhat import backlight
def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()
    return

clearBacklight()
