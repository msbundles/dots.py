import random
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
type(browser)
browser.get('https://msbundles.github.io/DotDrawer/')
canvas = browser.find_element_by_tag_name('body')
type(canvas)
keyl = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

# Base functions

# Insert dot above
def up(it):
    print("up")
    for it in range(0, it):
        time.sleep(0.2)
        canvas.send_keys(Keys.UP)
        time.sleep(0.2)

# Insert dot below
def down(it):
    for it in range(0, it):
        time.sleep(0.2)
        canvas.send_keys(Keys.DOWN)
        time.sleep(0.2)

# Insert dot to the left
def left(it):
    print("left")
    for it in range(0, it):
        time.sleep(0.2)
        canvas.send_keys(Keys.LEFT)
        time.sleep(0.2)

# Insert dot to the right
def right(it):
    for it in range(0, it):
        time.sleep(0.2)
        canvas.send_keys(Keys.RIGHT)
        time.sleep(0.2)

# Change the distance between the dots
# dir is either "w" or "s" and it is the
# number of iterations
def space(it, dir):
    for it in range(0, it):
        time.sleep(0.2)
        canvas.send_keys(dir)
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
    for iteration in range(0, iteration):
        up(1)
        time.sleep(0.1)
        left(1)
        time.sleep(0.1)

# Create a diagonal line of dots going up and right
def diagur(iteration, w):
    canvas.click()
    space(w, "w")
    for iteration in range(0, iteration):
        up(1)
        time.sleep(0.1)
        right(1)
        time.sleep(0.1)

# Create a diagonal line of dots going down and right
def diagdr(iteration, w):
    canvas.click()
    space(w, "w")
    for iteration in range(0, iteration):
        down(1)
        time.sleep(0.1)
        right(1)
        time.sleep(0.1)

# Sleep for a specified time and then quit out of the browser
def q(tim):
    time.sleep(tim)
    browser.quit()

# end of base functions

# main action functions

# Place dots in random directions
def randomdir(iteration):
    canvas.click()
    for iteration in range(8, iteration):
        random.shuffle(keyl)
        randnum = random.randint(0, 3)
        time.sleep(0.2)
        canvas.send_keys(keyl[randnum])
        time.sleep(0.2)

# Draw a multicolored square
def mcs(u, d, l, r, w):
    canvas.click()
    space(w, "w")
    randcolor()
    up(u)
    randcolor()
    right(r)
    randcolor()
    down(d)
    randcolor()
    left(l)

# Draw a triangle
def triangle(size, width):
    space(width,"w")
    left(size*2)
    diagur(size,0)
    diagdr(size,0)

# end of main action functions
if sys.argv[1] == "mcs":
    in2 = int(sys.argv[2])
    in3 = int(sys.argv[3])
    in4 = int(sys.argv[4])
    in5 = int(sys.argv[5])
    in6 = int(sys.argv[6])
    mcs(in2, in3, in4, in5, in6)
if sys.argv[1] == "rand":
    in2 = int(sys.argv[2])
    randomdir(in2)
if sys.argv[1] == "diag":
    in2 = int(sys.argv[2])
    in3 = int(sys.argv[3])
    diagur(in2, in3)
if sys.argv[1] == "tri":
    in2 = int(sys.argv[2])
    in3 = int(sys.argv[3])
    triangle(in2, in3)

