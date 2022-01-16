from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import os


def question_a():
  """
  Write a program that does the following:
  1. Write a script which will open the following:
      a - Chrome – http://www.walla.co.il
      b - FireFox – http://www.ynet.co.il
  """
  chrome_driver_path = "/home/shay79il/bin/chromedriver"
  firefox_driver_path = "/home/shay79il/bin/geckodriver"
  my_chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)
  my_firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path)
  chrome_url = "https://walla.co.il"
  firefox_url = "https://ynet.co.il"
  my_chrome_driver.maximize_window()
  my_firefox_driver.maximize_window()
  my_chrome_driver.get(chrome_url)
  my_firefox_driver.get(firefox_url)
  my_chrome_driver.close()
  my_firefox_driver.close()


def solution_b():
  """
  In one of the browsers you open do the following:
      a- Create a variable with the website’s title
      b- Refresh website
      c- Get website name and compare it to the variable you created in a.
  """
  chrome_url = "/home/shay79il/bin/chromedriver"
  my_chrome_driver = webdriver.Chrome(executable_path=chrome_url)
  my_chrome_driver.maximize_window()
  my_chrome_driver.get("https://www.walla.co.il")
  get_title = my_chrome_driver.title
  print(get_title)
  my_chrome_driver.refresh()
  print(my_chrome_driver.title == get_title)
  my_chrome_driver.close()


def solution_c():
  """
  Open a few browsers, locate any element, does the
  element has the same locators in the other browser?
  """
  chrome_driver_path = "/home/shay79il/bin/chromedriver"
  firefox_driver_path = "/home/shay79il/bin/geckodriver"
  my_chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)
  my_firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path)
  url = "https://github.com"
  my_chrome_driver.maximize_window()
  my_firefox_driver.maximize_window()
  my_chrome_driver.get(url)
  my_firefox_driver.get(url)
  sleep(6)
  chrome_elem_xpath = '/html/body/div[1]/header/div/div[2]/nav/ul/li[1]/details/summary'
  firefox_elem_xpath = '/html/body/div[1]/header/div/div[2]/nav/ul/li[1]/details/summary'
  chrome_text = my_chrome_driver.find_element_by_xpath(chrome_elem_xpath).text
  firefox_text = my_firefox_driver.find_element_by_xpath(firefox_elem_xpath).text
  print(f"chrome_text  is --->> {chrome_text}")
  print(f"firefox_text is --->> {firefox_text}")
  print("After checking with copy shortcut I found that")
  print("Chrome and Firefox have the SAME locators!!")
  my_chrome_driver.quit()
  my_firefox_driver.quit()
  if chrome_text == firefox_text:
      print("locators are the Same!")
  else:
      print("locators are NOT the Same!")


def solution_d():
  """
  Create a test with the following:
   Open Google Translate web page
   Write anything in Hebrew in the text area
  """
  driver_path = "/home/shay79il/bin/chromedriver"
  chrome_driver = webdriver.Chrome(executable_path=driver_path)
  chrome_driver.maximize_window()
  chrome_driver.get("https://translate.google.com/")
  chrome_driver.find_element_by_xpath("//span/div/textarea").send_keys("חתול")
  sleep(10)
  chrome_driver.quit()


def solution_e():
  """
   Open YouTube web page
   Type a name of a song
   Click on search.
  """
  driver_path = "/home/shay79il/bin/chromedriver"
  chrome_driver = webdriver.Chrome(executable_path=driver_path)
  chrome_driver.maximize_window()
  chrome_driver.get("https://youtube.com")
  sleep(6)
  locator = '//input[@id="search"]'
  chrome_driver.find_element_by_xpath(locator).send_keys("hakuna matata")
  chrome_driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
  sleep(10)
  chrome_driver.quit()


def solution_f():
  """
   Open Chrome browser on Google Translate website:
   Find translation text field (the one you send keys to)
  with 3 different locators and print the WebElement you created.
  """
  driver_path = "/home/shay79il/bin/chromedriver"
  chrome_driver = webdriver.Chrome(executable_path=driver_path)
  chrome_driver.maximize_window()
  chrome_driver.get("https://translate.google.com/")
  locator1 = "//textarea[@jsname='BJE2fc']"
  locator2 = "//textarea[@role='combobox']"
  locator3 = ".QFw9Te .er8xn"
  chrome_driver.find_element_by_xpath(locator1).send_keys("hakuna matata\n")
  chrome_driver.find_element_by_xpath(locator2).send_keys("hakuna matata\n")
  chrome_driver.find_element_by_css_selector(locator3).send_keys("hakuna matata\n")
  sleep(5)
  chrome_driver.quit()


def solution_g():
  """
   Open Chrome browser on Facebook website
   Login into Facebook (No need to send me credentials).
  """
  driver_path = "/home/shay79il/bin/chromedriver"
  chrome_driver = webdriver.Chrome(executable_path=driver_path)
  chrome_driver.maximize_window()
  chrome_driver.get("https://facebook.com")
  sleep(6)
  email_locator = '//*[@id="email"]'
  password_locator = '//*[@id="pass"]'
  submit_locator = "//button[@name='login']"
  chrome_driver.find_element_by_xpath(email_locator).send_keys("shay79il@gmail.com")
  chrome_driver.find_element_by_xpath(password_locator).send_keys("xxxxxxx")
  chrome_driver.find_element_by_xpath(submit_locator).click()
  sleep(10)
  chrome_driver.quit()


def solution_h():
  """
   Open Chrome browser on any webpage.
   Delete all cookies from browser.
   Make sure all cookies are deleted by
      printing all cookies stored in the browser.
  """
  driver_path = "/home/shay79il/bin/chromedriver"
  chrome_driver = webdriver.Chrome(executable_path=driver_path)
  chrome_driver.maximize_window()
  chrome_driver.get("https://facebook.com")
  sleep(3)
  print(chrome_driver.get_cookies())
  chrome_driver.delete_all_cookies()
  print(f"Deleting all cookies finished, current cookies = {chrome_driver.get_cookies()}")
  chrome_driver.quit()


def solution_i():
  """
   Open any browser on "GitHub" website.
   Enter “Selenium” keyword in search textfield
   Press Enter to search (through code - of course).
  """
  driver_path = "/home/shay79il/bin/chromedriver"
  chrome_driver = webdriver.Chrome(executable_path=driver_path)
  chrome_driver.maximize_window()
  chrome_driver.get("https://github.com")
  sleep(3)
  locator = "//input[@placeholder='Search GitHub']"
  chrome_driver.find_element_by_xpath(locator).send_keys("Selenium")
  chrome_driver.find_element_by_xpath(locator).send_keys(Keys.ENTER)
  sleep(3)
  chrome_driver.quit()


def solution_j():
  """
   Find a way to disable all extensions in
      o Chrome
      o Firefox
      o Internet Explorer.
   Run browsers without extensions.
  """
  # chrome_options = Options()
  # chrome_options.add_argument("--disable-extensions")
  # chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
  # chrome_driver.quit()
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("no-sandbox")
  chrome_options.add_argument("--disable-extensions")
  driver = os.path.join("/home/shay79il/bin/chromedriver")
  browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)
  browser.maximize_window()
  browser.get("https://www.google.com")
  sleep(5)
  browser.quit()
