from playwright.sync_api import Page,expect
import pytest

@pytest.mark.skip
def test_single_fileupload(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

# uploading single file

    page.locator("#singleFileInput").set_input_files("upload_file/trace viwer playwright.txt")
    page.wait_for_timeout(5000)
    page.locator("button:has-text('Upload Single File')").click()

    # validating the file
   # expect(page.locator("#singleFileStatus")).to_contain_text("trace viwer playwright.txt"")

   # upload the multiple files

    page.goto("https://testautomationpractice.blogspot.com/")


    file=['httpsgreencell.deepsense.devadmin.txt','trace viwer playwright.txt']
    page.locator("#multipleFilesInput").set_input_files(file)
     # or we can put directly path
    page.wait_for_timeout(5000)
    page.locator("button:has-text('Upload Multiple Files')").click()