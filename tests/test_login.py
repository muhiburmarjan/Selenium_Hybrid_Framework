from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):

    @pytest.mark.parametrize("email_address, password", ExcelUtils.get_data_from_excel("ExcelFiles/Qa_Foxtail.xlsx", "LoginTest"))
    def test_login_with_valid_credentials(self,email_address, password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(email_address, password)
        account_page = AccountPage(self.driver)
        assert account_page.display_status_of_edit_your_account_information()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_timestamp(), "12345")
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_text)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("marjanmuhibur@gmail.com", "12345759")
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_text)

    def test_login_with_no_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("", "")
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_text)

