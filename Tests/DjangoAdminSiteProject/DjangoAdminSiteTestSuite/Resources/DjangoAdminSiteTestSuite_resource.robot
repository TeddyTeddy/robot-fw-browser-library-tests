*** Settings ***
Documentation    Keywords available only To DjangoAdminSiteTestSuite.robot


*** Keywords ***
Add Group With Permissions
    [Documentation]     Assumes we are in AddGroup Page
    [Arguments]     ${group_name}       ${search_terms}
    Enter Name For New Group            ${group_name}
    FOR  ${search_term}  IN   @{search_terms}
        ${filtered_permissions} =    Enter Search Term In Available Permissions Filter  ${search_term}
        IF    ${filtered_permissions}
            ${filtered_permissions} =    Choose All Filtered Permissions
            Verify Permissions Added    ${filtered_permissions}
        END
        Clear Available Permissions Filter
    END
    Click On Save Button      # opens groups_page
    GroupsPage.Verify Url
    GroupsPage.Verify Group Added       ${group_name}

Verify Login Page
    LoginPage.Verify Title Text
    LoginPage.Verify Username Text
    LoginPage.Verify Password Text
    LoginPage.Verify Login Button Text

Verify Main Page
    [Arguments]     ${username}
    MainPage.Verify Url
    Verify Texts On Main Page   ${username}
    Verify Links On Main Page
    Verify Number Of Buttons On Main Page

Verify Links On Main Page
    MainPage.Verify Main Title Link
    MainPage.Verify View Site Link
    MainPage.Verify Change Password Link
    MainPage.Verify Logout Link
    MainPage.Verify Authentication And Authorization Section Link
    MainPage.Verify Groups Link
    MainPage.Verify Users Link
    MainPage.Verify Add Group Link
    MainPage.Verify Change Group Link
    MainPage.Verify Add User Link
    MainPage.Verify Change User Link
    MainPage.Verify Postings Section Link
    MainPage.Verify Blog Posts Link
    MainPage.Verify Add Blog Post Link
    MainPage.Verify Change Blog Post Link

Verify Texts On Main Page
    [Arguments]     ${username}
    MainPage.Verify Main Title Text
    MainPage.Verify Wellcome User X Text    ${username}
    MainPage.Verify View Site Text
    MainPage.Verify Change Password Text
    MainPage.Verify Logout Text
    MainPage.Verify Site Administration Text
    MainPage.Verify Authentication And Authorization Text
    MainPage.Verify Groups Text
    MainPage.Verify Users Text
    MainPage.Verify Postings Text
    MainPage.Verify Blog Posts Text

Verify Number Of Buttons On Main Page
    MainPage.Verify Number Of Add Buttons
    MainPage.Verify Number Of Change Buttons

Verify Add Group Page
    AddGroupPage.Verify Url
    Verify Texts On Add Group Page
    Verify Links On Add Group Page
    Verify Buttons On Add Group Page

Verify Texts On Add Group Page
    AddGroupPage.Verify Breadcrumbs Text
    AddGroupPage.Verify Add Group Text
    AddGroupPage.Verify Name Text
    AddGroupPage.Verify Permissions Text
    AddGroupPage.Verify Available Permissions Text
    AddGroupPage.Verify Available Permissions ToolTip Text
    AddGroupPage.Verify Available Permissions Dropdown Text
    AddGroupPage.Verify Choose All Permissions Text
    AddGroupPage.Verify Help To Select Multiple Permissions Text
    AddGroupPage.Verify Chosen Permissions Title Text
    AddGroupPage.Verify Chosen Permissions Tooltip Text
    AddGroupPage.Verify Chosen Permissions DropDown Text
    AddGroupPage.Verify Remove All Permissions Text

Verify Links On Add Group Page
    AddGroupPage.Verify Home Link
    AddGroupPage.Verify Authentication And Authorization Link
    AddGroupPage.Verify Groups Link
    AddGroupPage.Verify Choose All Permissions Link
    AddGroupPage.Verify Remove All Permissions Link

Verify Buttons On Add Group Page
    AddGroupPage.Verify Save And Add Another Button
    AddGroupPage.Verify Save And Continue Editing Button
    AddGroupPage.Verify Save Button

Verify Groups Page
    [Arguments]     ${group_name}=${EMPTY}
    GroupsPage.Verify Url
    Verify Texts On Groups Page     ${group_name}
    Verify Links On Groups Page     ${group_name}

Verify Texts On Groups Page
    [Arguments]     ${group_name}
    GroupsPage.Verify Breadcrumbs Text
    GroupsPage.Verify Home Text
    GroupsPage.Verify Authentication And Authorization Text
    GroupsPage.Verify Select Group To Change Text
    GroupsPage.Verify Search Button Text
    GroupsPage.Verify Action Text
    GroupsPage.Verify Delete Selected Groups Option Text
    GroupsPage.Verify Select All Groups Text
    IF    $group_name
        GroupsPage.Verify Dynamic Text Group X Added Successfully    ${group_name}
    END
    GroupsPage.Verify Dynamic Text X Of Y Selected

Verify Links On Groups Page
    [Arguments]     ${group_name}
    GroupsPage.Verify Home Link
    GroupsPage.Verify Authentication And Authorization Link
    GroupsPage.Verify Add Group Link
    IF    $group_name
        GroupsPage.Verify Dynamic Link For Group Name    ${group_name}
    END
    IF    $group_name
        GroupsPage.Verify Group Added    ${group_name}
    END

Verify Confirm Page
    [Arguments]     ${group_name}
    ConfirmPage.Verify Url
    Verify Texts On Confirm Page     ${group_name}
    Verify Links On Confirm Page     ${group_name}

Verify Texts On Confirm Page
    [Arguments]     ${group_name}
    ConfirmPage.Verify Breadcrumbs Text
    ConfirmPage.Verify Are You Sure Headline Text
    ConfirmPage.Verify Are You Sure Question Text
    ConfirmPage.Verify Summary Text
    ConfirmPage.Verify Objects Text
    ConfirmPage.Verify Dynamic Group Text    ${group_name}
    ConfirmPage.Verify Confirm Deletion Button Text
    ConfirmPage.Verify Cancel Deletion Button Text

Verify Links On Confirm Page
    [Arguments]     ${group_name}
    ConfirmPage.Verify Home Link
    ConfirmPage.Verify Authentication And Authorization Link
    ConfirmPage.Verify Groups Link
    ConfirmPage.Verify Group X Link     ${group_name}
    ConfirmPage.Verify Cancel Deletion Button Link
