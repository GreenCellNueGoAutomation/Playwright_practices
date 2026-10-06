import pytest
from playwright.sync_api import Page,expect


   #1.absoulte xapth
def test_xpath(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]")
    expect(logo).to_be_visible()

    #2.Reletive xpath
    expect(page.locator("img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(5000)

    #3 .xpath with contains
    products= page.locator("//h2//a[contains(@href,'computer')]")
    product_count=products.count()
    print("product count:",product_count)
    expect(product_count).to_equal(product_count)

    print("first Element :",products.first.text_content())
    print("first Element :", products.last.text_content())
    print("first Element :", products.nth(2).text_content())


    product_title=products.all_text_contents()
    print("print the title :",product_title)


    print("print the product title using loop statment.............")
    for i in product_title:
        print(i)



    # xpath with-start()

    product_name= page.locator("//h2//a[starts-with(@href,'/build')]")
    print("product name:",product_name.count())
    expect(product_name).to_have_count(product_name.count())

   # xpath with text()
    link=page.locator("//a[text()='Register']")
    expect(link).to_be_visible()

    # xpath with last()
    #page.locator("//div[@class='column follow-us']//li[5]") we can pass the index
    last= page.locator("//div[@class='column follow-us']//li[last()]")
    expect(last).to_have_text("Google+")

    # xpath with position
    lastlink = page.locator("//div[@class='column follow-us']//li[postion()=2]")
    expect(lastlink).to_have_text("Twitter")



























