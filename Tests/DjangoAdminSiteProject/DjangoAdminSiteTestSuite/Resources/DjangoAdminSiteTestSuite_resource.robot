*** Settings ***
Documentation    Keywords available only to DjangoAdminSiteTestSuite.robot

*** Keywords ***
Add Group With Permissions
    [Arguments]     ${group_name}       ${permissions}
    Enter name for new group    group_name=${group_name}
    FOR  ${permision}  IN   @{permissions}
        ${found_permissions} =  Enter search term in available permissions filter   permission_search_term=${permision}
        Run Keyword If  ${found_permissions}    Choose all filtered permissions
        Clear Available Permissions Filter
    END
    Click on save button      # opens groups_page
    Verify groups page loaded   group_name=${group_name}
    Verify group added     group_name=${group_name}



