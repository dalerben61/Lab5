import math
import random
from math import pi


def calculateAreaOfCircle(radius):
    area = pi * radius ** 2
    return area

def calculateMpg(miles, gallon):
    milesPerGallon = miles / gallon
    return milesPerGallon

def convertFahrenheitToCelsius(fTemp):
    cTemp = ((fTemp - 32) * 5) / 9
    return cTemp

def calculateDistanceBetweenPoints():
    x = random.randint(1,127)
    y = random.randint(1,63)
    x1 = random.randint(1,127)
    y1 = random.randint(1,63)

    distance = math.sqrt( ((x - x1) ** 2) + ((y - y1) ** 2) )
    return distance

def verticalLine():
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

def horizontalLine():
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

def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()
