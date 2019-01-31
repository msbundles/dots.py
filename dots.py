from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
#import pyautogui
browser = webdriver.Firefox()
type(browser)
browser.get('https://msbundles.github.io/Bundles-Personal-Programming-Betterment/p5/1-Dots/')
canvas = browser.find_element_by_tag_name('body')
type(canvas)
keyl = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
canvas.click()
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
  for x in range(random.randrange(1, 4)):
    time.sleep(0.1)
    canvas.send_keys(2)
    time.sleep(0.1)
def q(timee):
  time.sleep(timee)
  browser.quit()
#end of base functions

#main action functions
def randomdir(iteration1, iteration2):
  for iteration1 in range(1, iteration1):
    for iteration2 in range(1, iteration2):
      randnum = random.randint(0,3)
      time.sleep(0.1)
      canvas.send_keys(keyl[randnum])
      time.sleep(0.1)
def multicolorsquare():
  dist(2, "w")
  randcolor()
  up(10)
  randcolor()
  right(10)
  randcolor()
  down(10)
  randcolor()
  left(10)
#end of main action functions

randomdir(200,300)