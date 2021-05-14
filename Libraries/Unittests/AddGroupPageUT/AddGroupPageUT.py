import unittest
from mockito import unstub, verify, verifyNoUnwantedInteractions, expect, mock
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from Locators import locator, number_of_add_buttons, number_of_change_buttons
from AddGroupPage import AddGroupPage     # class under test (CUT)
from ExpectedLinks import expected_add_group_page_url, links
from ExpectedTexts import expected
from ExpectedAttributeValues import eav
from Browser import ElementState, AssertionOperator, MouseButton
from ControlOption import ControlOption

class AddGroupPageUT(unittest.TestCase):
    def setUp(self) -> None:  # before running an individual test case
        # instantiate a mock LibraryLoader, which returns a mock sl
        LibraryLoaderStub.configure_mock_library_loader()

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    @staticmethod
    def do_test_verify_add_group_page(chosen_permissions_dropdown_text):
        # configure the mock browser library for verify_add_group_page()'s calls
        # wait until title element is visible on add_group_page
        expect(LibraryLoader.get_instance().bl).wait_for_elements_state(
            selector=locator['add_group_page']['title'],
            state=ElementState.visible).thenReturn(None)

        # check the validity of the url on the add_group_page
        expect(LibraryLoader.get_instance().bl).get_url(
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected_add_group_page_url).thenReturn(None)

        # configure mock_calls in verify_texts_on_add_group_page()
        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['breadcrumbs'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['breadcrumbs_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['add_group'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['add_group_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['name'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['name_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['permissions'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['permissions_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['available_permissions_title'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['available_permissions_title_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['available_permissions_dropdown'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['available_permissions_dropdown_content']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(
            selector=locator['add_group_page']['available_permissions_tooltip'], attribute='title',
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['available_permissions_tooltip_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['choose_all_permissions'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['choose_all_permissions_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['help_to_select_multiple_permissions'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['help_to_select_multiple_permissions_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['chosen_permissions_title'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['chosen_permissions_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(
            selector=locator['add_group_page']['chosen_permissions_tooltip'], attribute='title',
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['chosen_permissions_tooltip_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['chosen_permissions_dropdown'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['chosen_permissions_dropdown_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['remove_all_permissions_option'],
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['remove_all_permissions_text']).thenReturn(None)

        # configure mock calls in _verify_links_on_add_group_page()
        expect(LibraryLoader.get_instance().bl).get_attribute(
            selector=locator['add_group_page']['home_link'], attribute='href',
            assertion_operator=AssertionOperator.equal,
            assertion_expected=links['add_group_page']['home_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(
            selector=locator['add_group_page']['authentication_and_authorization_link'],
            attribute='href',
            assertion_operator=AssertionOperator.equal,
            assertion_expected=links['add_group_page']['authentication_and_authorization_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(
            selector=locator['add_group_page']['groups_link'],
            attribute='href',
            assertion_operator=AssertionOperator.equal,
            assertion_expected=links['add_group_page']['groups_link']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(
            selector=locator['add_group_page']['choose_all_permissions_option'], attribute='href',
            assertion_operator=AssertionOperator.equal,
            assertion_expected=links['add_group_page']['choose_all_permissions_link']).thenReturn(None)

        # configure_mock_calls_in _verify_the_buttons_on_add_group_page()
        expect(LibraryLoader.get_instance().bl).get_attribute(
            selector=locator['add_group_page']['save_and_add_another_button'],
            attribute='value',
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['save_and_add_another_button_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(
            selector=locator['add_group_page']['save_and_continue_editing_button'],
            attribute='value',
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['save_and_continue_editing_button_text']).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_attribute(
            selector=locator['add_group_page']['save_button'],
            attribute='value',
            assertion_operator=AssertionOperator.equal,
            assertion_expected=expected['add_group_page']['save_button_text']).thenReturn(None)

        # configure mock calls in _verify_remove_all_permission_link()
        expect(LibraryLoader.get_instance().bl).get_element_state(
            selector=locator['add_group_page']['remove_all_permissions_option'],
            state=ElementState.visible).thenReturn( bool(chosen_permissions_dropdown_text) )

        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['chosen_permissions_dropdown']).thenReturn(chosen_permissions_dropdown_text)

        if chosen_permissions_dropdown_text:
            expect(LibraryLoader.get_instance().bl).get_attribute(
                selector=locator['add_group_page']['remove_all_permissions_option'],
                attribute='class',
                assertion_operator=AssertionOperator.equal,
                assertion_expected=eav['add_group_page']['remove_all_permissions_active']).thenReturn(None)
        else:
            # there are no permissions added to chosen_permissions_dropdown element
            expect(LibraryLoader.get_instance().bl).get_attribute(
                selector=locator['add_group_page']['remove_all_permissions_option'],
                attribute='class',
                assertion_operator=AssertionOperator.equal,
                assertion_expected=eav['add_group_page']['remove_all_permissions_inactive']).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        add_group_page.verify_add_group_page()

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_verify_add_group_page(self):
        # with permissions_drowdown_text is non empty string, "Remove all" button should be active
        AddGroupPageUT.do_test_verify_add_group_page(
            chosen_permissions_dropdown_text=expected['add_group_page']['auth-group-can_add_group'])
        self.tearDown()

        self.setUp()
        # with permissions_drowdown_text is an empty string, "Remove all" button should be inactive
        AddGroupPageUT.do_test_verify_add_group_page(chosen_permissions_dropdown_text='')

    def test_enter_name_for_new_group(self):
        # configure the mock browser library for enter_name_for_new_group()'s calls
        group_name = 'blog_editors'
        expect(LibraryLoader.get_instance().bl).fill_text(selector=locator['add_group_page']['input_name_field'], txt=group_name).thenReturn(None)
        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        add_group_page.enter_name_for_new_group(group_name=group_name)

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_enter_search_term_in_available_permissions_filter(self):
        self.do_test_enter_search_term_in_available_permissions_filter(permission_search_term='blog')
        self.tearDown()
        self.setUp()
        self.do_test_enter_search_term_in_available_permissions_filter(permission_search_term='yielding no permissions')

    def do_test_enter_search_term_in_available_permissions_filter(self, permission_search_term):
        expect(LibraryLoader.get_instance().bl).type_text(
            selector=locator['add_group_page']['input_permission_field'],
            txt=permission_search_term).thenReturn(None)

        dropdown_text = AddGroupPageUT.do_get_text_for_available_permissions_dropdown(permission_search_term)
        expect(LibraryLoader.get_instance().bl).get_text(
            selector=locator['add_group_page']['available_permissions_dropdown']).thenReturn(dropdown_text)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        permissions_found = add_group_page.enter_search_term_in_available_permissions_filter(
            permission_search_term=permission_search_term
        )

        self.assertEqual(bool(dropdown_text), permissions_found)
        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    @staticmethod
    def get_filtered_permission_elements():
        element_one = mock()
        element_one.text = expected['add_group_page']['auth-user-can_add_user']

        element_two = mock()
        element_two.text = expected['add_group_page']['auth-user-can_change_user']

        element_three = mock()
        element_three.text = expected['add_group_page']['auth-user-can_delete_user']

        return [element_one, element_two, element_three]

    def test_choose_all_filtered_permissions(self):
        # configure mock calls in choose_all_filtered_permissions()
        filtered_permission_elements = AddGroupPageUT.get_filtered_permission_elements()

        expect(LibraryLoader.get_instance().bl).wait_for_elements_state(
            selector=locator['add_group_page']['generic_filtered_permission'], state=ElementState.visible).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).get_elements(
            selector=locator['add_group_page']['generic_filtered_permission']).thenReturn(filtered_permission_elements)

        control_option = ControlOption()
        setattr(control_option, 'name', 'Control')
        for element in filtered_permission_elements:
            expect(LibraryLoader.get_instance().bl).get_text(element).thenReturn(element.text)
            expect(LibraryLoader.get_instance().bl).click( element, MouseButton.left, 1, None, None, None, False, False, ... ).thenReturn(None)

        expect(LibraryLoader.get_instance().bl).click( locator['add_group_page']['choose_all_permissions_option'], MouseButton.left).thenReturn(None)

        # configure mock calls in _verify_permissions_added()
        chosen_permission_elements = AddGroupPageUT.get_filtered_permission_elements()
        expect(LibraryLoader.get_instance().bl).get_elements(
            selector=locator['add_group_page']['generic_chosen_permission']).thenReturn(chosen_permission_elements)

        for element in chosen_permission_elements:
            expect(LibraryLoader.get_instance().bl).get_text(element).thenReturn(element.text)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        add_group_page.choose_all_filtered_permissions()

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_clear_available_permissions_filter(self):
        # configure the mock browser library for clear_available_permissions_filter()'s calls
        expect(LibraryLoader.get_instance().bl).clear_text(selector=locator['add_group_page']['input_permission_field']).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        add_group_page.clear_available_permissions_filter()

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_click_on_save_button(self):
        # configure the mock browser library for click_on_save_button()'s calls
        expect(LibraryLoader.get_instance().bl).click(selector=locator['add_group_page']['save_button']).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        add_group_page.click_on_save_button()

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    @staticmethod
    def do_get_text_for_available_permissions_dropdown(permission_search_term):
        if permission_search_term == 'blog':
            return expected['add_group_page']['postings-blog post-can_add_blog_post'] + '\n' + \
                   expected['add_group_page']['postings-blog post-can_add_blog_post'] + '\n' + \
                   expected['add_group_page']['postings-blog post-can_add_blog_post']
        elif permission_search_term == 'yielding no permissions':
            return ''
        else:
            raise AssertionError(f'What to yield in get_text for "{permission_search_term}"? Implement it here')


if __name__ == '__main__':
    unittest.main()
