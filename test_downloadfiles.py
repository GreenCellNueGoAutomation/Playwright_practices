from playwright.sync_api import Page,expect


import pytest


def test_download_file(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("sumedh sonawane")
    page.locator("#generateTxt").click()

    page.on("download", lambda download:download.save_as("download/text12file.txt") )
    page.wait_for_timeout(5000)
    page.locator("txtDownloadLink").click()

