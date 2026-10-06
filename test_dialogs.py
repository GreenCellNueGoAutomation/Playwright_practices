from playwright.sync_api import Page,expect
import pytest

@pytest.mark.skip
def test_date(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

   #Approrach 1
    # register event first before click the btn
    def handle_dialog(dialog):
        dialog.accept()
        page.on("dialog", handle_dialog)
        page.locator("#alertBtn").click() # after event btn is click
        page.wait_for_timeout(5000)


    #Approach 2
    @pytest.mark.skip
    def simple_dialog_handle(page:Page):
        page.goto("https://testautomationpractice.blogspot.com/")

        page.on("dialog", lambda dialog:dialog.accept)
        page.wait_for_timeout(3000)
        page.locator("#alertBtn").click()  # after event btn is click
        page.wait_for_timeout(5000)


  # confirmation dialog
@pytest.mark.skip
def confirmation_dialogs(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #page.on("dialog",lambda dialog:dialog.accept)
    page.on("dialog",lambda dialog:dialog.dismiss)
    page.wait_for_timeout(5000)
    page.locator("#confirmBtn").click()
    page.wait_for_timeout(5000)
    message= page.locator("#demo").inner_text()
    print("print the msg:",message)

    expect(page.locator("#demo")).to_have_text("You pressed OK!")


 # prompt dialogs


def prompt_dialogs(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog",lambda dialog:dialog.accept('sumeet'))
    #page.on("dialog",lambda dialog:dialog.dismiss)

    page.locator("promptBtn").click()
    msg=page.locator("demo").inner_text()
    print("output msg===>",msg)
    expect(page.locator("#demo")).to_have_text("Hello sumeet! How are you today?")

