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

