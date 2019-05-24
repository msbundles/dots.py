from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
#import pyautogui
browser = webdriver.Firefox()
type(browser)
browser.get('https://msbundles.github.io/Bundles-Personal-Programming-Betterment/p5/1-Dots/')
canvas = browser.find_element_by_tag_name('body')
type(canvas)
keyl = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

#Base functions
def up (iteration):
  for iteration in range(1,iteration):
    time.sleep(0.1)
    canvas.send_keys(Keys.UP)
    time.sleep(0.1)

def down(iteration):
  for iteration in range(1, iteration):
    time.sleep(0.1)
    canvas.send_keys(Keys.DOWN)
    time.sleep(0.1)

def left(iteration):
  for iteration in range(1, iteration):
    time.sleep(0.1)
    canvas.send_keys(Keys.LEFT)
    time.sleep(0.1)

def right(iteration):
  for iteration in range(1, iteration):
    time.sleep(0.1)
    canvas.send_keys(Keys.RIGHT)
    time.sleep(0.1)

def dist(iteration,dir):
  for iteration in range(1, iteration):
    time.sleep(0.1)
    canvas.send_keys(dir)
    time.sleep(0.1)

def randcolor():
  for i in range(random.randrange(1, 4)):
    time.sleep(0.1)
    canvas.send_keys(2)
    time.sleep(0.1)

def q(timee):
  time.sleep(timee)
  browser.quit()
#end of base functions

#main action functions
def randdir(iteration):
  canvas.click()
  for iteration in range(1, iteration):
    random.shuffle(keyl)
    randnum = random.randint(0,3)
    time.sleep(0.1)
    canvas.send_keys(keyl[randnum])
    time.sleep(0.1)
def mcs(u,d,l,r,w):
  canvas.click()
  dist(w, "w")
  randcolor()
  up(u)
  randcolor()
  right(r)
  randcolor()
  down(d)
  randcolor()
  left(l)
def diag(iteration,w):
  canvas.click()
  dist(w, "w")
  for iteration in range(1, iteration):
    up(1)
    left(1)
#end of main action functions
if sys.argv[1] == "mcs":
  in2 = int(sys.argv[2])
  in3 = int(sys.argv[3])
  in4 = int(sys.argv[4])
  in5 = int(sys.argv[5])
  in6 = int(sys.argv[6])
  mcs(in2, in3, in4, in5, in6)
elif sys.argv[1] == "rand":
  in2 = int(sys.argv[2])
  randdir(in2)
elif sys.argv[1] == "diag":
  in2 = int(sys.argv[2])
  in3 = int(sys.argv[3])
  diag(in2,in3)
