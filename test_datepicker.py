
from playwright.sync_api import Page,expect
import pytest

def test_jquery_datepicker(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.get_by_placeholder("Start Date").fill("2026-09-16")
    page.get_by_placeholder("End Date").fill("2026-09-22")

    page.wait_for_timeout(5000)