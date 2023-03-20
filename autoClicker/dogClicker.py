from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

i = 0
start = time.time()
faceUserName = "WinnieDog1234"
facePassword = "WinnieWins"

def isLoggedIn(browser):
  try:
    browser.find_element(By.XPATH, '//*[@id="nav-top"]/section[3]/div/div/button[2]/div')
  except NoSuchElementException:
    return True
  return False


def facebookLogin(browser):
  voteButton = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/article/div[3]/div/div/div/div/div/div[4]/div/div')
  voteButton.click()
  time.sleep(5)

  FreeVoteButton = browser.find_element(By.XPATH, '//*[@id="portal"]/div[2]/div/div/div/article/div[3]/div/div/div/div/div/div[4]/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div[3]/div')
  FreeVoteButton.click()
  time.sleep(3)

  facebookButton = browser.find_element(By.XPATH, '//*[@id="rmwcPortal"]/div/div[1]/div/div[2]/div[2]/div[6]/div/div/button[1]')
  facebookButton.click()
  time.sleep(5)

  userNameInput = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input')
  passwordInput = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input')
  userNameInput.send_keys(faceUserName)
  passwordInput.send_keys(facePassword)
  passwordInput.send_keys(Keys.ENTER)
  time.sleep(3)

  #Confirmation button may appear
  url = browser.current_url
  if url.startswith("https://www.facebook"):
    confirmButton = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div')
    confirmButton.click()
  time.sleep(3)




isHeadless = input("Would you like to run in headless mode (y/n)? ")

if isHeadless == 'y':
  sys.stdout.write("Running as headless... ")
  sys.stdout.flush()
  options = Options()
  options.add_argument( #Stack Overflow says this is the solution to all my problems
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
  options.add_argument("--window-size=1920,1080")
  options.add_argument("--headless")
  browser = webdriver.Chrome(options=options)
else:
  browser = webdriver.Chrome()

browser.get('https://www.kingpet.com/dog/6722442546595564-Winnie/vote/490/?from_login=1')
time.sleep(3)  #wait for page to load

while True:

  #check if logged in
  if not isLoggedIn(browser):
    facebookLogin(browser)

  time.sleep(2)
  voteButton = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/article/div[3]/div/div/div/div/div/div[4]/div/div')
  voteButton.click()
  time.sleep(5)

  freeVoteButton = browser.find_element(By.XPATH, '//*[@id="portal"]/div[2]/div/div/div/article/div[3]/div/div/div/div/div/div[4]/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div[3]/div')
  freeVoteButton.click()
  i += 1
  voteTime = (int)(time.time() - start)

  sys.stdout.write(f"Voted {i} times in {voteTime//3600} hours {(voteTime//60)%60} minutes {voteTime%60} seconds\n")
  sys.stdout.flush()

  time.sleep(600)  #wait for 10 min

  browser.refresh()



