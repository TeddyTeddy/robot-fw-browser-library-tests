*** Settings ***
Documentation       This is a test suite for Django Admin Site
Resource            ../Common/CommonKeywords.robot
Resource            Resources/DjangoAdminSiteTestSuite_resource.robot

*** Test Cases ***
Logging In As Admin
    Go to login page
    Verify Login Page
    Login    ${CREDENTIALS}[valid_admin][username]     ${CREDENTIALS}[valid_admin][password]    # opens admin_main_page
    Verify main page      ${CREDENTIALS}[valid_admin][username]

Creating "Blog Editors" Group
    Go To Main Page
    Verify Main Page    ${CREDENTIALS}[valid_admin][username]
    Click On Add Group Button   # opens add_group_page
    Verify Add Group Page
    Add Group With Permissions  group_name=${BLOG_EDITORS_GROUP_NAME}     permissions=${BLOG_EDITORS_PERMISSIONS}     # opens groups_page

Creating "Group Editors" Group
    Go To Main Page
    Verify Main Page    ${CREDENTIALS}[valid_admin][username]
    Click On Add Group Button   # opens add_group_page
    Verify Add Group Page
    Add Group With Permissions  group_name=${GROUP_EDITORS_GROUP_NAME}     permissions=${GROUP_EDITORS_PERMISSIONS}     # opens groups_page

Deleting "Blog Editors" Group
    Select Checkbox For Group  group_name=${BLOG_EDITORS_GROUP_NAME}
    Select Delete Selected Groups Dropdown
    Press Go    # opens confirm_groups_deletions_page
    Verify Confirm Page     group_name=${BLOG_EDITORS_GROUP_NAME}
    Press Confirm Button

Deleting "Group Editors" Group
    Select Checkbox For Group  group_name=${GROUP_EDITORS_GROUP_NAME}
    Select Delete Selected Groups Dropdown
    Press Go    # opens confirm_groups_deletions_page
    Verify Confirm Page     group_name=${GROUP_EDITORS_GROUP_NAME}
    Press Confirm Button

