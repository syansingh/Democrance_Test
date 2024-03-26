import pytest
from selenium.common import NoSuchElementException
from page_objects.base_tests import baseTest
from page_objects import page_locators as locators


@pytest.mark.usefixtures("test_setup")
class TestBuyInsuranceVisualElements(baseTest):

    def test_2_dob(self):
        try:
            element = self.element_get(locators.DATE_OF_BIRTH)
            assert element.is_displayed(), "Element is not displayed"
        except NoSuchElementException:
            assert False, "Element is not present"

    def test_3_salary_range(self):
        try:
            element = self.element_get(locators.SALARY_RANGE_2)
            assert element.is_displayed(), "Element is not displayed"
        except NoSuchElementException:
            assert False, "Element is not present"

    def test_4_premium_payment_option(self):
        try:
            element = self.element_get(locators.PREMIUM_PAYMENT_OPTION_1)
            assert element.is_displayed(), "Element is not displayed"
        except NoSuchElementException:
            assert False, "Element is not present"



