from playwright.sync_api import Page, expect


def test_openbrowser(page:Page):
    #Page  → Class
    #page  → Actual page object / pytest fixture
  page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # bydefault is open the chromium browser
  myurl= page.url
  print("title of page:",myurl)
  expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def test_verifyTitle(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php")
    title=page.title()
    print("my page title:",title)





