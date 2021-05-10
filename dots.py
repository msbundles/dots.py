import random
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://msbundles.github.io/DotDrawer/')
canvas = browser.find_element_by_tag_name('body')
# The list of arrow keys to be used in randomization.
keylist = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

# Base functions


# Insert dot above
def up(it):
    print("up")
    for _ in range(it):
        time.sleep(0.2)
        canvas.send_keys(Keys.UP)
        time.sleep(0.2)


# Insert dot below
def down(it):
    for _ in range(it):
        time.sleep(0.2)
        canvas.send_keys(Keys.DOWN)
        time.sleep(0.2)


# Insert dot to the left
def left(it):
    print("left")
    for _ in range(it):
        time.sleep(0.2)
        canvas.send_keys(Keys.LEFT)
        time.sleep(0.2)


# Insert dot to the right
def right(it):
    for _ in range(it):
        time.sleep(0.2)
        canvas.send_keys(Keys.RIGHT)
        time.sleep(0.2)


# Change the distance between the dots dir is either "w" or "s" and it
# is the number of iterations. "w" is an increase in space and "s" is
# a decrease in space.
def space(it, dirchar):
    for _ in range(it):
        time.sleep(0.2)
        canvas.send_keys(dirchar)
        time.sleep(0.2)


# Set the color of the dot randomly
def randcolor():
    for _ in range(random.randrange(0, 4)):
        time.sleep(0.2)
        canvas.send_keys(2)
        time.sleep(0.2)


# Create a diagonal line of dots going up and left
def diagul(iteration, w):
    canvas.click()
    space(w, "w")
    for _ in range(iteration):
        up(1)
        time.sleep(0.1)
        left(1)
        time.sleep(0.1)


# Create a diagonal line of dots going up and right
def diagur(iteration, w):
    canvas.click()
    space(w, "w")
    for _ in range(iteration):
        up(1)
        time.sleep(0.1)
        right(1)
        time.sleep(0.1)


# Create a diagonal line of dots going down and right
def diagdr(iteration, w):
    canvas.click()
    space(w, "w")
    for _ in range(iteration):
        down(1)
        time.sleep(0.1)
        right(1)
        time.sleep(0.1)

# Main action functions


# Place dots in random directions
def randomdir(iteration):
    canvas.click()
    for _ in range(8, iteration):
        random.shuffle(keylist)
        randnum = random.randint(0, 3)
        time.sleep(0.2)
        canvas.send_keys(keylist[randnum])
        time.sleep(0.2)


# Draw a multicolored square
def mcs(iup, idown, ileft, iright, w):
    canvas.click()
    space(w, "w")
    randcolor()
    up(iup)
    randcolor()
    right(iright)
    randcolor()
    down(idown)
    randcolor()
    left(ileft)


# Draw a triangle
def triangle(size, width):
    space(width, "w")
    left(size*2)
    diagur(size, 0)
    diagdr(size, 0)


# Taking command line arguments
if sys.argv[1] == "mcs":
    mcs(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
if sys.argv[1] == "rand":
    randomdir(int(sys.argv[2]))
if sys.argv[1] == "diag":
    diagur(int(sys.argv[2]), int(sys.argv[3]))
if sys.argv[1] == "tri":
    triangle(int(sys.argv[2]), int(sys.argv[3]))

