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
        driver.find_element_by_id("nblogin").click()
        alert = driver.switch_to.alert()
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Google")))
        except NoSuchElementException:
            time.sleep(1)

        driver.find_element_by_link_text("Google").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectPopUp |  | ]]
        for i in range(10):
            try:
                if self.is_element_present(By.ID, "account-chooser-link"):
                    break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("account-chooser-link").click()
        driver.find_element_by_id("account-chooser-add-account").click()
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("imdbtest0@gmail.com")
        for i in range(10):
            try:
                if "" == driver.find_element_by_id("next").text:
                    break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "next"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("next").click()
        for i in range(10):
            try:
                if self.is_element_present(By.ID, "Passwd"):
                    break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("Passwd").clear()
        driver.find_element_by_id("Passwd").send_keys("Password!@#$5")
        driver.find_element_by_id("signIn").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
