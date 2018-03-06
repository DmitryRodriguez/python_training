from StdSuites import null
from selenium import webdriver


def setUp():
    driver = webdriver.Chrome()
    driver.get("https://daily.ticketbird.com/")


def tearDown():
    if setUp().driver != null:
        setUp().driver.quit()

