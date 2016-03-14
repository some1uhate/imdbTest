from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_fixture import driver
from selenium.webdriver.common.action_chains import ActionChains


def logout(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "navUserMenu")))
    menu = driver.find_element_by_id("navUserMenu")
    ActionChains(driver).move_to_element(menu).perform()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Log Out")))
    driver.find_element_by_id("nblogout").click()


def login(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "nblogin")))
    driver.find_element_by_id("nblogin").click()
    # Switch to new pop-up
    driver.switch_to.frame(driver.find_element_by_class_name("cboxIframe"))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Google")))
    driver.find_element_by_link_text("Google").click()
    # Switch to new window
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Email")))
    driver.find_element_by_id("Email").clear()
    driver.find_element_by_id("Email").send_keys("imdbtest0@gmail.com")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "Passwd")))
    driver.find_element_by_id("Passwd").clear()
    driver.find_element_by_id("Passwd").send_keys("Password!@#$5")
    driver.find_element_by_id("signIn").click()


def test_login(driver):
    driver.get("http://www.imdb.com/")
    login(driver)
    logout(driver)

