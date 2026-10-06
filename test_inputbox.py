from playwright.sync_api import Page,expect
import pytest

def test_input(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    text_box= page.locator("name")

    # verify the visiability of element
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    # check the attribute of the element
    expect(text_box).to_have_attribute("maxlength","15")

    # get attribute of the element
    maxlenght=text_box.get_attribute("maxlength")
    print("maxlength of attribute",maxlenght)

    # fill the text
    text_box.fill("sumedh sonawane")

    # get the input value from the text
    name=text_box.input_value()
    print("input value Entered",name)




