from itertools import count

from playwright.sync_api import Page,expect
import pytest

def compersionmethod(page :Page):
    page.goto("https://demowebshop.tricentis.com/")

    product=page.locator(".product-title")

    # 1.inner_text vs text_content()

    print("inner_text product :",product.nth(1).inner_text())
    # return the actual text
    print("text_content product:",product.text_content())
    # return the content with special char and space with text

    count =product.count()

    for i in range(count):
        print("inner_text product :", product.nth(1).inner_text())
        # return the actual text
        print("text_content product:", product.text_content())
      # product_name= product.text_content()
       #print(product_name.strip())  this remove the extra space

        # return the content with special char and space with text

 # 2.all_text_contents vs all_inner_text both return the list of collection

    product_names=product.all_text_contents() # return the list of collection [a,b,c]
    print(product_names)
    product_details=product.all_inner_texts() #return the list of collection [a,b,c]

    # 3.All

    name= product.all()

    print(name.locators[0].inner_text())