from playwright.sync_api import sync_playwright
import pytest

from test_dd_items import search_item

search=["iphone","laptop","chair"]

@pytest.mark.parametrize("search_item", search)
def test_launch(search_item):
    with sync_playwright() as p:
        browser=p.chromium.launch(
            headless=False,
            channel="chrome",
            slow_mo=100

        )
        args = [
            "--start-maximized",
            "--disable-notifications",
            "--window-size=1050,1000"
        ]
        context= browser.new_context(
            record_video_dir="video")
        page=context.new_page()
        page.goto("https://www.flipkart.com/search?")
        page.get_by_placeholder("Search for products, brands and more").fill(search_item)
        page.wait_for_timeout(3000)
        page.locator("button[type='submit']").click()














