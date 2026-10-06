from playwright.sync_api import Page,expect
import pytest

def test_date(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#txtDate").click()
    select_month = page.locator(".ui-datepicker-month")
    select_month.select_option("Oct")
    page.wait_for_timeout(5000)

    select_year=page.locator(".ui-datepicker-year").select_option("2025")
    page.wait_for_timeout(5000)

    select_date = page.locator("td[data-handler='selectDay']", has_text="15")
    select_date.click()
    page.wait_for_timeout(5000)

