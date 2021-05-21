from LibraryLoader import LibraryLoader
from GroupsPageTexts import texts
from GroupsPageElementsAttributes import eav
from GroupsPageLinks import links, expected_groups_page_url, base_link
from GroupsPageLocators import locator
from robot.api import logger
from Browser import ElementState, AssertionOperator, SelectAttribute
import re


class GroupsPage:
    """
    This Robot Library contains keywords operating on groups_page
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def verify_groups_page_loaded(self, group_name):

        self._loader.bl.wait_for_elements_state(selector=locator['select_group_to_change'], state=ElementState.visible)

        # groups_page is loaded at this point
        # verify that groups_page url is correct
        self._loader.bl.get_url(assertion_operator=AssertionOperator.equal, assertion_expected=expected_groups_page_url)

        self._verify_texts_on_groups_page(group_name)
        self._verify_links_on_groups_page(group_name)

    def _verify_texts_on_groups_page(self, group_name):

        self._loader.bl.get_text(selector=locator['breadcrumbs'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['breadcrumbs'])

        self._loader.bl.get_text(selector=locator['home_link'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['home_link'])

        self._loader.bl.get_text(selector=locator['authentication_and_authorization_link'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['authentication_and_authorization_link'])

        self._verify_dynamic_text_group_x_added_successfully(group_name)

        self._loader.bl.get_text(selector=locator['select_group_to_change'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['select_group_to_change'])

        self._loader.bl.get_attribute(selector=locator['search_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=eav['search_button_value'])

        self._loader.bl.get_text(selector=locator['action'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['action'])

        self._loader.bl.get_text(selector=locator['delete_selected_groups_option'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['delete_selected_groups_option'])

        self._verify_dynamic_text_x_of_y_selected()

        self._loader.bl.get_text(selector=locator['select_all_groups'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['select_all_groups'])

    def _verify_dynamic_text_group_x_added_successfully(self, group_name):
        expected_text = texts['group_x_added_successfully'] % group_name

        self._loader.bl.get_text(selector=locator['group_x_added_successfully'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected_text)

    def _verify_dynamic_text_x_of_y_selected(self):
        """x and y are dynamic numbers that are present in the following elements in groups_page:
                x_of_y_selected
                y_groups
           This method grabs y from y_groups element and then checks if y is in present in x_of_y_selected.
           If y is present, then assertion passes, otherwise assertion fails
           :return None
        """
        observed_x_of_y_selected = self._loader.bl.get_text(selector=locator['x_of_y_selected'])
        observed_y_groups = self._loader.bl.get_text(selector=locator['y_groups'])
        y = re.match(r'\d+', observed_y_groups).group(0)
        logger.info(f'Observed {y} groups')
        logger.info(observed_x_of_y_selected)
        assert y in observed_x_of_y_selected

    def _verify_links_on_groups_page(self, group_name):

        self._loader.bl.get_attribute(selector=locator['home_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['home'])

        self._loader.bl.get_attribute(selector=locator['authentication_and_authorization_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['authentication_and_authorization'])

        self._loader.bl.get_attribute(selector=locator['add_group'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_group'])

        self._verify_dynamic_link_for_group_name(group_name)

    def _verify_dynamic_link_for_group_name(self, group_name):
        """
        An group element with text group_name is added in groups_page. This method checks that
        the element (which is an anchor with a dynamic href), contains the correct link
        :param group_name: the name of the group added to the group page (i.e. 'blog_editors')
        :return: None
        """
        added_group_locator = locator['generic_group_element'] % group_name
        group_link = self._loader.bl.get_attribute(selector=added_group_locator, attribute='href')
        logger.info(group_link)
        # group link e.g:   /admin/auth/group/168/change/
        match = re.search(links['added_group'], group_link)
        assert bool(match)


    def verify_group_added(self, group_name):
        # https://stackoverflow.com/questions/4302166/format-string-dynamically
        added_group_locator = locator['generic_group_element'] % group_name
        self._loader.bl.get_text(selector=added_group_locator,
            assertion_operator=AssertionOperator.equal, assertion_expected=group_name)

    def select_checkbox_for_group(self, group_name):
        group_element_checkbox_locator = locator['generic_group_element_checkbox'] % group_name
        self._loader.bl.click(selector=group_element_checkbox_locator)

    def select_delete_selected_groups_dropdown(self):
        self._loader.bl.click(selector=locator['default_option'])
        # NOTE: The following click does not work: https://github.com/MarketSquare/robotframework-browser/issues/987
        # self._loader.bl.wait_for_elements_state(selector=locator['delete_selected_groups_option'], state=ElementState.visible)
        # self._loader.bl.click(selector=locator['delete_selected_groups_option'])
        # NOTE: Instead, we have the following workaround:
        self._loader.bl.select_options_by(
                locator['delete_selected_groups_option_2'],
                SelectAttribute.text,
                texts['delete_selected_groups_option'])

    def press_go(self):
        self._loader.bl.click(selector=locator['go_button'])
