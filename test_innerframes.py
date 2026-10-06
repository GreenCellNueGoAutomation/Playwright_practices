from playwright.sync_api import Page,expect
import pytest

from playwright.sync_api import Page

def test_frame(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frame3= page.frame(url="https://ui.vision/demo/webtest/frames/frame_3") # grab the frame3
    frame3.locator("input[name='mytext3']").fill("welcome")

    child_frames=frame3.child_frames
    print("print the number of child frame inside the frame:-",len(child_frames))

    inner_frame=child_frames[0]
    radio_btn=inner_frame.get_by_label("I am a human")
    radio_btn.click()
    expect(radio_btn).to_be_checked()

    page.wait_for_timeout(5000)






