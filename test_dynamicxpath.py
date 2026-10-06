import pytest
from playwright.sync_api import Page,expect
import re


def test_dynamic(page:Page):
     page.goto("https://testautomationpractice.blogspot.com/")
     for i in range(5):
      button = page.locator("//button[text()='START' or text()='STOP']")
      button.click()
      page.wait_for_timeout(5000)

     #//button[@name="start" or @name="stop"]
     # //button[text()="START" or text()="STOP"]
     #//button[contains(@name,'st')]
     #//button[start-with(@name,'st')]


     def test_hande_dynamic_css(page:page):

         page.goto("https://testautomationpractice.blogspot.com/")
         for i in range(5):
             button = page.locator("button[name ^= 'st']")
             button.click()
             page.wait_for_timeout(5000)

            # button[name = 'start'], button[name = 'stop']
            # button[name ^= 'st']  # start-with() in xpath
            # button[name *= 'st] # equals to contains() in xpath


def test_handle_playwright(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    for i in range(5):
        button = page.get_by_role(role="button",name=re.compile('ST.*'))
        button.click()
        page.wait_for_timeout(5000)







