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

    def verify_url(self):
        """ Waits until the "Logout" Element appears enabled on the upper right side of the page
            Checks the page URL is the same as expected_main_page_url
        """
        self._loader.bl.wait_for_elements_state(selector=locators['logout'], state=ElementState.visible)
        # check the validity of the url on the main_page
        self._loader.bl.get_url(assertion_operator=AssertionOperator.equal, assertion_expected=expected_main_page_url)

    def verify_main_title_link(self):
        self._loader.bl.get_attribute(selector=locators['main_title'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['main_title'])

    def verify_view_site_link(self):
        self._loader.bl.get_attribute(selector=locators['view_site'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['view_site'])

    def verify_change_password_link(self):
        self._loader.bl.get_attribute(selector=locators['change_password'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['change_password'])

    def verify_logout_link(self):
        self._loader.bl.get_attribute(selector=locators['logout'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['logout'])

    # authentication and authorization section
    def verify_authentication_and_authorization_section_link(self):
        self._loader.bl.get_attribute(selector=locators['authentication_and_authorization'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['authentication_and_authorization'])

    def verify_groups_link(self):
        self._loader.bl.get_attribute(selector=locators['groups'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['groups'])

    def verify_users_link(self):
        self._loader.bl.get_attribute(selector=locators['users'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['users'])

    def verify_add_group_link(self):
        self._loader.bl.get_attribute(selector=locators['add_group'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_group'])

    def verify_change_group_link(self):
        self._loader.bl.get_attribute(selector=locators['change_group'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['change_group'])

    def verify_add_user_link(self):
        self._loader.bl.get_attribute(selector=locators['add_user'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_user'])

    def verify_change_user_link(self):
        self._loader.bl.get_attribute(selector=locators['change_user'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['change_user'])

    # postings section
    def verify_postings_section_link(self):
        self._loader.bl.get_attribute(selector=locators['postings'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['postings'])

    def verify_blog_posts_link(self):
        self._loader.bl.get_attribute(selector=locators['blog_posts'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['blog_posts'])

    def verify_add_blog_post_link(self):
        self._loader.bl.get_attribute(selector=locators['add_blog_post'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_blog_post'])

    def verify_change_blog_post_link(self):
        self._loader.bl.get_attribute(selector=locators['change_blog_post'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['change_blog_post'])

    def verify_main_title_text(self):
        self._loader.bl.get_text(selector=locators['main_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['main_title'])

    def verify_wellcome_user_x_text(self, username):
        """[X being the placeholder for username]
        Given the username (e.g. "Hakan"), this keyword verifies that a wellcome string appears mentioning the username

        Args:
            username ([str]): name of the user registered to the system
        """
        # user navigation bar on the upper right of the page
        expected_dynamic_user_tab_text = texts['dynamic_user_tab'] % username.upper()
        self._loader.bl.get_text(selector=locators['welcome_user_x'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected_dynamic_user_tab_text)

    def verify_view_site_text(self):
        self._loader.bl.get_text(selector=locators['view_site'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['view_site'])

    def verify_change_password_text(self):
        self._loader.bl.get_text(selector=locators['change_password'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['change_password'])

    def verify_logout_text(self):
        self._loader.bl.get_text(selector=locators['logout'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['logout'])

    def verify_site_administration_text(self):
        self._loader.bl.get_text(selector=locators['site_administration'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['site_administration'])

    def verify_authentication_and_authorization_text(self):
        self._loader.bl.get_text(selector=locators['authentication_and_authorization'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['authentication_and_authorization'])

    def verify_groups_text(self):
        self._loader.bl.get_text(selector=locators['groups'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['groups'])

    def verify_users_text(self):
        self._loader.bl.get_text(selector=locators['users'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['users'])

    def verify_postings_text(self):
        self._loader.bl.get_text(selector=locators['postings'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['postings'])

    def verify_blog_posts_text(self):
        self._loader.bl.get_text(selector=locators['blog_posts'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['blog_posts'])

    def verify_number_of_add_buttons(self):
        # the number of 'Add' buttons must be number_of_add_buttons
        logger.info(f"looking for Add buttons with XPATH = {locators['add_button']}")
        self._loader.bl.get_element_count(selector=locators['add_button'],
                assertion_operator=AssertionOperator.equal, expected_value=number_of_add_buttons)

    def verify_number_of_change_buttons(self):
        # the number of 'Change' buttons must be number_of_change_buttons
        logger.info(f"looking for Change buttons with XPATH = {locators['change_button']}")
        self._loader.bl.get_element_count(selector=locators['change_button'],
                assertion_operator=AssertionOperator.equal, expected_value=number_of_change_buttons)

    def verify_recent_actions_text(self):
        self._loader.bl.get_text(selector=locators['recent_actions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['recent_actions'])

    def verify_my_actions_text(self):
        self._loader.bl.get_text(selector=locators['my_actions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['my_actions'])

    def click_on_add_group_button(self):
        self._loader.bl.click(selector=locators['add_group'])

    def logout(self):
        self._loader.bl.click(selector=locators['logout'])

    def click_on_groups(self):
        """Causes a switch from MainPage to GroupsPage
        """
        self._loader.bl.click(selector=locators['groups'])