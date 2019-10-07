import time
from deli0061Library import clearBacklight
from deli0061Library import verticalLine
from deli0061Library import horizontalLine
from deli0061Library import staircase
from deli0061Library import randomPixels

print("This program executes different GFX Hat functions, and a 5th one that resets the backlight every time a function is done executing.")
print("Let's start by drawing a vertical line.")
clearBacklight()

time.sleep(5)

x = int(input("Set a value for x. "))
verticalLine(x)

time.sleep(5)

print("Now how about we draw a horizontal line.")
clearBacklight()

time.sleep(2)

y = int(input("Set a value for y. "))
horizontalLine(y)

time.sleep(5)

print("Ok! Let's use some RNG to draw random pixel on the Hat.")
clearBacklight()

time.sleep(2)

length = float(input("For how much seconds will the program show random pixels on the GFX Hat? "))
randomPixels(length)

time.sleep(5)

print("Alright! Earlier we've drawn a horizontal line and a vertical line.")
print("Let's combine both and draw a staircase!")
clearBacklight()

time.sleep(3)

#If you set the width to 20, and height to 5, this last part seems to work
width = int(input("Set the width of one stair. "))
height = int(input("Set the height of one stair. "))
staircase(width, height)