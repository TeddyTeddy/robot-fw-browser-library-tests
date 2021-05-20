from LibraryLoader import LibraryLoader
from AdminMainPageLayoutData import number_of_add_buttons, number_of_change_buttons
from AdminMainPageLocators import *
from AdminMainPageTexts import *
from AdminMainPageLinks import *
from robot.api import logger
from Browser import ElementState, AssertionOperator


class AdminMainPage:
    """
    This Robot Library contains keywords operating on the expected_admin_main_page_url
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def go_to_admin_main_page(self):
        self._loader.bl.go_to(url=expected_admin_main_page_url)

    def verify_admin_main_page(self, username):
        """
        If the login attempt is successful, user is redirected to admin main page. This test checks the success
        of the login attempt by waiting for 'logout' element in the admin main page.
        If the element is enabled, then the url of of the redirected page is checked against
        expected_admin_main_page_url. Then the test verifies all the texts and the links on the admin main page
        :return: None
        """
        # at this stage, we expect a redirection to expected_admin_main_page_url
        # wait until the Logout Element is enabled on the page
        self._loader.bl.wait_for_elements_state(selector=logout, state=ElementState.visible)
        # check the validity of the url on the admin_main_page page
        self._loader.bl.get_url(assertion_operator=AssertionOperator.equal, assertion_expected=expected_admin_main_page_url)

        # admin_main_page is loaded at this point
        self._verify_texts_on_admin_main_page(username)
        self._verify_links_on_admin_main_page()

    def _verify_links_on_admin_main_page(self):
        """
        Verify all the links on admin_main_page on expected_admin_main_page_url
        :return: None
        """
        self._loader.bl.get_attribute(selector=main_title, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=main_title_link)

        self._loader.bl.get_attribute(selector=view_site, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=view_site_link)

        self._loader.bl.get_attribute(selector=change_password, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=change_password_link)

        self._loader.bl.get_attribute(selector=logout, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=logout_link)

        # authentication and authorization section
        self._loader.bl.get_attribute(selector=authentication_and_authorization, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=authentication_and_authorization_link)

        self._loader.bl.get_attribute(selector=groups, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=groups_link)

        self._loader.bl.get_attribute(selector=users, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=users_link)

        self._loader.bl.get_attribute(selector=add_group, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=add_group_link)

        self._loader.bl.get_attribute(selector=change_group, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=change_group_link)

        self._loader.bl.get_attribute(selector=add_user, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=add_user_link)

        self._loader.bl.get_attribute(selector=change_user, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=change_user_link)

        # postings section
        self._loader.bl.get_attribute(selector=postings, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=postings_link)

        self._loader.bl.get_attribute(selector=blog_posts, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=blog_posts_link)

        self._loader.bl.get_attribute(selector=add_blog_post, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=add_blog_post_link)

        self._loader.bl.get_attribute(selector=change_blog_post, attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=change_blog_post_link)

    def _verify_texts_on_admin_main_page(self, username):
        """
        Verify all the texts on admin_main_page on expected_admin_main_page_url
        :return: None
        """
        self._loader.bl.get_text(selector=main_title,
                assertion_operator=AssertionOperator.equal, assertion_expected=main_title_text)

        # user navigation bar on the upper right of the page
        expected_dynamic_user_tab_text = dynamic_user_tab_text % username.upper()
        self._loader.bl.get_text(selector=welcome_user_x,
                assertion_operator=AssertionOperator.equal, assertion_expected=expected_dynamic_user_tab_text)

        self._loader.bl.get_text(selector=view_site,
                assertion_operator=AssertionOperator.equal, assertion_expected=view_site_text)

        self._loader.bl.get_text(selector=change_password,
                assertion_operator=AssertionOperator.equal, assertion_expected=change_password_text)

        self._loader.bl.get_text(selector=logout,
                assertion_operator=AssertionOperator.equal, assertion_expected=logout_text)

        self._loader.bl.get_text(selector=site_administration,
                assertion_operator=AssertionOperator.equal, assertion_expected=site_administration_text)

        self._loader.bl.get_text(selector=authentication_and_authorization,
                assertion_operator=AssertionOperator.equal, assertion_expected=authentication_and_authorization_text)

        self._loader.bl.get_text(selector=groups,
                assertion_operator=AssertionOperator.equal, assertion_expected=groups_text)

        self._loader.bl.get_text(selector=users,
                assertion_operator=AssertionOperator.equal, assertion_expected=users_text)

        self._loader.bl.get_text(selector=postings,
                assertion_operator=AssertionOperator.equal, assertion_expected=postings_text)

        self._loader.bl.get_text(selector=blog_posts,
                assertion_operator=AssertionOperator.equal, assertion_expected=blog_posts_text)

        # the number of 'Add' buttons must be number_of_add_buttons
        logger.info(f"looking for Add buttons with XPATH = {add_button}")
        self._loader.bl.get_element_count(selector=add_button,
                assertion_operator=AssertionOperator.equal, expected_value=number_of_add_buttons)
        # the number of 'Change' buttons must be number_of_change_buttons
        logger.info(f"looking for Change buttons with XPATH = {change_button}")
        self._loader.bl.get_element_count(selector=change_button,
                assertion_operator=AssertionOperator.equal, expected_value=number_of_change_buttons)

        self._loader.bl.get_text(selector=recent_actions,
                assertion_operator=AssertionOperator.equal, assertion_expected=recent_actions_text)

        self._loader.bl.get_text(selector=my_actions,
                assertion_operator=AssertionOperator.equal, assertion_expected=my_actions_text)

    def click_on_add_group_button(self):
        """
        In admin_main_page, it clicks on add_group button, once redirected to the add_group_page
        :return None
        """
        self._loader.bl.click(selector=add_group)
