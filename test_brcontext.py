import pytest
from playwright.sync_api import Playwright, expect

# browser ==> context (user profile) ==> pages

def test_browser_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page1 = context.new_page()
    page2 = context.new_page()

    page1.goto("https://playwright.dev/java/")
    page1.wait_for_timeout(5000)

    expect(page1).to_have_title(
        "Playwright enables reliable web automation for testing, scripting, and AI agents."
    )

    page2.goto("https://www.selenium.dev/")
    page2.wait_for_timeout(5000)

    expect(page2).to_have_title("Selenium")





