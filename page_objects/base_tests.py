import time
import random
from utilities.custom_logger import LogGen
from selenium.webdriver.common.by import By
from page_objects import page_locators as locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class baseTest():
    logger = LogGen.loggen()

    def __init__(self,driver):
        self.driver = driver

    def dob(self):
        time.sleep(15)
        self.driver.find_element(By.XPATH, locators.DATE_OF_BIRTH).click()
        self.driver.find_element(By.XPATH, locators.DOB_YEAR).click()
        self.driver.find_element(By.XPATH, locators.DOB_MONTH).click()
        self.driver.find_element(By.XPATH, locators.DOB_DATE).click()
        self.logger.info("******* DOB -> Success *******")

    def salary_range(self):
        random_number = random.randrange(1,5)
        if random_number == 1:
            self.driver.find_element(By.XPATH, locators.SALARY_RANGE_1).click()
        elif random_number == 2:
            self.driver.find_element(By.XPATH, locators.SALARY_RANGE_2).click()
        elif random_number == 3:
            self.driver.find_element(By.XPATH, locators.SALARY_RANGE_3).click()
        elif random_number == 4:
            self.driver.find_element(By.XPATH, locators.SALARY_RANGE_4).click()
        else:
            self.driver.find_element(By.XPATH, locators.SALARY_RANGE_5).click()
        self.logger.info("******* Salary range -> Success *******")

    def premium_payment_option(self):
        random_number = random.randrange(1, 2)
        if random_number == 1:
            self.driver.find_element(By.XPATH, locators.PREMIUM_PAYMENT_OPTION_1).click()
        else:
            self.driver.find_element(By.XPATH, locators.PREMIUM_PAYMENT_OPTION_2).click()
        self.driver.find_element(By.XPATH, locators.NEXT_BUTTON).click()
        time.sleep(15)
        self.logger.info("******* Premium payment option -> Success *******")

    def terms_and_conditions(self):
        self.driver.find_element(By.XPATH, locators.TERMS_AND_CONDITIONS).click()
        self.driver.find_element(By.XPATH, locators.QUOTE_TERMS_AND_CONDITIONS).click()
        self.driver.find_element(By.XPATH, locators.NEXT_BUTTON_POLICY_ISSUANCE).click()
        self.logger.info("******* Terms and conditions -> Success *******")

    def title(self):
        random_number = random.randrange(1,3)
        if random_number == 1:
            self.driver.find_element(By.XPATH,locators.TITLE_MR).click()
        elif random_number == 2:
            self.driver.find_element(By.XPATH,locators.TITLE_MRS).click()
        else:
            self.driver.find_element(By.XPATH,locators.TITLE_MS).click()
        self.logger.info("******* Title -> Success *******")

    def full_name(self):
        random_number = random.randrange(1, 5)
        name = self.driver.find_element(By.XPATH, locators.FULL_NAME)
        if random_number == 1:
            name.send_keys('Sachin Tendulkar')
        elif random_number == 2:
            name.send_keys('Yuvraj Singh')
        elif random_number == 3:
            name.send_keys('Rohit Sharma')
        elif random_number == 4:
            name.send_keys('Surya Kumar yadav')
        else:
            name.send_keys('Rishab Pant')
        self.logger.info("******* Full name -> Success *******")

    def nationality(self):
        self.driver.find_element(By.XPATH, locators.NATIONALITY_DROPDOWN).click()
        self.driver.find_element(By.XPATH, locators.NATIONALITY_SELECTION).click()
        self.logger.info("******* Nationality -> Success *******")

    def email(self):
        self.driver.find_element(By.XPATH, locators.EMAIL).send_keys('test_user@gmail.com')
        self.logger.info("******* Email -> Success *******")

    def phone_number(self):
        self.driver.find_element(By.XPATH, locators.MOBILE_NO).send_keys('501234567')
        self.logger.info("******* Phone number -> Success *******")

    def emirates_id(self):
        driver = self.driver
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, locators.EMIRATES_ID)))
        element.click()
        element.send_keys('100000000000')
        self.logger.info("******* Emirates id -> Success *******")

    def emirates_id_expiry(self):
        self.driver.find_element(By.XPATH, locators.EMIRATES_ID_EXPIRY).click()
        self.driver.find_element(By.XPATH, locators.EMIRATES_ID_EXPIRY_YEAR_DROPDOWN).click()
        self.driver.find_element(By.XPATH, locators.EMIRATES_ID_EXPIRY_YEAR).click()
        self.driver.find_element(By.XPATH, locators.EMIRATES_ID_EXPIRY_MONTH_DROPDOWN).click()
        self.driver.find_element(By.XPATH, locators.EMIRATES_ID_EXPIRY_MONTH).click()
        self.driver.find_element(By.XPATH, locators.EMIRATES_ID_EXPIRY_DATE).click()
        self.driver.find_element(By.XPATH, locators.NEXT_SUMMARY).click()
        self.logger.info("******* Emirates id expiry -> Success *******")


    def confirm_and_buy_now(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, locators.CONFIRM_AND_BUY_NOW).click()
        self.logger.info("******* Confirm and buy now -> Success *******")

    def payment_and_reference(self):
        time.sleep(15)
        self.driver.find_element(By.XPATH, locators.GENERATE_INVOICE).click()
        self.driver.find_element(By.XPATH, locators.PAYMENT_REFERENCE).send_keys('12345')
        self.driver.find_element(By.XPATH, locators.CONITNUE_BUTTON).click()
        self.logger.info("******* Payment reference-> Success *******")

    def download_policy(self):
        time.sleep(15)
        self.driver.find_element(By.XPATH, locators.DOWNLOAD_POLICY).click()
        self.logger.info("******* Download policy -> Success *******")



