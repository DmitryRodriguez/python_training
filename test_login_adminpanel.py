# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time, unittest


class LoginToAdminPanel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def login_to_admin_panel(self):
        driver = self.driver
        driver.get("https://daily.ticketbird.com/admin/login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("atest")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("stuff-fUr-testet2")
        driver.find_element_by_id("login-form").submit()
    
    def tearDown(self):
        self.driver.quit()
