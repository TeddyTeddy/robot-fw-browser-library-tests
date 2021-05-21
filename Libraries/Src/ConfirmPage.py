from LibraryLoader import LibraryLoader
from ConfirmPageTexts import texts
from ConfirmPageLinks import links, expected_confirmation_page_url
from ConfirmPageLocators import locators
from Browser import ElementState, AssertionOperator
import re
from robot.api import logger

class ConfirmPage:
    """
    This Robot Library contains keywords operating on the XXX
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def verify_confirm_page(self, group_name):

        self._loader.bl.wait_for_elements_state(selector=locators['are_you_sure_headline'], state=ElementState.visible)
        # at this stage, the page is assumed to be loaded
        # verify that confirm_groups_deletions_page url is correct
        self._loader.bl.get_url(assertion_operator=AssertionOperator.equal, assertion_expected=expected_confirmation_page_url)

        self._verify_texts_on_confirm_page(group_name)
        self._verify_links_on_confirm_page(group_name)

    def _verify_texts_on_confirm_page(self, group_name):

        self._loader.bl.get_text(selector=locators['breadcrumbs'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['breadcrumbs_text'])

        self._loader.bl.get_text(selector=locators['are_you_sure_headline'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['are_you_sure_headline_text'])

        self._loader.bl.get_text(selector=locators['are_you_sure_question'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['are_you_sure_question_text'])

        self._loader.bl.get_text(selector=locators['summary'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['summary_text'])

        self._loader.bl.get_text(selector=locators['objects'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['objects_text'])

        group_locator = locators['generic_group_element'] % group_name
        self._loader.bl.get_text(selector=group_locator,
                assertion_operator=AssertionOperator.equal, assertion_expected=group_name)

        self._loader.bl.get_attribute(selector=locators['confirm_deletion_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['confirm_deletion_button_text'])

        self._loader.bl.get_text(selector=locators['cancel_deletion_button'],
                assertion_operator=AssertionOperator.equal, assertion_expected=texts['cancel_deletion_button_text'])


    def _verify_links_on_confirm_page(self, group_name):
        self._loader.bl.get_attribute(selector=locators['home'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['home'])


        self._loader.bl.get_attribute(selector=locators['authentication_and_authorization'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['authentication_and_authorization'])


        self._loader.bl.get_attribute(selector=locators['groups'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['groups'])

        # the group to be deleted shows as an item under locators['objects']
        group_locator = locators['generic_group_element'] % group_name
        group_link = self._loader.bl.get_attribute(selector=group_locator, attribute='href')
        logger.info(group_link)
        # group link e.g:   /admin/auth/group/168/change/
        match = re.search(links['group_to_be_deleted'], group_link)
        assert bool(match)

        # cancel_deletion_button
        observed_cancel_deletion_button_link = self._loader.bl.get_attribute(
            selector=locators['cancel_deletion_button'], attribute='href')
        logger.info(observed_cancel_deletion_button_link)
        logger.info(links['cancel_deletion_button'])
        assert observed_cancel_deletion_button_link == links['cancel_deletion_button']

    def press_confirm_button(self):
        self._loader.bl.click(selector=locators['confirm_deletion_button'])

