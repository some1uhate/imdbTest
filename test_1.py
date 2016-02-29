# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.imdb.com/"
        self.verificationErrors = []

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("nblogin").click()
        driver.switch_to.frame(driver.find_element_by_class_name("cboxIframe"))
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Google")))
        driver.find_element_by_link_text("Google").click()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("imdbtest0@gmail.com")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "next")))
        driver.find_element_by_id("next").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "Passwd")))
        driver.find_element_by_id("Passwd").clear()
        driver.find_element_by_id("Passwd").send_keys("Password!@#$5")
        driver.find_element_by_id("signIn").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
