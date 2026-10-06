import pytest
from playwright.sync_api import Page, Playwright, expect


# direct injected user login with url
# https://httpbin.org/basic-auth/admin/password
# https://admin:password@httpbin.org/basic-auth/admin/password


def test_auth_popup_with_embedded_credentials(page: Page):
    page.goto("https://admin:password@httpbin.org/basic-auth/admin/password")
    page.wait_for_load_state("networkidle")
    expect(page.locator("body")).to_contain_text('"authenticated": true')


def test_auth_popup_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(
        http_credentials={
            "username": "admin",
            "password": "password",
        }
    )

    page = context.new_page()
    page.goto("https://httpbin.org/basic-auth/admin/password")
    expect(page.locator("body")).to_contain_text('"authenticated": true')

    context.close()
    browser.close()
