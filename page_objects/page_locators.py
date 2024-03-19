# URL
BASE_URL = 'https://client-platform2.democrance.com/d2c/policy/critical-illness-one-product/form/information'
OPEN_AI_KEY = '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'


# STEP - 1
PAGE_TITLE = '/html/head/title'
HEADER_IMAGE = '//*[@id="header"]/nav/div/div[2]/img'
DATE_OF_BIRTH = "//*[@id='insured_age']"
DOB_YEAR = '//*[@id="insured_age"]//option[28]'
DOB_MONTH = '//*[@id="insured_age"]//div[1]/span/select/option[6]'
DOB_DATE = '//*[@id="insured_age"]//div[2]/a[3]'
POLICY_EFFECTIVE_DATE = '//*[@id="policy_effective_date"]'
SALARY_RANGE_1 = '//*[@id="salary_range"]//*[text()="AED 0 - AED 4,00"]'
SALARY_RANGE_2 = '//*[@id="salary_range"]//*[text()="AED 4,001 - AED 10,000"]'
SALARY_RANGE_3 = '//*[@id="salary_range"]//*[text()="AED 10,001 - AED 20,000"]'
SALARY_RANGE_4 = '//*[@id="salary_range"]//*[text()="AED 20,001 - AED 30,000"]'
SALARY_RANGE_5 = '//*[@id="salary_range"]//*[text()="Above 30,000"]'
PREMIUM_PAYMENT_OPTION_1 = '//*[@id="premium_payment"]//*[text()="Monthly"]'
PREMIUM_PAYMENT_OPTION_2 = '//*[@id="premium_payment"]//*[text()="Annually"]'
NEXT_BUTTON = '//*[@id="buttonsBar"]/div/button'


# STEP - 2
TERMS_AND_CONDITIONS = '//*[@id="formsWrapper"]//div[1]/label/span[1]'
QUOTE_TERMS_AND_CONDITIONS = '//*[@id="formsWrapper"]//div[2]/label/span[1]'
NEXT_BUTTON_POLICY_ISSUANCE = '//*[@id="buttonsBar"]//*[text()="Next: Policy issuance and Payment"]'

# STEP - 3
TITLE_MR = '//*[@id="title"]//*[text()="Mr"]'
TITLE_MRS = '//*[@id="title"]//*[text()="Mrs"]'
TITLE_MS = '//*[@id="title"]//*[text()="Ms"]'
FULL_NAME = '//input[@name="full_name"]'
NATIONALITY_DROPDOWN = '//*[@id="nationality"]//*[@class="input is-success"]'
NATIONALITY_SELECTION = '//*[@id="nationality"]//a[103]'
EMAIL = '//*[@id="email_address"]//*[@class="input"]'
MOBILE_NO = '//*[@id="mobile"]//*[@class="vti__input input"]'
EMIRATES_ID = '.masked'
EMIRATES_ID_EXPIRY = '//*[@id="emirates_id_expiry_date"]'
EMIRATES_ID_EXPIRY_YEAR_DROPDOWN = '//*[@id="emirates_id_expiry_date"]//div[2]/span/select'
EMIRATES_ID_EXPIRY_YEAR = '//*[@id="emirates_id_expiry_date"]//option[90]'
EMIRATES_ID_EXPIRY_MONTH_DROPDOWN = '//*[@id="emirates_id_expiry_date"]//div[1]/span/select'
EMIRATES_ID_EXPIRY_MONTH = '//*[@id="emirates_id_expiry_date"]//*[text()=" December "]'
EMIRATES_ID_EXPIRY_DATE = '//*[@id="emirates_id_expiry_date"]//div[4]/a[7]'
NEXT_SUMMARY = '//*[@id="buttonsBar"]//button[2]'

# STEP - 4
CONFIRM_AND_BUY_NOW = '//*[@id="buttonsBar"]//button[2]'

# PAYMENT PAGE
GENERATE_INVOICE = '//*[text()="Generate Invoice"]'
PAYMENT_REFERENCE = '//*[@id="payment_reference"]//input'
CONITNUE_BUTTON = '//*[text()="Continue"]'

# SUCCESS BUY PAGE
POLICY_NUMBER = '//*[@id="bd"]//div[1]/h3'
DOWNLOAD_POLICY = '//*[@id="bd"]//button/span[2]'









