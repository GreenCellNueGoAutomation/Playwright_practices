from playwright.sync_api import Page,expect
import pytest

def text_radio_button(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    male_radio=page.locator("#male")

    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    # radio button should not be checked (default)
    expect(male_radio).not_to_be_checked()

    # select/check radio button
    male_radio.check()

    # # radio button checked
    expect(male_radio).to_be_checked()

    page.wait_for_timeout(5000)





