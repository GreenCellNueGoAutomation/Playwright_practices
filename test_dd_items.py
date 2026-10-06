import pytest
from playwright.sync_api import sync_playwright, Page, Expect, expect

search_item=['laptop','mobile','watch']


@pytest.mark.parametrize("item", search_item)
def test_dd_search(item,page :Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill(item)
    page.locator("input[value='Search']").click()
    #Assertion
    first_result=page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(item ,ignore_caase=True)

