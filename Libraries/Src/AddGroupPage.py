from LibraryLoader import LibraryLoader
from AddGroupPageElementsAttributes import eav
from AddGroupPageLocators import locators
from AddGroupPageLinks import links, expected_add_group_page_url
from AddGroupPageTexts import texts
from robot.api import logger
from Browser import ElementState, AssertionOperator, MouseButton
from ControlOption import ControlOption
import re

class AddGroupPage:
    """
    This Robot Library contains keywords operating on the expected_admin_main_page_url
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def verify_url(self):
        """ Waits for the page's title to appear in the page. Then
            Verifies that URL of the page matches to expected_add_group_page_url
        """
        # wait until the Logout Element is enabled on the page
        self._loader.bl.wait_for_elements_state(selector=locators['title'], state=ElementState.visible)

        # check the validity of the url on the add group page
        self._loader.bl.get_url(assertion_operator=AssertionOperator.equal, assertion_expected=expected_add_group_page_url)


    def verify_save_and_add_another_button(self):
        self._loader.bl.get_attribute(selector=locators['save_and_add_another_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['save_and_add_another_button'])

    def verify_save_and_continue_editing_button(self):
        self._loader.bl.get_attribute(selector=locators['save_and_continue_editing_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['save_and_continue_editing_button'])

    def verify_save_button(self):
        self._loader.bl.get_attribute(selector=locators['save_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['save_button'])

    def verify_breadcrumbs_text(self):
        self._loader.bl.get_text(selector=locators['breadcrumbs'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['breadcrumbs'])

    def verify_add_group_text(self):
        self._loader.bl.get_text(selector=locators['add_group'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['add_group'])

    def verify_name_text(self):
        self._loader.bl.get_text(selector=locators['name'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['name'])

    def verify_permissions_text(self):
        self._loader.bl.get_text(selector=locators['permissions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['permissions'])

    def verify_available_permissions_text(self):
        self._loader.bl.get_text(selector=locators['available_permissions_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['available_permissions_title'])

    def verify_available_permissions_dropdown_text(self):
        self._loader.bl.get_text(selector=locators['available_permissions_dropdown'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['available_permissions_dropdown_content'])

    def verify_available_permissions_tooltip_text(self):
        self._loader.bl.get_attribute(selector=locators['available_permissions_tooltip'], attribute='title',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['available_permissions_tooltip'])

    def verify_choose_all_permissions_text(self):
        self._loader.bl.get_text(selector=locators['choose_all_permissions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['choose_all_permissions'])

    def verify_help_to_select_multiple_permissions_text(self):
        self._loader.bl.get_text(selector=locators['help_to_select_multiple_permissions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['help_to_select_multiple_permissions'])

    def verify_chosen_permissions_title_text(self):
        self._loader.bl.get_text(selector=locators['chosen_permissions_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['chosen_permissions'])

    def verify_chosen_permissions_tooltip_text(self):
        self._loader.bl.get_attribute(selector=locators['chosen_permissions_tooltip'], attribute='title',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['chosen_permissions_tooltip'])

    def verify_chosen_permissions_dropdown_text(self):
        self._loader.bl.get_text(selector=locators['chosen_permissions_dropdown'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['chosen_permissions_dropdown'])

    def verify_remove_all_permissions_text(self):
        self._loader.bl.get_text(selector=locators['remove_all_permissions_option'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['remove_all_permissions'])

    def verify_home_link(self):
        self._loader.bl.get_attribute(selector=locators['home_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['home_link'])

    def verify_authentication_and_authorization_link(self):
        self._loader.bl.get_attribute(selector=locators['authentication_and_authorization_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['authentication_and_authorization_link'])

    def verify_groups_link(self):
        self._loader.bl.get_attribute(selector=locators['groups_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['groups_link'])

    def verify_choose_all_permissions_link(self):
        self._loader.bl.get_attribute(selector=locators['choose_all_permissions_option'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['choose_all_permissions_link'])

    def verify_remove_all_permissions_link(self):
        """
        If there are no permissions added under chosen_permissions_dropdown element,
        then remove_all_permissions_option should not be active.
        Otherwise (there are permissions added under chosen_permissions_dropdown element),
        then remove_all_permissions_option should have the right class attribute and should be active.
        :return: None
        """
        # wait until the Logout Element is visible on the page
        self._loader.bl.get_element_state(selector=locators['remove_all_permissions_option'], state=ElementState.visible)

        if self._loader.bl.get_text(selector=locators['chosen_permissions_dropdown']):
            self._loader.bl.get_attribute(selector=locators['remove_all_permissions_option'], attribute='class',
                assertion_operator=AssertionOperator.equal, assertion_expected=eav['remove_all_permissions_active'])
        else:
            self._loader.bl.get_attribute(selector=locators['remove_all_permissions_option'], attribute='class',
                assertion_operator=AssertionOperator.equal, assertion_expected=eav['remove_all_permissions_inactive'])

    def enter_name_for_new_group(self, group_name):
        self._loader.bl.fill_text(selector=locators['input_name_field'], txt=group_name)

    def enter_search_term_in_available_permissions_filter(self, permission_search_term):
        """ We enter permission_search_term into the available permissions filter, which then shows
            the available permissions matching the permission_search_term.
            This keyword types the content of permission_search_term into the filter.
            After filtering operation, if the filtering operation yields any permission(s), then
            this keyword returns True, otherwise it returns false

        Args:
            permission_search_term (str): a search string to match the permissions against

        Returns:
            bool: True, if there are any permission(s) matching permission_search_term
                  False, if there are not any permissions matching permission_search_term
        """
        self._loader.bl.type_text(selector=locators['input_permission_field'], txt=permission_search_term)
        return bool(self._loader.bl.get_text(selector=locators['available_permissions_dropdown']))

    def choose_all_filtered_permissions(self):
        """
        Given that a search term is entered into input_permission_field, the available_permissions_dropdown
        lists filtered permissions. This method creates a list of all the filtered permissions. Then it selects
        each and every element in filtered_permissions_elements. Then it clicks
        on choose_all_permissions_option. It then verifies that the permissions are added inside
        chosen_permissions_dropdown.
        :return: None
        """
        # create a list of all the permissions listed inside available_permissions_dropdown
        self._loader.bl.wait_for_elements_state(selector=locators['generic_filtered_permission'], state=ElementState.visible)
        filtered_permission_elements = self._loader.bl.get_elements(selector=locators['generic_filtered_permission'])
        filtered_permissions = []
        for element in filtered_permission_elements:
            permission = self._loader.bl.get_text(element)
            logger.info(permission)
            filtered_permissions.append(permission)

        logger.info(filtered_permissions)

        # then select each and every element in filtered_permission_elements by pressing CTRL key and clicking on them
        control_option = ControlOption()
        setattr(control_option, 'name', 'Control')
        for element in filtered_permission_elements:
            self._loader.bl.click( element, MouseButton.left, 1, None, None, None, False, False, control_option )

        # Then it clicks on choose_all_permissions_option
        self._loader.bl.click( locators['choose_all_permissions_option'], MouseButton.left)
        return filtered_permissions


    def verify_permissions_added(self, filtered_permissions):  # use set operations like set1.contains(set2)
        """
        Verifies that filtered_permissions is found under chosen_permissions_dropdown. Fails with assert otherwise.
        :param filtered_permissions: a list of filtered & chosen permissions to be verified to be added inside
        chosen_permissions_dropdown as generic_chosen_permission
        :return:
        """
        chosen_permission_elements = self._loader.bl.get_elements(selector=locators['generic_chosen_permission'])
        chosen_permissions = []
        for element in chosen_permission_elements:
            permission = self._loader.bl.get_text(element)
            chosen_permissions.append(permission)
        chosen_permissions = set(chosen_permissions)
        filtered_permissions = set(filtered_permissions)
        logger.info(chosen_permissions)
        logger.info(filtered_permissions)
        # NOTE: sorted(chosen_permissions) == sorted(filtered_permissions) does not work.
        # TODO: Why the below statement works, even though filtered_permissions is not a larger set then filtered_permissions
        assert chosen_permissions.issuperset(filtered_permissions)

    def clear_available_permissions_filter(self):
        self._loader.bl.clear_text(selector=locators['input_permission_field'])

    def click_on_save_button(self):
        self._loader.bl.click(selector=locators['save_button'])

