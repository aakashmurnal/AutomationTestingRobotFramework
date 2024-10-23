*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=data_test.csv    reader_class=generic_csv_reader    encoding=UTF-8    dialect=unix
Test Template    Enter Test Data On Search Field And Click On Search

*** Variables ***
${base_url}    https://www.google.co.in/
${search_bar_element_path}    //*[@title="Search"]
${selenium}    Selenium

*** Test Cases ***
01 - To Validate Search Filed With Different Data : ${TestData}
    [Documentation]    To Validate Search Filed With Different Data ${TestData[1]}
    [Tags]    Akash

*** Keywords ***
Enter Test Data On Search Field And Click On Search
    [Documentation]    This keyword is used to verify user is able to enter selenium on search field
    [Arguments]    ${TestData}
    Log    ${TestData[1]}
    Navigate Google Page
    Wait Until Element Is Visible    ${search_bar_element_path}
    Input Text    ${search_bar_element_path}    ${TestData[1]}
    Press Keys    None    ENTER
    Page Should Contain    ${selenium}
    Close Browser

Navigate Google Page
    [Documentation]    This keyword is used to navigate to google search page
    Open Browser    ${base_url}    chrome
    Maximize Browser Window
