from playwright.sync_api import Page,expect
import pytest

from playwright.sync_api import Page

def test_frame(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames = page.frames  # return the list of frames

    print("Total frames:", len(frames))  # number of frame list

    for frame in frames:
        print("Frame URL:", frame.url)

    page.wait_for_timeout(5000)

    # frame 1
#frame1=page.frame_locator("frame[src='frame_1.html']") #option 1 get the frame using css

    frame1=page.frame(url="https://ui.vision/demo/webtest/frames/frame_1.html")
    #option 2 get the frame using the url of frame

   # frame1=page.frame("option 3 using the frame name") # get the frame using the frame name
    input_box=frame1.locator("input[name='mytext1']")
    page.wait_for_timeout(5000)
    input_box.fill("Welcome")
    expect(input_box).to_have_value("Welcome")



