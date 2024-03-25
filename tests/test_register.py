from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Muhibur", "Marjan", self.generate_email_with_timestamp(), "9799996632", "12345", "12345", "no", "select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message() == expected_heading_text

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Muhibur", "Marjan", self.generate_email_with_timestamp(), "9799996632", "12345", "12345", "yes", "select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message() == expected_heading_text

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Muhibur", "Marjan", "muhiburmrazan@gmail.com", "9799996632", "12345", "12345", "yes", "select")
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_message)

    def test_without_entering_any_field(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("", "", "", "", "", "", "no", "no")
        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!", "First Name must be between 1 and 32 characters!", "Last Name must be between 1 and 32 characters!", "E-Mail Address does not appear to be valid!", "Telephone must be between 3 and 32 characters!", "Password must be between 4 and 20 characters!")

