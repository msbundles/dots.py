from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyautogui
browser = webdriver.Firefox()
type(browser)
browser.get('https://msbundles.github.io/Bundles-Personal-Programming-Betterment/p5/1-Dots/')
canvas = browser.find_element_by_tag_name('body')
type(canvas)
canvas.click()
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
def randcol():
  for x in range(random.randrange(1, 4)):
    time.sleep(0.1)
    canvas.send_keys(2)
    time.sleep(0.1)
def q(timee):
  time.sleep(timee)
  browser.quit()

def multicolorsquare():
  dist(2, "w")
  randcol()
  up(10)
  randcol()
  right(10)
  randcol()
  down(10)
  randcol()
  left(10)

multicolorsquare()
