from playwright.sync_api import Page,expect
import pytest


def test_mouse_hover(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1 = page.locator("#input1")
    input1.focus()

    page.keyboard.insert_text("Welcome")

    # CONTROL + A
    page.keyboard.press("Control+A")

    # CONTROL + C
    page.keyboard.press("Control+C")

    # Navigate to input2
    input2 = page.locator("#input2")
    input2.focus()

    # CONTROL + V
    page.keyboard.press("Control+V")
    expect(input2).to_have_value("Welecome")

    page.wait_for_timeout(5000)

   

