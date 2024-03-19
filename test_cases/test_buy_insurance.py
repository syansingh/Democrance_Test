import pytest, time
from page_objects.base_tests import baseTest
from page_objects import page_locators as locators

@pytest.mark.usefixtures("test_setup")
class TestBuyInsurance():

    def test_1_D2C_buy_insurance(self):

        driver = self.driver
        base = baseTest(driver)
        self.driver.get(locators.BASE_URL)

        '''STEP-1'''
        base.dob()
        base.salary_range()
        base.premium_payment_option()

        '''STEP-2'''
        base.terms_and_conditions()

        '''STEP-3'''
        base.title()
        base.full_name()
        base.nationality()
        base.email()
        base.phone_number()
        base.emirates_id()
        base.emirates_id_expiry()

        '''STEP-4'''
        base.confirm_and_buy_now()

        '''PAYMENT PAGE'''
        base.payment_and_reference()

        '''BUY SUCCESS PAGE'''
        base.download_policy()






