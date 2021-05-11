*** Settings ***
Documentation       This is a test suite for Django Admin Site
Resource            ../Common/CommonKeywords.robot
Resource            Resources/DjangoAdminSiteTestSuite_resource.robot

*** Test Cases ***
Logging In As Admin
    Login As Admin

Creating "Blog Editors" Group
    Create "Blog Editors" Group

# Creating "Group Editors" Group
#    Create "Group Editors" Group

Deleting "Blog Editors" Group
    Delete "Blog Editors" Group

# Deleting "Group Editors" Group
#  Delete "Group Editors" Group

