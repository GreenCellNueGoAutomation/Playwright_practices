from operator import truediv

from playwright.sync_api import Page,expect
import pytest
from tornado.concurrent import is_future


def select_date(page, target_year, target_month, target_date, is_future):

    while True:

        current_month = page.locator(".ui-datepicker-month").text_content()
        current_year = page.locator(".ui-datepicker-year").text_content()

        # Check whether target month and year are reached
        if current_month == target_month and current_year == target_year:
            break

        # Navigate to next or previous month
        if is_future:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

    # Get all dates from calendar
    all_date = page.locator(".ui-datepicker-calendar td").all()

    # Select target date
    for td in all_date:
        date_text = td.inner_text().strip()

        if date_text == target_date:
            td.click()
            break


def test_jquery_datepicker(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date_input=page.locator("#datepicker")
    # jquery date picker use the fill method as per the date format

    #  Approach 1
   #  date_input.fill("10/15/2025")  # mm/dd/yy
    #page.wait_for_timeout(5000)


    # Approach 2
 # Target date
    is_future = False
    year = "2025"
    month = "October"
    date = "15"

    # Open date picker
    date_input.click()

    # Select date
    select_date(page, year, month, date, is_future)

    # Print selected date
    print("Selected date:", date_input.input_value())

    # Verify selected date
    expect(date_input).to_have_value("10/15/2025")

    page.wait_for_timeout(5000)