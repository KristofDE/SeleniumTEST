# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SeleniumTestKZ(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.soastastore.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_selenium_test_k_z(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Store").click()
        driver.find_element_by_id("product_160_submit_button").click()
        driver.find_element_by_id("product_158_submit_button").click()
        driver.find_element_by_id("product_157_submit_button").click()
        driver.find_element_by_id("product_155_submit_button").click()
        driver.find_element_by_link_text("Checkout").click()
        driver.find_element_by_css_selector("input.remove_button").click()
        driver.find_element_by_link_text("Black Swan").click()
        Select(driver.find_element_by_name("product_rating")).select_by_visible_text("3")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
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
