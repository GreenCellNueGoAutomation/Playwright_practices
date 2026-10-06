from playwright.sync_api import Page,expect
import pytest

#1 mouse hover
@pytest.mark.skip
def test_mouse_hover(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    pointme= page.locator(".dropbtn")
    pointme.hover()
    laptop=page.locator(".dropdown-content a:nth-child(2)")
    laptop.hover()
    page.wait_for_timeout(5000)

# 2 right click
@pytest.mark.skip

def test_mouse_right_click(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    button=page.locator(".context-menu-one")
    button.click(button="right") # perform the right click action --> right,left,middle


# 3 double click
@pytest.mark.skip

def test_mouse_double_click(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    double_click= page.locator("button[ondblclick='myFunction1()']")
    double_click.dblclick() # perform double click

# 4 drag and drop

def test_mouse_draganddrop(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source=page.locator("#draggable")
    target=page.locator("#droppable")

 # manual drag using hover
 # Approach 1
  #  source.hover()
  #  source.mouse.down()
  #  target.hover()
  #  target.mouse.up()
  #  page.wait_for_timeout(5000)

  #Approach 2 drag_to

    source.drag_to(target)
    page.wait_for_timeout(5000)





