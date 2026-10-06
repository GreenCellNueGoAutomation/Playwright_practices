from playwright.sync_api import Page,expect
import pytest

def test_multiple_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 way to select same like single dropdown
    # 1.label we need to pass multiple data create the list

   # page.locator("#colours").select_option(label=["Red","Blue","Green"]) # by label
    page.locator("#colors").select_option(["Red","Blue","Green"]) # by label

    page.wait_for_timeout(5000)

   # 2 by value keyword is most for multi select dropdown
    page.locator("#colors").select_option(value=["Red","Blue","Green"])

    # by index index keyword is most for multi select dropdown
    page.locator("#colors").select_option(index=[2,4])

    # count the number of options
    dropdown_options=page.locator("#colors>option")
    expect(dropdown_options).to_have_count(7)

    option=[text.strip() for text in dropdown_options().all_text_content]
    print(option)

    # print one by one
    for opt in option:
        print(opt)

    



