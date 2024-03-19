import pytest
from selenium.common import NoSuchElementException

from page_objects.base_tests import baseTest
from page_objects import page_locators as locators
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup")
class TestBuyInsuranceVisualELements():


    def test_2_DOB(self):
        driver = self.driver
        base = baseTest(driver)
        self.driver.get(locators.BASE_URL)
        try:
            element = self.driver.find_element(By.XPATH, locators.DATE_OF_BIRTH)
            assert element.is_displayed(), "Element is not displayed"
        except NoSuchElementException:
            assert False, "Element is not present"




