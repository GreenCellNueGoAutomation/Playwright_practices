
from playwright.sync_api import Page, expect
import pytest

# Login test data
login_test_data = [
    ("sumedhsonawane19@gmail.com", "Sumedh@123#", "valid"),
    ("sumedhsonawane19@gmail.com", "Sumedh@12#", "invalid"),
    ("sumedhsonawane19@gmail.com", "Sumedh@#", "invalid"),
    ("  ", "invalid", "invalid")
]


@pytest.mark.parametrize("email, password, validity", login_test_data)
def test_data_driven(email, password, validity, page: Page):

    page.goto("https://demowebshop.tricentis.com/login")

    page.locator("#Email").fill(email)
    page.locator("#Password").fill(password)
    page.locator("input[value='Log in']").click()

    # Validation
    if validity == "valid":

        logout_link = page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible(timeout=5000)

    else:

        error_message = page.locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000)

        expect(page).to_have_url(
            "https://demowebshop.tricentis.com/login"
        )

