from playwright.sync_api import Page, expect
import pytest

def test_sorted_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Get all dropdown options
    dropdown_option = page.locator("#colors > option")

    # Get option text and remove extra spaces
    option_dropdown = [
        text.strip() for text in dropdown_option.all_text_contents()
    ]

    #execute strip and return the cleaned text".

    # Copy the original list
    original_option = option_dropdown.copy()

    # Create sorted list
    sorted_list = sorted(option_dropdown)

    print("Original list:", original_option)
    print("Sorted list:", sorted_list)

    # Compare original and sorted lists
    if original_option == sorted_list:
        print("Dropdown options are in sorted order.")
    else:
        print("Dropdown options are not in sorted order.")