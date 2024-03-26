import time
import pytest
from page_objects.base_tests import baseTest


@pytest.mark.usefixtures("test_setup")
class TestBuyInsurance(baseTest):

    def test_1_D2C_buy_insurance(self):

        '''STEP-1'''
        self.dob()
        self.salary_range()
        self.premium_payment_option()

        '''STEP-2'''
        self.terms_and_conditions()

        '''STEP-3'''
        self.title()
        self.full_name()
        self.nationality()
        self.email()
        self.phone_number()
        self.emirates_id()
        self.emirates_id_expiry()

        '''STEP-4'''
        self.confirm_and_buy_now()

        '''PAYMENT PAGE'''
        self.payment_and_reference()

        '''BUY SUCCESS PAGE'''
        self.download_policy()
