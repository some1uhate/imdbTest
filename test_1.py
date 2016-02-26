# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.imdb.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        current_window = driver.window_handles[0]
        driver.find_element_by_id("nblogin").click()
        driver.switch_to.frame(driver.find_element_by_class_name("cboxIframe"))
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Google")))
        except NoSuchElementException:
            time.sleep(1)
        driver.find_element_by_link_text("Google").click()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("imdbtest0@gmail.com")
        try:
            self.assertTrue(self.is_element_present(By.ID, "next"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("next").click()
        try:
            self.assertTrue(self.is_element_present(By.ID, "Passwd"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        driver.find_element_by_id("Passwd").clear()
        driver.find_element_by_id("Passwd").send_keys("Password!@#$5")
        driver.find_element_by_id("signIn").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
