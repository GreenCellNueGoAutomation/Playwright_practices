

from playwright.sync_api import sync_playwright, expect


def test_hrm_login_url():
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            channel="chrome",
            slow_mo=300,
            args=[
                "--start-maximized",
                "--disable-notifications",
                "--window-size=1920,1080"
            ]
        )

        context = browser.new_context(record_video_dir="video"
                                      )

        page = context.new_page()

        page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

        expect(page).to_have_title("OrangeHRM")
        print(context.pages)
        print("title of the page :",page.title())
        print("title of the page :",page.url)
        page.reload()
        page.go_back()
        page.go_forward()
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.screenshot(path="screenshot")
        page.bring_to_front()
        page.wait_for_timeout(5000)
        page.close()










