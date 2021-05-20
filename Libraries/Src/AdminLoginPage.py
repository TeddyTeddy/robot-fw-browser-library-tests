from LibraryLoader import LibraryLoader
from ExpectedTexts import expected
from AdminLoginPageLocators import *
from AdminLoginPageTexts import *
from AdminLoginPageLinks import admin_login_page_url
from Browser import ElementState, AssertionOperator

class AdminLoginPage:
    """
    This Robot Library contains keywords operating on the admin_login_page_url
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def go_to_admin_login_page(self):
        """
        Goes to Admin Login Page specified by admin_login_page_url. It waits until the page's login button is enabled.
        Once the login button is loaded, it checks title_text, username_text, password_text, and
        login_button_text for correctness.
        :return: None
        """
        self._loader.bl.go_to(url=admin_login_page_url)
		# check if the login button is visible
        self._loader.bl.wait_for_elements_state(selector=login_button, state=ElementState.visible)
        self._verify_texts_on_admin_login_page()

    def _verify_texts_on_admin_login_page(self):
        self._loader.bl.get_text(selector=title, assertion_operator=AssertionOperator.equal, assertion_expected=title_text)

        self._loader.bl.get_text(selector=username_title, assertion_operator=AssertionOperator.equal, assertion_expected=username_text)

        self._loader.bl.get_text(selector=password_title, assertion_operator=AssertionOperator.equal, assertion_expected=password_text)

        self._loader.bl.get_attribute(selector=login_button, attribute='value',
            assertion_operator=AssertionOperator.equal, assertion_expected=login_button_text)

    def login(self, username, password):
        """
        Logins as admin user via admin login page. If the login attempt is successful, user is redirected to
        admin main page.
        """
        self._loader.bl.fill_secret(selector=username_field, secret=username)
        self._loader.bl.fill_secret(selector=password_field, secret=password)
        self._loader.bl.click(selector=login_button)


