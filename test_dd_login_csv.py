
from playwright.sync_api import Page, expect
import pytest
import csv

# Empty list to store CSV data
login_data = []

# Read CSV file
with open("test_data/data.csv", newline="", encoding="utf-8") as csvfile:

    reader = csv.DictReader(csvfile)

    # Read each row from CSV
    for row in reader:
        login_data.append(
            (
                row["email"],
                row["password"],
                row["validity"]
            )
        )


# Parameterize test with CSV data
@pytest.mark.parametrize(
    "email, password, validity",
    login_data
)
def test_data_driven(email, password, validity, page: Page):

    # Open login page
    page.goto("https://demowebshop.tricentis.com/login")

    # Enter email
    page.locator("#Email").fill(email)

    # Enter password
    page.locator("#Password").fill(password)

    # Click Login
    page.locator("input[value='Log in']").click()

    # Validation
    if validity == "valid":

        # Verify Logout link is visible
        logout_link = page.locator("a[href='/logout']")

        expect(logout_link).to_be_visible(timeout=5000)

    else:

        # Verify error message is visible
        error_message = page.locator(".validation-summary-errors")

        expect(error_message).to_be_visible(timeout=5000)

        # Verify user remains on login page
        expect(page).to_have_url(
            "https://demowebshop.tricentis.com/login"
        )

