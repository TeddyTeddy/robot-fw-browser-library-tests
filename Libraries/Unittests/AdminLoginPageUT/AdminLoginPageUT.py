import unittest
from mockito import unstub, verify, expect, verifyNoUnwantedInteractions
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from BrowserLibraryStub import configure_mock_calls_in_login
from Locators import locator
from CommonVariables import get_variables
from AdminLoginPage import AdminLoginPage
from ExpectedLinks import admin_login_page_url
from ExpectedTexts import expected
from Browser import ElementState, AssertionOperator

class AdminLoginPageUT(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(AdminLoginPageUT, self).__init__(*args, **kwargs)
        self.credentials = get_variables()['CREDENTIALS']

    def setUp(self) -> None:  # before running an individual test case
        # instantiate a mock LibraryLoader, which returns a mock bl
        LibraryLoaderStub.configure_mock_library_loader()

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    def test_go_to_admin_login_page(self):
        # in method under test, stub the expected function calls with correct arguments
        expect(LibraryLoader.get_instance().bl, times=1).go_to(url=admin_login_page_url)

        expect(LibraryLoader.get_instance().bl, times=1).wait_for_elements_state(
            selector=locator['admin_login_page']['login_button'], state=ElementState.visible)

        expect(LibraryLoader.get_instance().bl, times=1).get_text(
            selector=locator['admin_login_page']['title'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['admin_login_page']['title_text'])

        expect(LibraryLoader.get_instance().bl, times=1).get_text(
            selector=locator['admin_login_page']['username_title'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['admin_login_page']['username_text'])

        expect(LibraryLoader.get_instance().bl, times=1).get_text(
                selector=locator['admin_login_page']['password_title'],
                assertion_operator=AssertionOperator.equal,
                assertion_expected=expected['admin_login_page']['password_text'])

        expect(LibraryLoader.get_instance().bl, times=1).get_attribute(
            selector=locator['admin_login_page']['login_button'],
            attribute='value',
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['admin_login_page']['login_button_text'])

        # CUT gets magically the mock instances (i.e. _loader & bl)
        admin_login_page = AdminLoginPage()

        # method under test gets called
        admin_login_page.go_to_admin_login_page()

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_login_long_way(self):
        configure_mock_calls_in_login(
            bl=LibraryLoader.get_instance().bl
        )
        # CUT gets magically the mock instances (i.e. _loader & bl)
        admin_login_page = AdminLoginPage()

        # method under test gets called
        admin_login_page.login(self.credentials['valid_admin']['username'],
                               self.credentials['valid_admin']['password'])

        # verify that correct mock instance bl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().bl, times=1).fill_secret(
            selector=locator['admin_login_page']['username_field'],
            secret=self.credentials['valid_admin']['username'])

        verify(LibraryLoader.get_instance().bl, times=1).fill_secret(
            selector=locator['admin_login_page']['password_field'],
            secret=self.credentials['valid_admin']['password'])

        verify( LibraryLoader.get_instance().bl, times=1).click( selector=locator['admin_login_page']['login_button'] )

    def test_login_short_way(self):
        # stub the expected function calls in method under test
        expect(LibraryLoader.get_instance().bl, times=1).fill_secret(
            selector=locator['admin_login_page']['username_field'],
            secret=self.credentials['valid_admin']['username']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl, times=1).fill_secret(
            selector=locator['admin_login_page']['password_field'],
            secret=self.credentials['valid_admin']['password']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl, times=1).click(
            selector=locator['admin_login_page']['login_button']).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & bl)
        admin_login_page = AdminLoginPage()

        # method under test gets called
        admin_login_page.login(self.credentials['valid_admin']['username'],
                               self.credentials['valid_admin']['password'])

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()


if __name__ == '__main__':
    unittest.main()
