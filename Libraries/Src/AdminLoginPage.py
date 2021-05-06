from LibraryLoader import LibraryLoader
from ExpectedTexts import expected
from Locators import locator
from ExpectedLinks import links, admin_login_page_url
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
        self._loader.bl.wait_for_elements_state(selector=locator['admin_login_page']['login_button'], state=ElementState.visible)
        self._verify_texts_on_admin_login_page()

    def _verify_texts_on_admin_login_page(self):
        self._loader.bl.get_text(selector=locator['admin_login_page']['title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_login_page']['title_text'])

        self._loader.bl.get_text(selector=locator['admin_login_page']['username_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_login_page']['username_text'])

        self._loader.bl.get_text(selector=locator['admin_login_page']['password_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_login_page']['password_text'])

        self._loader.bl.get_attribute(selector=locator['admin_login_page']['login_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_login_page']['login_button_text'])

    def login(self, username, password):
        """
        Logins as admin user via admin login page. If the login attempt is successful, user is redirected to
        admin main page.
        """
        self._loader.bl.fill_secret(selector=locator['admin_login_page']['username_field'],
                                   secret=username)
        self._loader.bl.fill_secret(selector=locator['admin_login_page']['password_field'],
                                    secret=password)
        self._loader.bl.click(selector=locator['admin_login_page']['login_button'])


