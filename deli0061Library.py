import math
import random
from math import pi
from gfxhat import lcd
from gfxhat import backlight
import time


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

def verticalLine(x):
    lcd.clear()
    lcd.show()

    y = 0
    while (y <= 63):
        lcd.set_pixel(x,y,1)
        y = y + 1

    backlight.set_all(0,255,0)
    backlight.show()
    lcd.show()
    return

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

def randomPixels(length):
    lcd.clear()
    lcd.show()
    timestop = time.time() + length
    backlight.set_all(0,255,0)
    backlight.show()
    
    while time.time() <= timestop:
        x = random.randint(1,127)
        y = random.randint(1,63)
        lcd.set_pixel(x,y,1)
        lcd.show()
        time.sleep(0.2)

    return

def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()
    return