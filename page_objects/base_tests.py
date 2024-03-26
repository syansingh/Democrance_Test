import time
import random
import logging
from traceback import print_stack
from selenium.webdriver.common.by import By
from page_objects import page_locators as locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.custom_logger import LogGen as cl


class baseTest():
    log = cl.loggen()

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        else:
            self.log.info("Locator type: " + locator_type + 'is not found')
        return False

    def element_get(self, locator, locator_type='xpath'):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info('Element found with locator: ' + locator + ' and locator_type: ' + locator_type)
        except:
            self.log.info('Element not found with locator: ' + locator + ' and locator_type: ' + locator_type)
        return element

    def element_click(self, locator, locator_type='xpath'):
        try:
            element = self.element_get(locator, locator_type)
            element.click()
            self.log.info('Clicked on element with locator: ' + locator + ' and locator type: ' + locator_type)
        except:
            self.log.info('Cannot click on element with locator: ' + locator + ' and locator type: ' + locator_type)
            print_stack()

    def element_send_keys(self, data, locator, locator_type='xpath'):
        try:
            element = self.element_get(locator, locator_type)
            element.send_keys(data)
            self.log.info('Sent data on element with locator: ' + locator + ' and locator type: ' + locator_type)
        except:
            self.log.info('Cannot send data on element with locator: ' + locator + ' and locator type: ' + locator_type)
            print_stack()

    def dob(self):
        time.sleep(15)
        self.element_click(locators.DATE_OF_BIRTH)
        self.element_click(locators.DOB_YEAR)
        self.element_click(locators.DOB_MONTH)
        self.element_click(locators.DOB_DATE)
        self.log.info("******* DOB -> Success *******")

    def salary_range(self):
        random_number = random.randrange(1,5)
        if random_number == 1:
            self.element_click(locators.SALARY_RANGE_1)
        elif random_number == 2:
            self.element_click(locators.SALARY_RANGE_2)
        elif random_number == 3:
            self.element_click(locators.SALARY_RANGE_3)
        elif random_number == 4:
            self.element_click(locators.SALARY_RANGE_4)
        else:
            self.element_click(locators.SALARY_RANGE_5)
        self.log.info("******* Salary range -> Success *******")

    def premium_payment_option(self):
        random_number = random.randrange(1, 2)
        if random_number == 1:
            self.element_click(locators.PREMIUM_PAYMENT_OPTION_1)
        else:
            self.element_click(locators.PREMIUM_PAYMENT_OPTION_2)
        self.element_click(locators.NEXT_BUTTON)
        time.sleep(15)
        self.log.info("******* Premium payment option -> Success *******")

    def terms_and_conditions(self):
        self.element_click(locators.TERMS_AND_CONDITIONS)
        self.element_click(locators.QUOTE_TERMS_AND_CONDITIONS)
        self.element_click(locators.NEXT_BUTTON_POLICY_ISSUANCE)
        self.log.info("******* Terms and conditions -> Success *******")

    def title(self):
        random_number = random.randrange(1,3)
        if random_number == 1:
            self.element_click(locators.TITLE_MR)
        elif random_number == 2:
            self.element_click(locators.TITLE_MRS)
        else:
            self.element_click(locators.TITLE_MS)
        self.log.info("******* Title -> Success *******")

    def full_name(self):
        random_number = random.randrange(1, 5)
        if random_number == 1:
            self.element_send_keys('Sachin Tendulkar', locators.FULL_NAME)
        elif random_number == 2:
            self.element_send_keys('Yuvraj Singh', locators.FULL_NAME)
        elif random_number == 3:
            self.element_send_keys('Rohit Sharma', locators.FULL_NAME)
        elif random_number == 4:
            self.element_send_keys('Surya Kumar yadav', locators.FULL_NAME)
        else:
            self.element_send_keys('Rishab Pant', locators.FULL_NAME)
        self.log.info("******* Full name -> Success *******")

    def nationality(self):
        self.element_click(locators.NATIONALITY_DROPDOWN)
        self.element_click(locators.NATIONALITY_SELECTION)
        self.log.info("******* Nationality -> Success *******")

    def email(self):
        self.element_send_keys('test_user@gmail.com', locators.EMAIL)
        self.log.info("******* Email -> Success *******")

    def phone_number(self):
        self.element_send_keys('501234567',  locators.MOBILE_NO)
        self.log.info("******* Phone number -> Success *******")

    def emirates_id(self):
        driver = self.driver
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, locators.EMIRATES_ID)))
        element.click()
        element.send_keys('100000000000')
        self.log.info("******* Emirates id -> Success *******")

    def emirates_id_expiry(self):
        self.element_click(locators.EMIRATES_ID_EXPIRY)
        self.element_click(locators.EMIRATES_ID_EXPIRY_YEAR_DROPDOWN)
        self.element_click(locators.EMIRATES_ID_EXPIRY_YEAR)
        self.element_click(locators.EMIRATES_ID_EXPIRY_MONTH_DROPDOWN)
        self.element_click(locators.EMIRATES_ID_EXPIRY_MONTH)
        self.element_click(locators.EMIRATES_ID_EXPIRY_DATE)
        self.element_click(locators.NEXT_SUMMARY)
        self.log.info("******* Emirates id expiry -> Success *******")

    def confirm_and_buy_now(self):
        time.sleep(5)
        self.element_click(locators.CONFIRM_AND_BUY_NOW)
        self.log.info("******* Confirm and buy now -> Success *******")

    def payment_and_reference(self):
        time.sleep(15)
        self.element_click(locators.GENERATE_INVOICE)
        self.element_send_keys('12345', locators.PAYMENT_REFERENCE)
        self.element_click(locators.CONITNUE_BUTTON)
        self.log.info("******* Payment reference-> Success *******")

    def download_policy(self):
        time.sleep(15)
        self.element_click(locators.DOWNLOAD_POLICY)
        self.log.info("******* Download policy -> Success *******")





