*** Settings ***
Documentation       This is a test suite for Django Admin Site
Resource            ../Common/CommonKeywords.robot
Resource            Resources/DjangoAdminSiteTestSuite_resource.robot

*** Test Cases ***
Logging In As Admin
    Login As Admin

Creating "Blog Editors" Group
    Create "Blog Editors" Group




