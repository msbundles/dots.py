import random
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
type(browser)
browser.get(
    'https://msbundles.github.io/Bundles-Personal-Programming-Betterment/p5/1-Dots/')
canvas = browser.find_element_by_tag_name('body')
type(canvas)
keyl = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

# Base functions


def up(it):
    print("up")
    for it in range(1, it):
        time.sleep(0.2)
        canvas.send_keys(Keys.UP)
        time.sleep(0.2)


def upone():
    time.sleep(0.2)
    canvas.send_keys(Keys.UP)
    time.sleep(0.2)


def down(it):
    for it in range(1, it):
        time.sleep(0.2)
        canvas.send_keys(Keys.DOWN)
        time.sleep(0.2)


def left(it):
    print("left")
    for it in range(1, it):
        time.sleep(0.2)
        canvas.send_keys(Keys.LEFT)
        time.sleep(0.2)


def leftone():
    time.sleep(0.2)
    canvas.send_keys(Keys.LEFT)
    time.sleep(0.2)


def right(it):
    for it in range(1, it):
        time.sleep(0.2)
        canvas.send_keys(Keys.RIGHT)
        time.sleep(0.2)


def space(it, dir):
    for it in range(1, it):
        time.sleep(0.2)
        canvas.send_keys(dir)
        time.sleep(0.2)


def randcolor():
    for _ in range(random.randrange(1, 4)):
        time.sleep(0.2)
        canvas.send_keys(2)
        time.sleep(0.2)


def q(tim):
    time.sleep(tim)
    browser.quit()
# end of base functions

# main action functions


def randdir(iteration):
    canvas.click()
    for iteration in range(1, iteration):
        random.shuffle(keyl)
        randnum = random.randint(0, 3)
        time.sleep(0.2)
        canvas.send_keys(keyl[randnum])
        time.sleep(0.2)

# Multi colored square function


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


def diag(iteration, w):
    canvas.click()
    space(w, "w")
    for iteration in range(1, iteration):
        upone()
        time.sleep(0.2)
        leftone()
        time.sleep(0.2)
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
    randdir(in2)
if sys.argv[1] == "diag":
    in2 = int(sys.argv[2])
    in3 = int(sys.argv[3])
    diag(in2, in3)
