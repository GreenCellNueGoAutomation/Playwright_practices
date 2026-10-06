from playwright.sync_api import Page,expect
import pytest

def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select single dropdown 3 way
    # 1.by label
    page.locator("#country").select_option("India")   # by label
    page.locator("#country").select_option(label="India") # By label
    page.wait_for_timeout(5000)


    # 2.by value
    page.locator("#country").select_option("India") # select by value
    page.locator("#country").select_option(value="India")
    page.wait_for_timeout(5000)


    # 3.select by index
    page.locator("#country").select_option(index=2) # index is starting from 0
    page.wait_for_timeout(5000)

    # 4 check the number of option in dropdown
    dropdown_option= page.locator("#country>option")
    expect(dropdown_option).to_have_count(10)

    # 5 print the exact text in console

    options_text=[text.strip() for text in dropdown_option.all_text_contents()]
    # text is new variable to store the value and then
    # text.strip trim the gap and store the exact match value
    # this is print the list all
    print(options_text)

    page.wait_for_timeout(5000)

 # if you want print one by one
    for option in options_text:
        print(option)
        page.wait_for_timeout(5000)
