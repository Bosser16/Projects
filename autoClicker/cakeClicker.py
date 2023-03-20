from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


i = 0
start = time.time()

while True:
  browser = webdriver.Chrome()
  browser.get('https://www.amazingcakeideas.com/11/17/2022/vote-join-worlds-super-exceptional-cake-decorator/4/')
  time.sleep(3)  #wait for page to load

  button = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/div/div[1]/div/article/div[2]/center[2]/div/a/span/b')
  time.sleep(3)

  button.click()
  browser.close()

  i += 1
  voteTime = (int)(time.time() - start)

  sys.stdout.write(f"Voted {i} times in {voteTime//3600} hours {(voteTime//60)%60} minutes {voteTime%60} seconds\n")
  sys.stdout.flush()

  #time.sleep(300)  #wait for 30 min

