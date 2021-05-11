from LibraryLoader import LibraryLoader
from ExpectedTexts import expected
from ExpectedLinks import links, expected_add_group_page_url
from ExpectedAttributeValues import eav
from Locators import locator
from robot.api import logger
from Browser import ElementState, AssertionOperator, MouseButton
from ControlOption import ControlOption

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
        self._loader.bl.wait_for_elements_state(selector=locator['add_group_page']['title'], state=ElementState.visible)

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
        self._loader.bl.get_attribute(selector=locator['add_group_page']['save_and_add_another_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['save_and_add_another_button_text'])

        self._loader.bl.get_attribute(selector=locator['add_group_page']['save_and_continue_editing_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['save_and_continue_editing_button_text'])

        self._loader.bl.get_attribute(selector=locator['add_group_page']['save_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['save_button_text'])

    def _verify_texts_on_add_group_page(self):

        self._loader.bl.get_text(selector=locator['add_group_page']['breadcrumbs'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['breadcrumbs_text'])

        self._loader.bl.get_text(selector=locator['add_group_page']['add_group'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['add_group_text'])

        self._loader.bl.get_text(selector=locator['add_group_page']['name'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['name_text'])

        self._loader.bl.get_text(selector=locator['add_group_page']['permissions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['permissions_text'])

        self._loader.bl.get_text(selector=locator['add_group_page']['available_permissions_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['available_permissions_title_text'])

        self._loader.bl.get_text(selector=locator['add_group_page']['available_permissions_dropdown'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['available_permissions_dropdown_content'])

        self._loader.bl.get_attribute(selector=locator['add_group_page']['available_permissions_tooltip'], attribute='title',
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['available_permissions_tooltip_text'])

        self._loader.bl.get_text(selector=locator['add_group_page']['choose_all_permissions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['choose_all_permissions_text'])

        self._loader.bl.get_text(selector=locator['add_group_page']['help_to_select_multiple_permissions'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['help_to_select_multiple_permissions_text'])

        self._loader.bl.get_text(selector=locator['add_group_page']['chosen_permissions_title'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['chosen_permissions_text'])

        self._loader.bl.get_attribute(selector=locator['add_group_page']['chosen_permissions_tooltip'], attribute='title',
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['chosen_permissions_tooltip_text'])

        self._loader.bl.get_text(selector=locator['add_group_page']['chosen_permissions_dropdown'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['chosen_permissions_dropdown_text'])

        self._loader.bl.get_text(selector=locator['add_group_page']['remove_all_permissions_option'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['add_group_page']['remove_all_permissions_text'])

    def _verify_links_on_add_group_page(self):
        """
        Verify all the links on add_groups_page on expected_add_group_page_url
        :return: None
        """

        self._loader.bl.get_attribute(selector=locator['add_group_page']['home_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_group_page']['home_link'])

        self._loader.bl.get_attribute(selector=locator['add_group_page']['authentication_and_authorization_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_group_page']['authentication_and_authorization_link'])

        self._loader.bl.get_attribute(selector=locator['add_group_page']['groups_link'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_group_page']['groups_link'])

        self._loader.bl.get_attribute(selector=locator['add_group_page']['choose_all_permissions_option'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['add_group_page']['choose_all_permissions_link'])

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
        self._loader.bl.get_element_state(selector=locator['add_group_page']['remove_all_permissions_option'], state=ElementState.visible)

        if self._loader.bl.get_text(selector=locator['add_group_page']['chosen_permissions_dropdown']):
            self._loader.bl.get_attribute(selector=locator['add_group_page']['remove_all_permissions_option'], attribute='class',
                assertion_operator=AssertionOperator.equal, assertion_expected=eav['add_group_page']['remove_all_permissions_active'])
        else:
            self._loader.bl.get_attribute(selector=locator['add_group_page']['remove_all_permissions_option'], attribute='class',
                assertion_operator=AssertionOperator.equal, assertion_expected=eav['add_group_page']['remove_all_permissions_inactive'])

    def enter_name_for_new_group(self, group_name):
        self._loader.bl.fill_text(selector=locator['add_group_page']['input_name_field'], txt=group_name)

    def enter_search_term_in_available_permissions_filter(self, permission_search_term):
        self._loader.bl.fill_text(selector=locator['add_group_page']['input_permission_field'],
                                   txt=permission_search_term)
        # return True if there are permissions listed, otherwise return False
        return bool(self._loader.bl.get_text(selector=locator['add_group_page']['available_permissions_dropdown']))

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
        self._loader.bl.wait_for_elements_state(selector=locator['add_group_page']['generic_filtered_permission'], state=ElementState.visible)
        filtered_permission_elements = self._loader.bl.get_elements(selector=locator['add_group_page']['generic_filtered_permission'])
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
        self._loader.bl.click( locator['add_group_page']['choose_all_permissions_option'], MouseButton.left)
        # It then verifies that the permissions are added inside chosen_permissions_dropdown.
        self._verify_permissions_added(filtered_permissions)


    def _verify_permissions_added(self, filtered_permissions):  # use set operations like set1.contains(set2)
        """
        Verifies that filtered_permissions is found under chosen_permissions_dropdown. Fails with assert otherwise.
        :param filtered_permissions: a list of filtered & chosen permissions to be verified to be added inside
        chosen_permissions_dropdown as generic_chosen_permission
        :return:
        """
        chosen_permission_elements = self._loader.bl.get_elements(selector=locator['add_group_page']['generic_chosen_permission'])
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
        assert filtered_permissions.issuperset(chosen_permissions)

    def clear_available_permissions_filter(self):
        self._loader.bl.clear_text(selector=locator['add_group_page']['input_permission_field'])

    def click_on_save_button(self):
        self._loader.bl.click(selector=locator['add_group_page']['save_button'])

