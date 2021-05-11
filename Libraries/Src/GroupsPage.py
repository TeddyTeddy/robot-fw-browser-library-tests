from LibraryLoader import LibraryLoader
from ExpectedTexts import expected
from ExpectedAttributeValues import eav
from ExpectedLinks import links, expected_groups_page_url, base_link
from Locators import locator
from robot.api import logger
from Browser import ElementState, AssertionOperator
import re


class GroupsPage:
    """
    This Robot Library contains keywords operating on groups_page
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def verify_groups_page_loaded(self, group_name):

        self._loader.bl.wait_for_elements_state(selector=locator['groups_page']['select_group_to_change'], state=ElementState.visible)

        # groups_page is loaded at this point
        # verify that groups_page url is correct
        self._loader.bl.get_url(assertion_operator=AssertionOperator.equal, assertion_expected=expected_groups_page_url)

        self._verify_texts_on_groups_page(group_name)
        self._verify_links_on_groups_page(group_name)

    def _verify_texts_on_groups_page(self, group_name):

        self._loader.bl.get_text(selector=locator['groups_page']['breadcrumbs'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['groups_page']['breadcrumbs_text'])

        self._loader.bl.get_text(selector=locator['groups_page']['home_link'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['groups_page']['home_link_text'])

        self._loader.bl.get_text(selector=locator['groups_page']['authentication_and_authorization_link'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['groups_page']['authentication_and_authorization_link_text'])

        self._verify_dynamic_text_group_x_added_successfully(group_name)

        self._loader.bl.get_text(selector=locator['groups_page']['select_group_to_change'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['groups_page']['select_group_to_change_text'])

        self._loader.bl.get_attribute(selector=locator['groups_page']['search_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=eav['groups_page']['search_button_value'])

        self._loader.bl.get_text(selector=locator['groups_page']['action'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['groups_page']['action_text'])

        self._loader.bl.get_text(selector=locator['groups_page']['delete_selected_groups_option'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['groups_page']['delete_selected_groups_option_text'])

        self._verify_dynamic_text_x_of_y_selected()

        self._loader.bl.get_text(selector=locator['groups_page']['select_all_groups'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['groups_page']['select_all_groups_text'])

    def _verify_dynamic_text_group_x_added_successfully(self, group_name):
        group_x_added_successfully_text = expected['groups_page']['group_x_added_successfully_text'] % group_name

        self._loader.bl.get_text(selector=locator['groups_page']['group_x_added_successfully'],
                assertion_operator=AssertionOperator.equal, assertion_expected=group_x_added_successfully_text)

    def _verify_dynamic_text_x_of_y_selected(self):
        """x and y are dynamic numbers that are present in the following elements in groups_page:
                x_of_y_selected
                y_groups
           This method grabs y from y_groups element and then checks if y is in present in x_of_y_selected.
           If y is present, then assertion passes, otherwise assertion fails
           :return None
        """
        observed_x_of_y_selected = self._loader.bl.get_text(selector=locator['groups_page']['x_of_y_selected'])
        observed_y_groups = self._loader.bl.get_text(selector=locator['groups_page']['y_groups'])
        y = re.match(r'\d+', observed_y_groups).group(0)
        logger.info(f'Observed {y} groups')
        assert y in observed_x_of_y_selected

    def _verify_links_on_groups_page(self, group_name):

        self._loader.bl.get_attribute(selector=locator['groups_page']['home_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['groups_page']['home_link'])

        self._loader.bl.get_attribute(selector=locator['groups_page']['authentication_and_authorization_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['groups_page']['authentication_and_authorization_link'])

        self._loader.bl.get_attribute(selector=locator['groups_page']['add_group'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['groups_page']['add_group_link'])

        self._verify_dynamic_link_for_group_name(group_name)

    def _verify_dynamic_link_for_group_name(self, group_name):
        """
        An group element with text group_name is added in groups_page. This method checks that
        the element (which is an anchor with a dynamic href), contains the correct link
        :param group_name: the name of the group added to the group page (i.e. 'blog_editors')
        :return: None
        """
        added_group_locator = locator['groups_page']['generic_group_element'] % group_name
        group_link = self._loader.bl.get_attribute(selector=added_group_locator, attribute='href')
        # group link e.g:   https://glacial-earth-31542.herokuapp.com/admin/auth/group/168/change/
        match = re.search(links['groups_page']['added_group_link'], group_link)
        assert bool(match)


    def verify_group_added(self, group_name):
        # https://stackoverflow.com/questions/4302166/format-string-dynamically
        added_group_locator = locator['groups_page']['generic_group_element'] % group_name
        self._loader.bl.get_text(selector=added_group_locator,
            assertion_operator=AssertionOperator.equal, assertion_expected=group_name)

    def select_checkbox_for_group(self, group_name):
        group_element_checkbox_locator = locator['groups_page']['generic_group_element_checkbox'] % group_name
        self._loader.bl.click(selector=group_element_checkbox_locator)

    def select_delete_selected_groups_dropdown(self):
        self._loader.bl.click(selector=locator['groups_page']['default_option'])
        self._loader.bl.wait_for_elements_state(selector=locator['groups_page']['delete_selected_groups_option'], state=ElementState.visible)
        self._loader.bl.click(selector=locator['groups_page']['delete_selected_groups_option'])

    def press_go(self):
        self._loader.bl.click(selector=locator['groups_page']['go_button'])
