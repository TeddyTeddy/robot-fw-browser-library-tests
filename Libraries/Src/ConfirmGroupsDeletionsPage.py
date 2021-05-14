from LibraryLoader import LibraryLoader
from ExpectedTexts import expected
from ExpectedLinks import links, expected_groups_page_url, base_link
from Locators import locator
from Browser import ElementState, AssertionOperator
import re
from robot.api import logger

class ConfirmGroupsDeletionsPage:
    """
    This Robot Library contains keywords operating on the XXX
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def verify_confirm_group_deletions_page(self, group_name):

        self._loader.bl.wait_for_elements_state(selector=locator['confirm_groups_deletions_page']['are_you_sure_headline'], state=ElementState.visible)
        # at this stage, the page is assumed to be loaded
        # verify that confirm_groups_deletions_page url is correct
        self._loader.bl.get_url(assertion_operator=AssertionOperator.equal, assertion_expected=expected_groups_page_url)

        self._verify_texts_on_confirm_groups_deletions_page(group_name)
        self._verify_links_on_confirm_groups_deletions_page(group_name)

    def _verify_texts_on_confirm_groups_deletions_page(self, group_name):

        self._loader.bl.get_text(selector=locator['confirm_groups_deletions_page']['breadcrumbs'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['confirm_groups_deletions_page']['breadcrumbs_text'])

        self._loader.bl.get_text(selector=locator['confirm_groups_deletions_page']['are_you_sure_headline'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['confirm_groups_deletions_page']['are_you_sure_headline_text'])

        self._loader.bl.get_text(selector=locator['confirm_groups_deletions_page']['are_you_sure_question'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['confirm_groups_deletions_page']['are_you_sure_question_text'])

        self._loader.bl.get_text(selector=locator['confirm_groups_deletions_page']['summary'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['confirm_groups_deletions_page']['summary_text'])

        self._loader.bl.get_text(selector=locator['confirm_groups_deletions_page']['objects'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['confirm_groups_deletions_page']['objects_text'])

        group_locator = locator['confirm_groups_deletions_page']['generic_group_element'] % group_name
        self._loader.bl.get_text(selector=group_locator,
                assertion_operator=AssertionOperator.equal, assertion_expected=group_name)

        self._loader.bl.get_attribute(selector=locator['confirm_groups_deletions_page']['confirm_deletion_button'], attribute='value',
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['confirm_groups_deletions_page']['confirm_deletion_button_text'])

        self._loader.bl.get_text(selector=locator['confirm_groups_deletions_page']['cancel_deletion_button'],
                assertion_operator=AssertionOperator.equal, assertion_expected=expected['confirm_groups_deletions_page']['cancel_deletion_button_text'])


    def _verify_links_on_confirm_groups_deletions_page(self, group_name):
        self._loader.bl.get_attribute(selector=locator['confirm_groups_deletions_page']['home'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['confirm_groups_deletions_page']['home_link'])


        self._loader.bl.get_attribute(selector=locator['confirm_groups_deletions_page']['authentication_and_authorization'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['confirm_groups_deletions_page']['authentication_and_authorization_link'])


        self._loader.bl.get_attribute(selector=locator['confirm_groups_deletions_page']['groups'], attribute='href',
                assertion_operator=AssertionOperator.equal, assertion_expected=links['confirm_groups_deletions_page']['groups_link'])

        # the group to be deleted shows as an item under locator['confirm_groups_deletions_page']['objects']
        group_locator = locator['confirm_groups_deletions_page']['generic_group_element'] % group_name
        group_link = self._loader.bl.get_attribute(selector=group_locator, attribute='href')
        logger.info(group_link)
        # group link e.g:   /admin/auth/group/168/change/
        match = re.search(links['confirm_groups_deletions_page']['group_to_be_deleted_link'], group_link)
        assert bool(match)

        # cancel_deletion_button
        observed_cancel_deletion_button_link = self._loader.bl.get_attribute(
            selector=locator['confirm_groups_deletions_page']['cancel_deletion_button'], attribute='href')
        logger.info(observed_cancel_deletion_button_link)
        logger.info(links['confirm_groups_deletions_page']['cancel_deletion_button_link'])
        assert observed_cancel_deletion_button_link == links['confirm_groups_deletions_page']['cancel_deletion_button_link']

    def press_confirm_button(self):
        self._loader.bl.click(selector=locator['confirm_groups_deletions_page']['confirm_deletion_button'])

