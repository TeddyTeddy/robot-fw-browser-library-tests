from LibraryLoader import LibraryLoader
from MainPageLayoutData import number_of_add_buttons, number_of_change_buttons
from MainPageLocators import locators
from MainPageTexts import texts
from MainPageLinks import links, expected_main_page_url
from robot.api import logger
from Browser import ElementState, AssertionOperator


class MainPage:
    """
    This Robot Library contains keywords operating on the expected_main_page_url
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def go_to_main_page(self):
        self._loader.bl.go_to(url=expected_main_page_url)

    def verify_main_page(self, username):
        """
        If the login attempt is successful, user is redirected to admin main page. This test checks the success
        of the login attempt by waiting for 'logout' element in the admin main page.
        If the element is enabled, then the url of of the redirected page is checked against
        expected_main_page_url. Then the test verifies all the texts and the links on the admin main page
        :return: None
        """
        # at this stage, we expect a redirection to expected_main_page_url
        # wait until the Logout Element is enabled on the page
        self._loader.bl.wait_for_elements_state(selector=locators['logout'], state=ElementState.visible)
        # check the validity of the url on the main_page page
        self._loader.bl.get_url(assertion_operator=AssertionOperator.equal, assertion_expected=expected_main_page_url)

        # main_page is loaded at this point
        self._verify_texts_on_main_page(username)
        self._verify_links_on_main_page()

    def _verify_links_on_main_page(self):
        """
        Verify all the links on main_page on expected_main_page_url
        :return: None
        """
        self._loader.bl.get_attribute(selector=locators['main_title'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['main_title'])

        self._loader.bl.get_attribute(selector=locators['view_site'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['view_site'])

        self._loader.bl.get_attribute(selector=locators['change_password'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['change_password'])

        self._loader.bl.get_attribute(selector=locators['logout'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['logout'])

        # authentication and authorization section
        self._loader.bl.get_attribute(selector=locators['authentication_and_authorization'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['authentication_and_authorization'])

        self._loader.bl.get_attribute(selector=locators['groups'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['groups'])

        self._loader.bl.get_attribute(selector=locators['users'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['users'])

        self._loader.bl.get_attribute(selector=locators['add_group'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_group'])

        self._loader.bl.get_attribute(selector=locators['change_group'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['change_group'])

        self._loader.bl.get_attribute(selector=locators['add_user'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_user'])

        self._loader.bl.get_attribute(selector=locators['change_user'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['change_user'])

        # postings section
        self._loader.bl.get_attribute(selector=locators['postings'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['postings'])

        self._loader.bl.get_attribute(selector=locators['blog_posts'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['blog_posts'])

        self._loader.bl.get_attribute(selector=locators['add_blog_post'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_blog_post'])

        self._loader.bl.get_attribute(selector=locators['change_blog_post'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['change_blog_post'])

    def _verify_texts_on_main_page(self, username):
        """
        Verify all the texts on main_page on expected_main_page_url
        :return: None
        """
        self._loader.bl.get_text(selector=locators['main_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['main_title'])

        # user navigation bar on the upper right of the page
        expected_dynamic_user_tab_text = texts['dynamic_user_tab'] % username.upper()
        self._loader.bl.get_text(selector=locators['welcome_user_x'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected_dynamic_user_tab_text)

        self._loader.bl.get_text(selector=locators['view_site'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['view_site'])

        self._loader.bl.get_text(selector=locators['change_password'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['change_password'])

        self._loader.bl.get_text(selector=locators['logout'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['logout'])

        self._loader.bl.get_text(selector=locators['site_administration'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['site_administration'])

        self._loader.bl.get_text(selector=locators['authentication_and_authorization'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['authentication_and_authorization'])

        self._loader.bl.get_text(selector=locators['groups'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['groups'])

        self._loader.bl.get_text(selector=locators['users'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['users'])

        self._loader.bl.get_text(selector=locators['postings'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['postings'])

        self._loader.bl.get_text(selector=locators['blog_posts'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['blog_posts'])

        # the number of 'Add' buttons must be number_of_add_buttons
        logger.info(f"looking for Add buttons with XPATH = {locators['add_button']}")
        self._loader.bl.get_element_count(selector=locators['add_button'],
                assertion_operator=AssertionOperator.equal, expected_value=number_of_add_buttons)
        # the number of 'Change' buttons must be number_of_change_buttons
        logger.info(f"looking for Change buttons with XPATH = {locators['change_button']}")
        self._loader.bl.get_element_count(selector=locators['change_button'],
                assertion_operator=AssertionOperator.equal, expected_value=number_of_change_buttons)

        self._loader.bl.get_text(selector=locators['recent_actions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['recent_actions'])

        self._loader.bl.get_text(selector=locators['my_actions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['my_actions'])

    def click_on_add_group_button(self):
        """
        In main_page, it clicks on add_group button, once redirected to the add_group_page
        :return None
        """
        self._loader.bl.click(selector=locators['add_group'])
