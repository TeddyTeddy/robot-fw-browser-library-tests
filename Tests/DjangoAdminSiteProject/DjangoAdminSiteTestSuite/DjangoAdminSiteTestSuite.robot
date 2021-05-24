*** Settings ***
Documentation       This is a test suite for Django Admin Site
Resource            ../Common/CommonKeywords.robot
Resource            Resources/DjangoAdminSiteTestSuite_resource.robot

*** Keywords ***
Creating Group
    [Arguments]     ${username}         ${password}         ${group_name}       ${permissions}
    Go to login page
    Verify Login Page
    Login    ${username}     ${password}        # opens admin_main_page
    Verify main page      ${username}
    Click On Add Group Button                   # opens add_group_page
    Verify Add Group Page
    Add Group With Permissions  group_name=${group_name}     permissions=${permissions}     # opens groups_page
    Verify Groups Page      ${group_name}
    Logout

Deleting Group
    [Arguments]     ${username}         ${password}         ${group_name}
    Go to login page
    Verify Login Page
    Login    ${username}     ${password}        # opens admin_main_page
    Verify main page      ${username}
    Click On Groups
    Select Checkbox For Group  group_name=${group_name}
    Select Delete Selected Groups Dropdown
    Press Go    # opens confirm_groups_deletions_page
    Verify Confirm Page     group_name=${group_name}
    Press Confirm Button
    Verify Groups Page
    Logout

*** Test Cases ***
Creating Different Groups
    [Template]     Creating Group
    ${CREDENTIALS}[valid_admin][username]       ${CREDENTIALS}[valid_admin][password]    ${BLOG_EDITORS_GROUP_NAME}    ${BLOG_EDITORS_PERMISSIONS}
    ${CREDENTIALS}[valid_admin][username]       ${CREDENTIALS}[valid_admin][password]    ${GROUP_EDITORS_GROUP_NAME}   ${GROUP_EDITORS_PERMISSIONS}

Deleting "Blog Editors" Group
    [Template]      Deleting Group
    ${CREDENTIALS}[valid_admin][username]       ${CREDENTIALS}[valid_admin][password]    ${BLOG_EDITORS_GROUP_NAME}
    ${CREDENTIALS}[valid_admin][username]       ${CREDENTIALS}[valid_admin][password]    ${GROUP_EDITORS_GROUP_NAME}


