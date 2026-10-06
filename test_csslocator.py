from playwright.sync_api import Page

# tag id   =    tag#id

#tag class =    tag.class

#tag attribute =  tag[attribute=value]

#tag class attribute  tag.class[attribute=value]


def test_css(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    #tag id
    #page.locator("input#small-searchterms").fill("T-Shirts")
    #page.locator("#small-searchterms").fill("T-Shirts")
    #page.wait_for_timeout(5000)

    # tag class
    page.locator("input.search-box-text").fill("T-shirt")
    page.locator(".search-box-text").fill("T-shirt")
    page.wait_for_timeout(5000)

    #tag attribute
    page.locator("input[name=q]").fill("T-shirt")
    page.locator("[name=q]").fill("T-shirt")
    page.wait_for_timeout(5000)

    # #tag class attribute
    page.locator('.search-box-text[value="Search store"]').fill("T-shirt")

  #  https: // demowebshop.tricentis.com /







