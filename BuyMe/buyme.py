# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep


def get_chrome_driver():
    driver_path = "/home/shay79il/bin/chromedriver"
    return webdriver.Chrome(executable_path=driver_path)


def open_website(driver):
    with open("website_url.txt", "r") as website_file:
        website_url = website_file.readline()
    driver.maximize_window()
    driver.get(website_url)


def register_screen(driver):
    sleep(1)
    login_and_register_locator = "//span[@class='seperator-link']"
    driver.find_element_by_xpath(login_and_register_locator).click()
    sleep(1)
    # register_locator = "//span[@class='text-link theme']"
    driver.find_element_by_xpath("//span[@class='text-link theme']").click()
    name_locator = "//input[@placeholder='שם פרטי']" #'//*[@id="ember1522"]'
    mail_locator = "//input[@placeholder='מייל']" #'//*[@id="ember1525"]'
    password_locator = '//*[@id="valPass"]'
    password_validation_locator = "//input[@placeholder='אימות סיסמה']"
    submit_button_locator = "//button[@type='submit']"
    driver.find_element_by_xpath(name_locator).send_keys("Shay")
    driver.find_element_by_xpath(mail_locator).send_keys("shay79il@gmail.com")
    driver.find_element_by_xpath(password_locator).send_keys("q1W2e3r4")
    driver.find_element_by_xpath(password_validation_locator).send_keys("q1W2e3r4")
    chrome_driver.find_element_by_xpath(submit_button_locator).click()
    sleep(5)


def login_screen(driver):
    sleep(1)
    login_and_register_locator = "//span[@class='seperator-link']"
    driver.find_element_by_xpath(login_and_register_locator).click()
    sleep(1)
    email_locator = "//input[@placeholder='מייל']"
    driver.find_element_by_xpath(email_locator).send_keys("shay79il@gmail.com")
    password_locator = "//input[@placeholder='סיסמה']"
    driver.find_element_by_xpath(password_locator).send_keys("ne6gb2RQQyLkZjV")
    submit_button_locator = "//button[@type='submit']"
    chrome_driver.find_element_by_xpath(submit_button_locator).click()
    sleep(5)


def home_screen(driver):
    price_locator = "//li[text()='סכום']/..//li[@data-option-array-index='1']"
    driver.find_element_by_xpath(price_locator).click()
    area_locator = "//li[text()='אזור']/..//li[@data-option-array-index='2']"
    driver.find_element_by_xpath(area_locator).click()
    category_locator = "//option[@value='8']"
    driver.find_element_by_xpath(category_locator).click()
    search_button_locator = "//a[@href='https://buyme.co.il/search']"
    driver.find_element_by_xpath(search_button_locator).click()


chrome_driver = get_chrome_driver()
open_website(chrome_driver)
# register_screen(chrome_driver)
login_screen(chrome_driver)
home_screen(chrome_driver)