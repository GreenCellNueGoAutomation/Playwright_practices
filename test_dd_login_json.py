
from playwright.sync_api import Page, expect
import pytest
import json

#read the json write the commnad
file=open("test_data/data.json","r")  # mention the json file path and r is read in-build commnad
# load the read file
login_data=json.load(file)



@pytest.mark.parametrize("email, password, validity",[
(data["email"],data["password"],data["validity"])for data in login_data])
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

