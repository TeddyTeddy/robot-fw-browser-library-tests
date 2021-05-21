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

    def verify_add_group_page(self):
        """
        In admin_main_page, it clicks on add_group button, once redirected to the add_group_page.
        Once redirection occurs, this method checks for element title to be visible on add_group_page.
        Then it verifies that current url is expected_add_group_page_url
        It then verifies the page's texts and the links for correctness
        :return: None
        """
        # wait until the Logout Element is enabled on the page
        self._loader.bl.wait_for_elements_state(selector=locators['title'], state=ElementState.visible)

        # check the validity of the url on the add group page
        self._loader.bl.get_url(assertion_operator=AssertionOperator.equal, assertion_expected=expected_add_group_page_url)

        # at this point, the add_group_page is loaded
        self._verify_texts_on_add_group_page()
        self._verify_links_on_add_group_page()
        self._verify_the_buttons_on_add_group_page()


    def _verify_the_buttons_on_add_group_page(self):
        """
        Verifies the correctness of the value attribute in the following buttons:
            save_and_add_another_button
            save_and_continue_editing_button
            save_button
        :return: None
        """
        self._loader.bl.get_attribute(selector=locators['save_and_add_another_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['save_and_add_another_button_text'])

        self._loader.bl.get_attribute(selector=locators['save_and_continue_editing_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['save_and_continue_editing_button_text'])

        self._loader.bl.get_attribute(selector=locators['save_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['save_button_text'])

    def _verify_texts_on_add_group_page(self):

        self._loader.bl.get_text(selector=locators['breadcrumbs'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['breadcrumbs_text'])

        self._loader.bl.get_text(selector=locators['add_group'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['add_group_text'])

        self._loader.bl.get_text(selector=locators['name'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['name_text'])

        self._loader.bl.get_text(selector=locators['permissions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['permissions_text'])

        self._loader.bl.get_text(selector=locators['available_permissions_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['available_permissions_title_text'])

        self._loader.bl.get_text(selector=locators['available_permissions_dropdown'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['available_permissions_dropdown_content'])

        self._loader.bl.get_attribute(selector=locators['available_permissions_tooltip'], attribute='title',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['available_permissions_tooltip_text'])

        self._loader.bl.get_text(selector=locators['choose_all_permissions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['choose_all_permissions_text'])

        self._loader.bl.get_text(selector=locators['help_to_select_multiple_permissions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['help_to_select_multiple_permissions_text'])

        self._loader.bl.get_text(selector=locators['chosen_permissions_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['chosen_permissions_text'])

        self._loader.bl.get_attribute(selector=locators['chosen_permissions_tooltip'], attribute='title',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['chosen_permissions_tooltip_text'])

        self._loader.bl.get_text(selector=locators['chosen_permissions_dropdown'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['chosen_permissions_dropdown_text'])

        self._loader.bl.get_text(selector=locators['remove_all_permissions_option'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['remove_all_permissions_text'])

    def _verify_links_on_add_group_page(self):
        """
        Verify all the links on add_groups_page on expected_add_group_page_url
        :return: None
        """

        self._loader.bl.get_attribute(selector=locators['home_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['home_link'])

        self._loader.bl.get_attribute(selector=locators['authentication_and_authorization_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['authentication_and_authorization_link'])

        self._loader.bl.get_attribute(selector=locators['groups_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['groups_link'])

        self._loader.bl.get_attribute(selector=locators['choose_all_permissions_option'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['choose_all_permissions_link'])

        self._verify_remove_all_permission_link()

    def _verify_remove_all_permission_link(self):
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
        # IMPORTANT: There are 2 options here, only comment out one option at a time and run the test suite
        # *********************** OPTION #1 start **********************************************************
        self._loader.bl.type_text(selector=locators['input_permission_field'], txt=permission_search_term)
        # *********************** OPTION #1 end ************************************************************
        # *********************** OPTION #2 start **********************************************************
        # input_permission_field = self._loader.bl.get_element(selector=locators['input_permission_field)
        # logger.info(permission_search_term)
        # fill_text_js_function = ( 'function fill_permission_field() {\n'
        #        f'input_field = document.getElementById("id_permissions_input");\n'
        #        'input_field.focus();'
        #        f'permission_search_term = "{permission_search_term}"\n'
        #        'var i;\n'
        #        'for (i = 0; i < permission_search_term.length; i++) {\n'
        #         'input_field.dispatchEvent(new KeyboardEvent("keydown",  {"key":permission_search_term[i]}));\n'
        #        'input_field.dispatchEvent(new KeyboardEvent("keypress", {"key":permission_search_term[i]}));\n'
        #        'input_field.dispatchEvent(new KeyboardEvent("keyup", {"key":permission_search_term[i]}));\n'
        #       '}}\n'
        #      'fill_permission_field();\n'
        #)

        # self._loader.bl.execute_javascript(function=fill_text_js_function, selector=locators['input_permission_field)
        # *********************** OPTION #2 end **********************************************************

        # return True if there are permissions listed, otherwise return False
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
        # It then verifies that the permissions are added inside chosen_permissions_dropdown.
        self._verify_permissions_added(filtered_permissions)


    def _verify_permissions_added(self, filtered_permissions):  # use set operations like set1.contains(set2)
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
        # Why? because filtered_permissions is a larger set
        assert chosen_permissions.issuperset(filtered_permissions)

    def clear_available_permissions_filter(self):
        self._loader.bl.clear_text(selector=locators['input_permission_field'])

    def click_on_save_button(self):
        self._loader.bl.click(selector=locators['save_button'])

