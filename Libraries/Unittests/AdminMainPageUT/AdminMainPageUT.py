import unittest
from mockito import unstub, verifyNoUnwantedInteractions, expect
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from CommonVariables import get_variables
from AdminMainPage import AdminMainPage     # class under test (CUT)
from ExpectedLinks import expected_admin_main_page_url, links
from ExpectedTexts import expected
from Locators import locator, number_of_add_buttons, number_of_change_buttons
from Browser import ElementState, AssertionOperator

class AdminMainPageUT(unittest.TestCase):
    def setUp(self) -> None:  # before running an individual test case
        # instantiate a mock LibraryLoader, which returns a mock bl
        LibraryLoaderStub.configure_mock_library_loader()

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    def test_go_to_admin_main_page(self):
        # configure the mock browser library for go_to_admin_main_page()'s calls
        expect(LibraryLoader.get_instance().bl).go_to(url=expected_admin_main_page_url).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & bl)
        admin_main_page = AdminMainPage()

        # method under test gets called
        admin_main_page.go_to_admin_main_page()

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_verify_admin_main_page(self):
        # configure the mock browser library for verify_admin_main_page()'s calls
        expect(LibraryLoader.get_instance().bl).wait_for_elements_state(
                selector=locator['admin_main_page']['logout'],
                state=ElementState.visible).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_url(
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected_admin_main_page_url).thenReturn(expected_admin_main_page_url)

        # configure mock calls in _verify_texts_on_admin_main_page()
        username=get_variables()['CREDENTIALS']['valid_admin']['username']
        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['main_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['main_title_text']).thenReturn(None)

        # user navigation bar on the upper right of the page
        dynamic_user_tab_text = expected['admin_main_page']['dynamic_user_tab_text'] % username.upper()
        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['admin_main_page']['welcome_user_x'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=dynamic_user_tab_text).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['view_site'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['view_site_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['change_password'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['change_password_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['logout'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['logout_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['site_administration'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['site_administration_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['authentication_and_authorization'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['authentication_and_authorization_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['groups'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['groups_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['users'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['users_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['postings'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['postings_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['blog_posts'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['blog_posts_text']).thenReturn(None)

        # the number of 'Add' buttons must be number_of_add_buttons
        expect(LibraryLoader.get_instance().bl).get_element_count(selector=locator['admin_main_page']['add_button'],
                assertion_operator=AssertionOperator.equal, expected_value=number_of_add_buttons).thenReturn(None)

        # the number of 'Change' buttons must be number_of_change_buttons
        expect(LibraryLoader.get_instance().bl).get_element_count(selector=locator['admin_main_page']['change_button'],
                assertion_operator=AssertionOperator.equal, expected_value=number_of_change_buttons).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['recent_actions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['recent_actions_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(selector=locator['admin_main_page']['my_actions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['admin_main_page']['my_actions_text']).thenReturn(None)

        # configure mock calls in _verify_links_on_admin_main_page()
        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['main_title'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['main_title_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['view_site'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['view_site_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['change_password'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['change_password_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['logout'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['logout_link']).thenReturn(None)

        # authentication and authorization section
        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['authentication_and_authorization'], attribute='href',
                assertion_operator=AssertionOperator.equal,
                assertion_expected=links['admin_main_page']['authentication_and_authorization_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['groups'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['groups_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['users'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['users_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['add_group'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['add_group_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['change_group'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['change_group_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['add_user'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['add_user_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['change_user'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['change_user_link']).thenReturn(None)

        # postings section
        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['postings'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['postings_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['blog_posts'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['blog_posts_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['add_blog_post'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['add_blog_post_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(selector=locator['admin_main_page']['change_blog_post'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['admin_main_page']['change_blog_post_link']).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & bl)
        admin_main_page = AdminMainPage()

        # method under test gets called
        admin_main_page.verify_admin_main_page(username=username)

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_click_on_add_group_button(self):
        # configure the mock browser library for click_on_add_group_button()'s calls
        expect(LibraryLoader.get_instance().bl).click(selector=locator['admin_main_page']['add_group']).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & bl)
        admin_main_page = AdminMainPage()

        # method under test gets called
        admin_main_page.click_on_add_group_button()

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()


if __name__ == '__main__':
    unittest.main()
