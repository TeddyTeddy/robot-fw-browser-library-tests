from LibraryLoader import LibraryLoader
from AdminLoginPageLocators import locators
from AdminLoginPageTexts import texts
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
        Once the login button is loaded, it checks title, username, password, and
        login_button for correctness.
        :return: None
        """
        self._loader.bl.go_to(url=admin_login_page_url)
		# check if the login button is visible
        self._loader.bl.wait_for_elements_state(selector=locators['login_button'], state=ElementState.visible)
        self._verifys_on_admin_login_page()

    def _verifys_on_admin_login_page(self):
        self._loader.bl.get_text(selector=locators['title'], assertion_operator=AssertionOperator.equal, assertion_expected=texts['title'])

        self._loader.bl.get_text(selector=locators['username_title'], assertion_operator=AssertionOperator.equal, assertion_expected=texts['username'])

        self._loader.bl.get_text(selector=locators['password_title'], assertion_operator=AssertionOperator.equal, assertion_expected=texts['password'])

        self._loader.bl.get_attribute(selector=locators['login_button'], attribute='value',
            assertion_operator=AssertionOperator.equal, assertion_expected=texts['login_button'])

    def login(self, username, password):
        """
        Logins as admin user via admin login page. If the login attempt is successful, user is redirected to
        admin main page.
        """
        self._loader.bl.fill_secret(selector=locators['username_field'], secret=username)
        self._loader.bl.fill_secret(selector=locators['password_field'], secret=password)
        self._loader.bl.click(selector=locators['login_button'])


