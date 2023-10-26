"""
 Welcome Screen will start our program letting
drivers know that the InfoTech Center 2023 is loading
"""

# Import Libraries Here
import time
import sys

timetosleep = 2

print("\nWelcome - Infotech Center 2023\n")
time.sleep(timetosleep)

#Add code to have the ellipsis add a dot evey .5 seconds
x = 0
ellipsis= 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading..." + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first, so, message is printed on top of the previous line
    time.sleep(0.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Loaded - Brain Data Chip Scanned - Access Granted")

