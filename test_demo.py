# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time


class TestLoginM2LTestinSelenium():
    def setup_method(self, method):
        # options = Options()
        # options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_loginM2LTestinSelenium(self):
        self.driver.get("https://med2lab.com/")
        # self.driver.set_window_size(1696, 1026)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys(
            "K4_kiat.neo@med2lab.com")
        self.driver.find_element(
            By.NAME, "password").send_keys("K4_kiat.neo@2021")
        self.driver.find_element(By.ID, "button_submit_form").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,".userName").click()
        time.sleep(2)
        # element = self.driver.find_element(
        #     By.CSS_SELECTOR, ".Acc__item:nth-child(2) .Acc__button")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # self.driver.find_element(By.CSS_SELECTOR, ".userName__text").click()
        # self.driver.find_element(By.NAME, "userName").click()
        self.driver.find_element(By.CSS_SELECTOR, ".logout").click()
        time.sleep(2)
