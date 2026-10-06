from playwright.sync_api import sync_playwright

def test_one():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,
                                  channel="chrome",
                                  slow_mo=200,
                                  args=["--start-maximized",
                                         "--disable-notification",
                                        "--window-size=1000,1000"
                                        ]

                                  )
        context1 = browser.new_context(viewport=
                   {
                "width": 1366,
                "height": 786
         },
            color_scheme="dark",
            record_video_dir="video"

        )
        context2=browser.new_context()
        page1=context1.new_page()
        page1.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page2=context2.new_page()
        page2.goto("https://greencell-nuego-web.web.app/confirmation")
        print(context1.pages)
        print(context2.pages)