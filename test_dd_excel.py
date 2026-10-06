
'''

read the data from excel file install the
pip install openpyxl

'''
import openpyxl
from playwright.sync_api import Page, expect
import pytest

# reading the data
login_data=[]
workbook=openpyxl.load_workbook("test_data/data.xlsx")
sheet=workbook.active  # we can specifiy the name of sheet or active


# reading the data from excel sheet using for loop


for row in sheet.iter_rows(min_row=2,values_only=True):
    email,password,validity=row
    login_data.append((str(email or ""),str(password or ""),str(validity or "")))


# Parameterize test with CSV data
@pytest.mark.parametrize("email,password,validity",login_data)
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

