import pytest

from playwright.sync_api import Playwright, expect


def test_popus_handle(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("popup", lambda popup: popup.wait_for_load_state())

    page.locator("#PopUp").click()

    page.wait_for_timeout(5000)

    all_pops = context.pages

    print("Total number of popup/pages:", len(all_pops))

    # Capture all page URLs
    for pw in all_pops:
        print("Popup/page URL =====>", pw.url)

        title = pw.title()
        print("Title =====>", title)

        if "Playwright" in title:
            pw.locator(".getStarted_Sjon").click()

            pw.wait_for_timeout(5000)

            expect(pw).to_have_title("Installation | Playwright Java")

            pw.close()
    context.close()
    browser.close()