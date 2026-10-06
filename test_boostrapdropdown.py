from itertools import count

from playwright.sync_api import Page,expect
import pytest


def test_boostrap_dropdown(page : Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()
    page.wait_for_timeout(5000)

    page.get_by_text("PIM").click()

    #click the job title dropdown
    page.locator("form i").nth(2).click()

    #capture all the option form dropdown
    options=page.locator("div[role='listbox'] span")

    counts=options.count()
    print("count the options",count)
    #assertion
    expect(options).to_have_count(counts) # assertion for counting the option

  # print the all the option
    print("all avaliable options==>",options.all_text_contents)

    # print all option using loop
    for i in range(counts):
        print(options.nth(i).text_content())

        # select/click specific option

        for i in range(count):
            txt= options.nth(i).inner_text()
            if txt=='Finance Manager':
                print("mathcing sucessfull")
                options.nth(i).click()
                break

            page.wait_for_timeout(5000)





