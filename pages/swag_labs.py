from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator = 'div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def is_name_field_present(self):
        try:
            self.find_element(locator = '#user-name')
        except NoSuchElementException:
            return False
        return True

    def is_password_field_present(self):
        try:
            self.find_element(locator = '#password')
        except NoSuchElementException:
            return False
        return True