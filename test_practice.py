from playwright.sync_api import Page, expect


def test_verifydashboard(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    expect(page.get_by_placeholder("Username")).to_have_value("Admin")

    page.get_by_placeholder("Password").fill("admin123")
    expect(page.get_by_placeholder("Password")).to_have_value("admin123")

    page.locator("button[type='submit']").click()

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    page.wait_for_timeout(5000)