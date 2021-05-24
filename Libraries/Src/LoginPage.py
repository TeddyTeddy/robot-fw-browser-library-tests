from LibraryLoader import LibraryLoader
from LoginPageLocators import locators
from LoginPageTexts import texts
from LoginPageLinks import login_page_url
from Browser import ElementState, AssertionOperator

class LoginPage:
    """
    This Robot Library contains keywords operating on the login_page_url
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def go_to_login_page(self):
        """
        Goes to Admin Login Page specified by login_page_url. It waits until the page's login button is enabled.
        :return: None
        """
        self._loader.bl.go_to(url=login_page_url)
		# check if the login button is visible
        self._loader.bl.wait_for_elements_state(selector=locators['login_button'], state=ElementState.visible)

    def verify_title_text(self):
        self._loader.bl.get_text(selector=locators['title'], assertion_operator=AssertionOperator.equal, assertion_expected=texts['title'])

    def verify_username_text(self):
        self._loader.bl.get_text(selector=locators['username_title'], assertion_operator=AssertionOperator.equal, assertion_expected=texts['username'])

    def verify_password_text(self):
        self._loader.bl.get_text(selector=locators['password_title'], assertion_operator=AssertionOperator.equal, assertion_expected=texts['password'])

    def verify_login_button_text(self):
        self._loader.bl.get_attribute(selector=locators['login_button'], attribute='value',
            assertion_operator=AssertionOperator.equal, assertion_expected=texts['login_button'])

    def login(self, username, password):
        """
        Logins with the given credentials to admin login page. If the login attempt is successful, user is redirected to
        admin main page.
        """
        self._loader.bl.fill_secret(selector=locators['username_field'], secret=username)
        self._loader.bl.fill_secret(selector=locators['password_field'], secret=password)
        self._loader.bl.click(selector=locators['login_button'])


